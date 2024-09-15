# O models é onde trabalhamos com o banco de dados no nosso site
from FakePintrest import database
from datetime import datetime

# Criando as tabelas do banco de dados
# Definimos o database.model para que o Python entenda que se trata de um modelo de Classe para tabela
class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    user_name = database.Column(database.String, nullable = False)
    email = database.Column(database.String, nullable = False, unique = True)
    senha = database.Column(database.String, nullable = False)
    # O relationship pega informações de uma outra tabela 
    fotos = database.relationship("Foto", backref = "usuario", lazy = True)


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key = True) 
    imagem = database.Column(database.String, default = "default.png") 
    data = database.Column(database.DateTime, nullable = False, default = datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable = False)