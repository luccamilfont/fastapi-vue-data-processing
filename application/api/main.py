from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from typing import List, Annotated
from datetime import date
from decimal import Decimal
from fastapi.middleware.cors import CORSMiddleware
import os

URL_FRONT = os.getenv("URL_FRONT")
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
print(URL_FRONT)
origins = [
    URL_FRONT
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransacaoBase(BaseModel):
    data: date
    reg_ans: int
    cd_conta_contabil: int
    descricao: str
    vl_saldo_inicial: Decimal
    vl_saldo_final: Decimal

class OperadoraBase(BaseModel):
    reg_ans: int
    cnpj: str
    razao_social: str
    nome_fantasia: str
    modalidade: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    cep: int
    ddd: int
    telefone: str
    fax: str
    endereco_eletronico: str
    representante: str
    cargo_representante: str
    regiao_de_comercializacao: int
    data_registro_ans: date

def get_db():
    db= SessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/operadora/")
def create_operadora(operadora: OperadoraBase, db: db_dependency):
    db_operadora = models.Operadora(
        reg_ans=operadora.reg_ans,
        cnpj=operadora.cnpj,
        razao_social=operadora.razao_social,
        nome_fantasia=operadora.nome_fantasia,
        modalidade=operadora.modalidade,
        numero=operadora.numero,
        complemento=operadora.complemento,
        bairro=operadora.bairro,
        cidade=operadora.cidade,
        uf=operadora.uf,
        cep=operadora.cep,
        ddd=operadora.ddd,
        telefone=operadora.telefone,
        fax=operadora.fax,
        endereco_eletronico=operadora.endereco_eletronico,
        representante=operadora.representante,
        cargo_representante=operadora.cargo_representante,
        regiao_de_comercializacao=operadora.regiao_de_comercializacao,
        data_registro_ans=operadora.data_registro_ans,
    )

    try:
        db.add(db_operadora)
        db.commit()
        db.refresh(db_operadora) 

        return {"message": "'Operadora' created successfully", "id": db_operadora.id}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating 'Operadora': {e}")
    
@app.post("/transacao/")
def create_transacao(transacao: TransacaoBase, db: db_dependency):
    db_transacao = models.Transacao(
        data=transacao.data,
        reg_ans=transacao.reg_ans,
        cd_conta_contabil=transacao.cd_conta_contabil,
        descricao=transacao.descricao,
        vl_saldo_inicial=transacao.vl_saldo_inicial,
        vl_saldo_final=transacao.vl_saldo_final,
    )

    try:
        db.add(db_transacao)
        db.commit()
        db.refresh(db_transacao) 

        return {"message": "'Transação' created successfully", "id": db_transacao.id}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating 'Transação': {e}")

@app.get("/operadora/all")
async def read_all_operadora(db: db_dependency):
    result = db.query(models.Operadora).all()
    if not result:
        raise HTTPException(status_code=404, detail='Question is not found')
    return result