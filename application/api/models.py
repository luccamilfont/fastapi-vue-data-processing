from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from database import Base
from sqlmodel import Field, Session, SQLModel, create_engine, select, Field
from datetime import date
from decimal import Decimal
import sqlalchemy as sa

class AsnDado(Base):
    __tablename__ = 'ans_dado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    reg_ans = Column(Integer)
    cd_conta_contabil = Column(Integer)
    descricao = Column(String(255))
    vl_saldo_inicial = Column(Numeric(15, 2))
    vl_saldo_final = Column(Numeric(15, 2))
