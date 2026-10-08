# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?

Para filtrar os livros que estão dispóniveis e assim tornar a função esmprestar e devolver livros pratica, pois quando emprestamos o livro o valor de livro.disponivel se torna False, quando ele esta disponivel. Já quando ele esta indisponivel nós não conseguimos empresta-lo porém agora podemos devolve-lo atualizando o seu status de disponibilidade para True.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?

Para que as alterações fiquem salvas no banco de dados, atualizando o status do livro na função de emprestar e devolver.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?

Na consulta de buscar livros pelo autor, onde a gente digita o nome do autor e a partir dessa informação porcuramos um livro que contem o id do autor que tem esse nome informado, usando:

nome_autor = input("Digite o nome do Autor do livro que procura? ")
    stmt = select(Autor).where(Autor.nome.ilike(nome_autor))
    autor = session.scalars(stmt).first()
    if autor:
        for livro in autor.livros:
            print(f"- {livro.titulo} ({livro.ano})")
    else:
        print(f"Autor '{nome_autor}' não encontrado.")