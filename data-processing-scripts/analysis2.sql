SELECT operadora.*
FROM operadora
JOIN transacao ON operadora.reg_ans = transacao.reg_ans
WHERE transacao.vl_saldo_inicial < transacao.vl_saldo_final
    AND transacao.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND operadora.data_registro_ans >= NOW() - INTERVAL '1 YEAR'
GROUP BY operadora.id
LIMIT 10;