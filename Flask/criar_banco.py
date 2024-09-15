from FakePintrest import database
from FakePintrest import app
# Importando as tabelas de models e criando elas no banco de dados
from FakePintrest.models import Usuario
from FakePintrest.models import Foto

# Para criar o banco de dados é necessário um contexto então chamamos o App e executamos o database
with app.app_context():
    database.create_all()