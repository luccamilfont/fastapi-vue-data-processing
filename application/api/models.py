from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Numeric
from database import Base
from sqlmodel import Field, Session, SQLModel, create_engine, select, Field
from datetime import date
from decimal import Decimal
import sqlalchemy as sa

# class Ans_dado(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     data: date
#     reg_ans: int
#     cd_conta_contabil: str = Field(max_length=20)
#     descricao: str = Field(max_length=255)
#     vl_saldo_inicial: Decimal = Field(ge=2)
#     vl_saldo_final: Decimal = Field(ge=2)

# class Testes(SQLModel, table=True):
#     __tablename__ = 'teste_table'

#     id: int = Field(default=None, primary_key=True, index=True)
#     descricao: str = Field(sa_column=sa.Column(sa.String, index=True))

#     class Config:
#         arbitrary_types_allowed = True

class AsnDado(Base):
    __tablename__ = 'ans_dado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    reg_ans = Column(Integer)
    cd_conta_contabil = Column(Integer)
    descricao = Column(String(255))
    vl_saldo_inicial = Column(Numeric(15, 2))
    vl_saldo_final = Column(Numeric(15, 2))
