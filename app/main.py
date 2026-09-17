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

@app.put("/livros/{id_livro}", response_model=LivroResposta, tags=["Livros"])
def atualizar_livro(
    id_livro: int,
    dados_livro: LivroCriacao,
    sessao_banco: Session = Depends(obter_sessao_banco),
):
    consulta = select(Livro).where(Livro.id == id_livro)
    resultado = sessao_banco.execute(consulta)
    livro = resultado.scalar_one_or_none()

    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    livro.titulo = dados_livro.titulo
    livro.autor = dados_livro.autor
    livro.ano_publicacao = dados_livro.ano_publicacao
    livro.disponivel = dados_livro.disponivel

    sessao_banco.commit()
    sessao_banco.refresh(livro)

    return livro