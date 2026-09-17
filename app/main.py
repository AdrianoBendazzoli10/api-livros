from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import BaseBanco, mecanismo_banco, obter_sessao_banco
from app.models import Livro
from app.schemas import LivroCriacao, LivroResposta


BaseBanco.metadata.create_all(bind=mecanismo_banco)

app = FastAPI(
    title="API de Livros",
    version="1.0.0",
    description="API didática para gerenciamento de livros.",
)