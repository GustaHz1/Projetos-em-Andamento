from main import app
from flask import render_template
from flask import url_for 
from FakePintrest import app

# O arquivo views é utilizado para guardas as rotas, necessário importar as informações como APP do projeto Main

# São rotas que geram novas páginas
@app.route("/")
def homepage():
    # Utilizamos o render_template para retornar o arquivo HTML da pasta de Templates
    return render_template("homepage.html")

# Quando colocamos um indíce da rota entre <> estamos dizendo que ele é uma variável
@app.route("/perfil/<usuario>")
def perfil(usuario):
    # Estamos utilizando a variavel declarada na função e atribuindo valores a ela
    # Passamos usuario = usuario para que o valor mude de acordo com a entrada que a variavel receber
    return  render_template("perfil.html", usuario = usuario)       

    # Apenas para explicação, com isto ao entrar no site na rota de perfil, podemos entrar em qualquer usuario passando o nome na rota!