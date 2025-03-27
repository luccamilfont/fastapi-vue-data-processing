from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Depends
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List, Annotated
from datetime import date
from decimal import Decimal

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, connect_args=connect_args)

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)

# def get_session():
#     with Session(engine) as session:
#         yield session

# SessionDep = Annotated[Session, Depends(get_session)]

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

# @app.on_event("startup")
# def on_startup():
#     # create_db_and_tables()

# @app.post("/ans_dados/")
# def create_ans_dado(ans_dado: Ans_dado, session: SessionDep) -> Ans_dado:
#     session.add(ans_dado)
#     session.commit()
#     session.refresh(ans_dado)
#     return ans_dado

# @app.get("/ans_dados/")
# def read_ans_dados(
#     session: SessionLocal,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ) -> list[Ans_dado]:
#     ans_dados = session.exec(select(Ans_dado).offset(offset).limit(limit)).all()
#     return ans_dados


# @app.get("/ans_dados/{ans_dado_id}")
# def read_ans_dado(ans_dado_id: int, session: SessionDep) -> Ans_dado:
#     ans_dado = session.get(Ans_dado, ans_dado_id)
#     if not ans_dado:
#         raise HTTPException(status_code=404, detail="Ans_dado not found")
#     return ans_dado


# @app.delete("/ans_dados/{ans_dado_id}")
# def delete_ans_dado(ans_dado_id: int, session: SessionDep):
#     ans_dado = session.get(Ans_dado, ans_dado_id)
#     if not ans_dado:
#         raise HTTPException(status_code=404, detail="Ans_dado not found")
#     session.delete(ans_dado)
#     session.commit()
#     return {"ok": True}