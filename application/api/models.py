from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from database import Base
from sqlmodel import Field, Session, SQLModel, create_engine, select, Field
from datetime import date
from decimal import Decimal
import sqlalchemy as sa

class Transacao(Base):
    __tablename__ = 'transacao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    reg_ans = Column(Integer, ForeignKey('operadora.reg_ans'))
    cd_conta_contabil = Column(Integer)
    descricao = Column(String(255))
    vl_saldo_inicial = Column(Numeric(15, 2))
    vl_saldo_final = Column(Numeric(15, 2))

class Operadora(Base):
    __tablename__ = 'operadora'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reg_ans = Column(Integer, unique=True)
    cnpj = Column(String(15))
    razao_social = Column(String(255))
    nome_fantasia = Column(String(255))
    modalidade = Column(String(255))
    logradouro = Column(String(255))
    numero = Column(String(255))
    complemento = Column(String(255))
    bairro = Column(String(255))
    cidade = Column(String(255))
    uf = Column(String(255))
    cep = Column(Integer)
    ddd = Column(Integer)
    telefone = Column(String(255))
    fax = Column(String(255))
    endereco_eletronico = Column(String(255))
    representante = Column(String(255))
    cargo_representante = Column(String(255))
    regiao_de_comercializacao = Column(Integer)
    data_registro_ans = Column(Date)