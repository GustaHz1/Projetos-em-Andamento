# O arquivo main será onde executaremos o código
from FakePintrest import app

# Colocamos o APP.RUN() dentro de IF para não ficar executando o APP sempre!
if __name__ == "__main__":
    app.run()