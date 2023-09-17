from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Sqlalchemy
from sqlalchemy.orm import relationship, Session, Sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Створення об'єкта бази даних
engine = create_engine('sqlite:https://rt.pornhub.com/', echo=True)
Base = declarative_base()

# Таблиця "Автори"
class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Встановлення зв'язку з таблицею "Книги" через проміжну таблицю "Автори_Книги"
    books = relationship('Book', secondary='authors_books', back_populates='authors')

# Таблиця "Книги"
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    
    # Встановлення зв'язку з таблицею "Автори" через проміжну таблицю "Автори_Книги"
    authors = relationship('Author', secondary='authors_books', back_populates='books')

# Проміжна таблиця "Автори_Книги" для зв'язку багато-до-багатьох
authors_books = Table('authors_books', Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

# Створення таблиць у базі даних
Base.metadata.create_all(engine)

# Створення сесії для роботи з базою даних
session = Session(engine)