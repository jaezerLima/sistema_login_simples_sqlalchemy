import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("bd.txt", 'r') as arq:
    senha = arq.readlines()[0]


USUARIO = "root"
SENHA = senha
HOST = "localhost"
BANCO = "sistema_login_simples_sqlalchemy"
PORT = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(20))
    senha = Column(String(64))


Base.metadata.create_all(engine)

