from sqlalchemy import select

from models import Livro

def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""

    titulo = input("Digite um trecho do titulo de livro que deseja emprestar? ")
    stmt = select(Livro).where(Livro.titulo.ilike(titulo))
    livro = session.scalars(stmt).first()
    if livro:
        if livro.disponivel == True:
            livro.disponivel == False
            print(f"Livro: {livro.titulo}, emprestado com sucesso.")
            session.commit()
        else:
            print(f"- {livro.titulo} (Autor: {livro.autor.nome}), está indisponível.")
    else:
        print("Livro não encontrado")

def devolver_livro(session, titulo):
    """Marque um livro como disponível."""

    titulo = input("Digite um trecho do titulo de livro que deseja emprestar? ")
    stmt = select(Livro).where(Livro.titulo.ilike(titulo))
    livro = session.scalars(stmt).first()
    if livro:
        if livro.disponivel == False:
            livro.disponivel == True
            print(f"Livro: {livro.titulo}, devolvido com sucesso.")
            session.commit()
        else:
            print(f"- {livro.titulo} (Autor: {livro.autor.nome}), jé está disponivel.")
    else:
        print("Livro não encontrado")
