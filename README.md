# 🦠 Coleta e Envio de Dados COVID-19 para o Google BigQuery

Este projeto automatiza a coleta diária dos dados oficiais da COVID-19 no Brasil, disponibilizados pelo Brasil.IO, e realiza o processamento e envio direto para uma tabela no Google BigQuery. Com isso, é possível construir dashboards dinâmicos e análises avançadas, por exemplo, no Looker Studio.
___________

## 🚀 Objetivo
Criar um pipeline ETL confiável e automatizado para alimentar um banco de dados analítico, facilitando análises em larga escala e visualizações atualizadas sobre a evolução da pandemia.

___________
## 📦 Tecnologias Utilizadas

* Python 3.x

* Pandas

* Requests

* google-cloud-bigquery

* python-dotenv

* Google Cloud Platform (BigQuery, IAM, API)

* Looker Studio (Google Data Studio) para visualização

---
## 📂 Organização do projeto

* `Projeto Covid/src/main.py`        - Script principal com toda a lógica ETL
* `.env.example`                     - Modelo para variáveis de ambiente (credenciais e paths)
* `requirements.txt`                 - Bibliotecas necessárias para rodar o projeto
* `.gitignore`                       - Arquivos ignorados pelo Git (ex: credenciais)
* `README.md`                        - Documentação do projeto
---

## 🔁 Fluxo do Processo

* Download automático do dataset .csv.gz oficial do Brasil.IO

* Descompactação e leitura eficiente com Pandas

* Salvamento local do CSV com data no nome para versionamento

* Inclusão da coluna data_carga para controle de auditoria

* Envio programático para o BigQuery com schema definido

* Atualização da tabela usando WRITE_TRUNCATE para garantir dados frescos

* Possibilidade de integrar com agendadores como cron (Linux) ou Task Scheduler (Windows)

---

## ⚙️ Configurações Necessárias

- Gere uma conta de serviço e baixe a chave JSON no Google Cloud Console

- Atualize o arquivo .env com suas credenciais e caminhos locais

- Instale as dependências: pip install -r requirements.txt

- Execute o script principal: python src/main.py


## 🧠 Diferenciais Técnicos

- Controle de schema no envio ao BigQuery.
- Manipulação eficiente de arquivos `.csv.gz`.
- Coluna `data_carga` adicionada para auditoria.
- Pode ser integrado a um **agendador** (como `cron` ou `Task Scheduler`) para execuções automáticas.

---

## 📊 Dashboard criado com base nos dados (Looker Studio)

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

