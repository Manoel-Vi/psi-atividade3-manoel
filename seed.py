from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    autores = [
        Autor(nome = "Alisson Bezerra Cândido da Silva", pais = "São Fernando"),
        Autor(nome = "Lucival dos Santos Alves", pais = "Paraiba"),
        Autor(nome = "Gabriel de Medeiros Lima", pais = "Burguesia"),
    ]
    livros = [
        Livro(titulo = "Mortes", ano = 2009, disponivel = True, autor_id = 1),
        Livro(titulo = "Vidas", ano = 2020, disponivel = True, autor_id = 1),
        Livro(titulo = "Brasil contra o Mundo", ano = 2016, disponivel = False, autor_id = 2),
        Livro(titulo = "Julgadores", ano = 2008, disponivel = True, autor_id = 2),
        Livro(titulo = "Ps5 ou Xbox", ano = 2020, disponivel = False, autor_id = 3),
        Livro(titulo = "Filosofatos", ano = 2000, disponivel = True, autor_id = 3),
    ]

    session.add_all(autores)
    session.add_all(livros)
    session.commit()
