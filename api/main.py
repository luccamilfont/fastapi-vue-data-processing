from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from datetime import date
from decimal import Decimal


class Ans_dado(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    data: date
    reg_ans: int
    cd_conta_contabil: str = Field(max_length=20)
    descricao: str = Field(max_length=255)
    vl_saldo_inicial: Decimal = Field(ge=0)
    vl_saldo_final: Decimal = Field(ge=0)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/ans_dados/")
def create_ans_dado(ans_dado: Ans_dado, session: SessionDep) -> Ans_dado:
    session.add(ans_dado)
    session.commit()
    session.refresh(ans_dado)
    return ans_dado


@app.get("/ans_dados/")
def read_ans_dados(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Ans_dado]:
    ans_dados = session.exec(select(Ans_dado).offset(offset).limit(limit)).all()
    return ans_dados


@app.get("/ans_dados/{ans_dado_id}")
def read_ans_dado(ans_dado_id: int, session: SessionDep) -> Ans_dado:
    ans_dado = session.get(Ans_dado, ans_dado_id)
    if not ans_dado:
        raise HTTPException(status_code=404, detail="Ans_dado not found")
    return ans_dado


@app.delete("/ans_dados/{ans_dado_id}")
def delete_ans_dado(ans_dado_id: int, session: SessionDep):
    ans_dado = session.get(Ans_dado, ans_dado_id)
    if not ans_dado:
        raise HTTPException(status_code=404, detail="Ans_dado not found")
    session.delete(ans_dado)
    session.commit()
    return {"ok": True}