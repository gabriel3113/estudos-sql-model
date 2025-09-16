from __future__ import annotations
from sqlmodel import select
from .db import create_db_and_tables, get_session
from .models import Hero, Livros




def seed_data() -> None:
# Heroes de exemplo
    heroes = [
    Hero(name="Deadpond", secret_name="Dive Wilson"),
    Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
    Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
    ]


    # Livros de exemplo (corrigindo pequenos typos)
    livros = [
    Livros(book_name="Percy Jackson: O Ladrão de Raios", autor="Fulano de Tal", genero="Aventura"),
    Livros(book_name="Maze Runner: Correr ou Morrer", autor="Fulano de Tal", genero="Ficção"),
    ]


    with get_session() as session:
        session.add_all(heroes + livros)
        session.commit()




def print_all() -> None:
    with get_session() as session:
        print("\n📚 Livros:")
    for row in session.exec(select(Livros)).all():
        print(f"- [{row.id}] {row.book_name} — {row.autor} ({row.genero})")


    print("\n🦸 Heróis:")
    for row in session.exec(select(Hero)).all():
        age = f", {row.age} anos" if row.age is not None else ""
        print(f"- [{row.id}] {row.name} (segredo: {row.secret_name}{age})")




def main() -> None:
    print("🔹 Criando tabelas (se não existirem)...")
    create_db_and_tables()
    print("🔹 Inserindo dados de exemplo...")
    seed_data()
    print("🔹 Listando registros...")
    print_all()
    print("\n✅ Pronto! Banco em data/database.db")




if __name__ == "__main__":
    main()