from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Depends
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Annotated
from datetime import date
from decimal import Decimal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class AsnDadoBase(BaseModel):
    data: date
    reg_ans: int
    cd_conta_contabil: int
    descricao: str
    vl_saldo_inicial: Decimal
    vl_saldo_final: Decimal

def get_db():
    db= SessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/asnDado/")
def create_asn_dado(asn_dado: AsnDadoBase, db: Session = Depends(get_db)):
    db_asn_dado = models.AsnDado(
        data=asn_dado.data,
        reg_ans=asn_dado.reg_ans,
        cd_conta_contabil=asn_dado.cd_conta_contabil,
        descricao=asn_dado.descricao,
        vl_saldo_inicial=asn_dado.vl_saldo_inicial,
        vl_saldo_final=asn_dado.vl_saldo_final,
    )

    try:
        db.add(db_asn_dado)
        db.commit()
        db.refresh(db_asn_dado) 

        return {"message": "AsnDado created successfully", "id": db_asn_dado.id}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating AsnDado: {e}")