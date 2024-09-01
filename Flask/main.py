from flask import Flask

# O arquivo Main é onde criamos todas instâncias necessárias!

app = Flask(__name__)

# Importando todas as rotas/arquivos do projeto views
from views import *

# Colocamos o APP.RUN() dentro de IF para não ficar executando o APP sempre!
if __name__ == "__main__":
    app.run()