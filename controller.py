from Model import Pessoa
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from hashlib import sha256


def retorna_session():
    USUARIO = "root"
    SENHA = "root"
    HOST = "localhost"
    BANCO = "sistema_login_simples_sqlalchemy"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)

    return Session()


class ControllerCadastro:
    @classmethod
    def verificar_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 5:
            return 2
        elif len(email) > 100:
            return 3
        elif len(senha) < 6 or len(senha) > 100:
            return 4
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()

        # pessoa = Pessoa(nome=nome, email=email, senha=senha)
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()
        print('usuario')
        print(usuario)
        if usuario:
            return 5

        dados_verificados = cls.verificar_dados(nome=nome, email=email, senha=senha)
        print(f"dados verificados: {dados_verificados}")
        if dados_verificados != 1:
            return dados_verificados

        try:
            senha = sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email, senha=senha)
            session.add_all([p1])
            session.commit()
            return 1

        except:
            return 6


class ControllerLogin:
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()

        senha = sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()
        if logado:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False

# ControllerCadastro.cadastrar('Jaézer', 'jaezer.17@gmail.com', '123456')