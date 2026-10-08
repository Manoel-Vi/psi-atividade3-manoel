from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""

    stmt = select(Livro)
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"Livro: {livro.titulo}, Autor: {livro.autor.nome}")

def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""

    stmt = select(Livro)
    livros = session.scalars(stmt).all()
    for livro in livros:
        if livro.disponivel == True:
            print(f"Livro: {livro.titulo}")

def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""

    trecho = input("Digite um trecho do titulo de livro que procura? ")
    stmt = select(Livro).where(Livro.titulo.ilike(trecho))
    livro = session.scalars(stmt).first()
    if livro:
        print(f"- {livro.titulo} (Autor: {livro.autor.nome})")
    else:
        print("Livro não encontrado.")

def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""

    nome_autor = input("Digite o nome do Autor do livro que procura? ")
    stmt = select(Autor).where(Autor.nome.ilike(nome_autor))
    autor = session.scalars(stmt).first()
    if autor:
        for livro in autor.livros:
            print(f"- {livro.titulo} ({livro.ano})")
    else:
        print(f"Autor '{nome_autor}' não encontrado.")
