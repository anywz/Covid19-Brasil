import os
import requests
import gzip
import pandas as pd
from io import BytesIO
from datetime import datetime
from google.cloud import bigquery
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# ------- CONFIGURAÇÕES -------- #
URL_DADOS = "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"

# Variáveis de ambiente
PASTA_SAIDA = os.getenv("PASTA_SAIDA")
CHAVE_GOOGLE = os.getenv("CHAVE_GOOGLE")
PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
TABLE_ID = os.getenv("TABLE_ID")
# -------------------------------- #

# Nome do arquivo com data atual
data_hoje = datetime.today().strftime('%Y-%m-%d')
nome_arquivo = f"covid_CASOS_{data_hoje}.csv"
caminho_arquivo = os.path.join(PASTA_SAIDA, nome_arquivo)

try:
    print("📡 Baixando dados do Brasil.IO...")
    resposta = requests.get(URL_DADOS)
    resposta.raise_for_status()

    print("📦 Descompactando e lendo CSV...")
    arquivo = BytesIO(resposta.content)
    with gzip.open(arquivo, 'rt', encoding='utf-8') as f:
        df = pd.read_csv(f)

    print(f"📊 Dados carregados: {len(df):,} linhas")
    print(f"💾 Salvando arquivo como: {caminho_arquivo}")
    df.to_csv(caminho_arquivo, index=False, encoding='utf-8-sig')

    print("🚀 Preparando envio ao BigQuery...")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CHAVE_GOOGLE
    df = pd.read_csv(caminho_arquivo)

    df["date"] = pd.to_datetime(df["date"]).dt.date
    df["last_available_date"] = pd.to_datetime(df["last_available_date"], errors='coerce')
    df["data_carga"] = pd.to_datetime(datetime.now())

    client = bigquery.Client(project=PROJECT_ID)
    table_ref = client.dataset(DATASET_ID).table(TABLE_ID)

    schema = [
        bigquery.SchemaField("city", "STRING"),
        bigquery.SchemaField("city_ibge_code", "INTEGER"),
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("epidemiological_week", "INTEGER"),
        bigquery.SchemaField("estimated_population", "INTEGER"),
        bigquery.SchemaField("estimated_population_2019", "INTEGER"),
        bigquery.SchemaField("is_last", "BOOLEAN"),
        bigquery.SchemaField("is_repeated", "BOOLEAN"),
        bigquery.SchemaField("last_available_confirmed", "INTEGER"),
        bigquery.SchemaField("last_available_confirmed_per_100k_inhabitants", "FLOAT"),
        bigquery.SchemaField("last_available_date", "DATETIME"),
        bigquery.SchemaField("last_available_death_rate", "FLOAT"),
        bigquery.SchemaField("last_available_deaths", "INTEGER"),
        bigquery.SchemaField("order_for_place", "INTEGER"),
        bigquery.SchemaField("place_type", "STRING"),
        bigquery.SchemaField("state", "STRING"),
        bigquery.SchemaField("new_confirmed", "INTEGER"),
        bigquery.SchemaField("new_deaths", "INTEGER"),
        bigquery.SchemaField("data_carga", "DATETIME")
    ]

    job_config = bigquery.LoadJobConfig(
        schema=schema,
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()

    print("✅ Dados enviados com sucesso para o BigQuery!")

except Exception as e:
    print(f"❌ Erro durante o processo: {e}")
