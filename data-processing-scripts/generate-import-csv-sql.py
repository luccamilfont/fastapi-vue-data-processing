import os

files_dir = "E:/yourpathhere/files"

output_sql_file = "E:/yourpathhere/generated-import-csv.sql"

create_tables_sql = """
CREATE TABLE IF NOT EXISTS operadora (
    id SERIAL PRIMARY KEY,
    reg_ans INTEGER UNIQUE,
    cnpj VARCHAR(15),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(255),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(255),
    uf VARCHAR(255),
    cep INTEGER,
    ddd INTEGER,
    telefone VARCHAR(255),
    fax VARCHAR(255),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao INTEGER,
    data_registro_ans DATE
);

CREATE TABLE IF NOT EXISTS transacao_staging (
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil INTEGER,
    descricao VARCHAR(255),
    vl_saldo_inicial NUMERIC(15, 2),
    vl_saldo_final NUMERIC(15, 2)
);
"""

final_sql = """
CREATE TABLE IF NOT EXISTS transacao (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil INTEGER,
    descricao VARCHAR(255),
    vl_saldo_inicial NUMERIC(15, 2),
    vl_saldo_final NUMERIC(15, 2),
    FOREIGN KEY (reg_ans) REFERENCES operadora(reg_ans)
);

INSERT INTO transacao (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
SELECT t.data, t.reg_ans, t.cd_conta_contabil, t.descricao, t.vl_saldo_inicial, t.vl_saldo_final
FROM transacao_staging t
JOIN operadora o ON t.reg_ans = o.reg_ans;

TRUNCATE TABLE transacao_staging;
DROP TABLE IF EXISTS transacao_staging;
"""

with open(output_sql_file, "w") as f:
    f.write(create_tables_sql)
    f.write("\n")
    
    relatorio_cadop_path = os.path.join(files_dir, "Relatorio_cadop.csv").replace("\\", "/")
    
    f.write(f"""
COPY operadora (reg_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans)
FROM '{relatorio_cadop_path}'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');
""")
    f.write("\n")
    
    copy_template = """
COPY transacao_staging (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM '{file_path}'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');
"""
    
    for file_name in os.listdir(files_dir):
        if file_name.endswith(".csv") and file_name != "Relatorio_cadop.csv":
            file_path = os.path.join(files_dir, file_name).replace("\\", "/")
            copy_command = copy_template.format(file_path=file_path)
            f.write(copy_command)
            f.write("\n")
    
    f.write(final_sql)

print(f"SQL file generated: {output_sql_file}")
