CREATE TABLE IF NOT EXISTS ans_dado (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil INTEGER,
    descricao VARCHAR(255),
    vl_saldo_inicial NUMERIC(15, 2),
    vl_saldo_final NUMERIC(15, 2)
);

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere' 
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere' 
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere' 
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere' 
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere' 
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere' 
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');

COPY ans_dado(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'yourpathhere'
WITH (FORMAT CSV, HEADER TRUE, DELIMITER ';', NULL '');
