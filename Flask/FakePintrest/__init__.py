# __init__ é onde definimos nosso app 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
# Configurando nosso banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

# Conectando o SQLAlchemy ao Flask por meio do APP
database = SQLAlchemy(app)

# Importando todas as rotas/arquivos do projeto views
from FakePintrest import views 

# importamos o views abaixo para que primeiramente o views possa importar o app
