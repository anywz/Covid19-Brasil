# 🦠 Coleta e Envio de Dados COVID-19 para o Google BigQuery

Este projeto automatiza a coleta de dados da COVID-19 disponibilizados pelo [Brasil.IO](https://brasil.io/dataset/covid19/caso_full/) e realiza o envio dos dados tratados diretamente para uma tabela no Google BigQuery, facilitando a análise e visualização em dashboards como o Looker Studio.

## 🚀 Objetivo

Automatizar o processo de ETL (Extração, Transformação e Carga) de dados sobre a COVID-19 no Brasil para um banco de dados analítico, permitindo análises de larga escala com visualizações dinâmicas e atualizadas.

---

## 📦 Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**
- **Requests**
- **Google Cloud BigQuery**
- **Google Cloud SDK / API**
- **Dashboards via Looker Studio (Google Data Studio)**

---

## 📁 Estrutura do Projeto

```
📂 coleta_covid_bigquery/
├── coleta_covid_bigquery.py     # Script principal com a lógica de ETL
├── README.md                    # Documentação do projeto
├── .gitignore                   # Ignora arquivos sensíveis (ex: chave JSON)
```

---

## 🔁 Etapas do Processo

1. **Download automático** do dataset `.csv.gz` do Brasil.IO.
2. **Descompactação e leitura** eficiente do arquivo com Pandas.
3. **Salvamento local** do CSV tratado com nome contendo a data da coleta.
4. **Adição de coluna `data_carga`** para controle de versionamento.
5. **Envio automático** dos dados para o BigQuery.
6. **Atualização da tabela** no modo `WRITE_TRUNCATE` (sobrescreve os dados).

---

## ⚙️ Configurações Necessárias

1. **Credencial do Google Cloud**
   - Gere sua chave JSON de conta de serviço no [Google Cloud Console](https://console.cloud.google.com/).
   - Salve o caminho da chave na variável `CHAVE_GOOGLE`.

2. **Variáveis de configuração no script:**

```python
URL_DADOS = "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"
PASTA_SAIDA = "CAMINHO/LOCAL/PARA/SALVAR/ARQUIVO"
CHAVE_GOOGLE = "CAMINHO/DA/CHAVE.JSON"
PROJECT_ID = "seu-projeto-id"
DATASET_ID = "nome-do-dataset"
TABLE_ID = "nome-da-tabela"
```

---

## 🧠 Diferenciais Técnicos

- Script modular, limpo e documentado.
- Controle de schema no envio ao BigQuery.
- Manipulação eficiente de arquivos `.csv.gz`.
- Coluna `data_carga` adicionada para auditoria.
- Pode ser integrado a um **agendador** (como `cron` ou `Task Scheduler`) para execuções automáticas.

---

## 📊 Dashboard (Looker Studio)

> 🔗 https://lookerstudio.google.com/reporting/42e565b4-1d7d-4b01-8e3a-3a97bf0d244b

---

## 👨‍💻 Autor

**Aniel Torres**  
📧 aniel.vidaltorres@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/anieltorres/)  
🌐 [Portfólio]( https://github.com/anywz)

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

