# fastapi-vue-data-processing
_Last READ.ME update: 2025-03-28_

## Summary

This repository contains a series of scripts to facilitate handling data from a .csv, importing them into a Postgres database, which will be alimenting a fastapi and vue application that will display some data. The tools on here were built assuming a number of manual preparation steps were taken.

## data-processing-scripts/csv-standardization.py
**Requirements:** 
1. Download files from the folders respective to the last two years (as in 2025) from: https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/
2. Download Relatorio_cadop.csv from: https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/

- Standardizes .csv to be ready to be consumed for the database

**Execution:**

For every .zip in the "files" folder in the same directory as this script:
1. Extracts file (.csv)
2. Reads it
3. Checks "DATA" column and parses into pandas  datetime
4. Replaces ',' with '.'

## data-processing-scripts/generate-import-csv-sql.py
- Generates a script that creates a .sql script ready to import all data. The script create tables "operadora", "transacao", and uses "transacao_staging" as a pivot, later dropped, for values that would break the script, later merged into "transacao". Created and tested with PostgreSQL, but with a little tweaking should run any relational database.
- Replace files path accordingly

## application

The Vue + Vite and FastAPI application

### api (FastApi)
- Makes requests to the database, using SQLAlchemy and Pydantic. By default, creates the necessary tables when served.

#### Setup
0. Create a python virtual env:
```
python -m venv
.\venv\Scripts\Activate
pip install sqlmodel uvicorn fastapi sqlalchemy pydantic psycopg2 python-dotenv
python.exe -m pip install --upgrade pip

```

1. For serving the API, run:
```
uvicorn api/main:app --reload
```

#### Attention points
. If necessary, run ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser``` in the terminal before entering the venv

### front (Vue + Vite)
- Displays data fetched with axios from the API using vue-good-table-next.

#### Setup

```
npm install
npm run dev
```

### using .env
- Replace local variables in .../front/.env and .../api/.env

## fastapi-vue-data-processing-requests.postman_collection

- Collection prepared to run GET requests from Postman
- http://127.0.0.1:8000/docs is also usable for testing the requests

## .sql queries
### analysis1.sql
- Query created to get "operadora"s with highest debt in the last trimestre in the "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"

### analysis2.sql
- Query created to get "operadora"s with highest deb in the last year in the same category as the previous file