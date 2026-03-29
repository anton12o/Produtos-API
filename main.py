from contextlib import asynccontextmanager
from typing import Optional, Annotated
from fastapi import Depends, FastAPI, Query, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


class Produtos(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    preco: float
    descricao: str


class ProdutoCreate(SQLModel):
    nome: str
    preco: float
    descricao: str


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ativo!"}


@app.post("/produtos/", response_model=Produtos)
def create_produto(produto: ProdutoCreate, session: SessionDep):
    db_produto = Produtos.model_validate(produto)
    session.add(db_produto)
    session.commit()
    session.refresh(db_produto)
    return db_produto


@app.get("/produtos/", response_model=list[Produtos])
def read_produtos(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    return session.exec(select(Produtos).offset(offset).limit(limit)).all()


@app.get("/produtos/{produto_id}", response_model=Produtos)
def read_produto(produto_id: int, session: SessionDep):
    produto = session.get(Produtos, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return produto


@app.delete("/produtos/{produto_id}")
def delete_produto(produto_id: int, session: SessionDep):
    produto_db = session.get(Produtos, produto_id)
    if not produto_db:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    session.delete(produto_db)
    session.commit()
    return {"ok": True, "message": f"Produto {produto_id} deletado com sucesso"}