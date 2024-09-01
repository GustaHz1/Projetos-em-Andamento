from main import app
from flask import render_template

# O arquivo views é utilizado para guardas as rotas, necessário importar as informações como APP do projeto Main

# São rotas que geram novas páginas
@app.route("/")
def homepage():
    # Utilizamos o render_template para retornar o arquivo HTML da pasta de Templates
    return render_template("homepage.html")
