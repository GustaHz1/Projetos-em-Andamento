from flask import render_template, url_for, redirect
from fakepintrest import app
from flask_login import login_required
from fakepintrest.forms import FormCriarConta, FormLogin

# Criando a rota do site, e permitindoos metodos como GET e POST
@app.route("/", methods = ["GET", "POST"])
def homepage():
    form_login = FormLogin()
    # Ao declarar form = nome da variavel, estamos delcarando o form para o html
    return render_template("homepage.html", form = form_login)

@app.route("/criarconta", methods = ["GET", "POST"])
def criarconta():
    form_criar_conta = FormCriarConta()
    return render_template("criarconta.html", form = form_criar_conta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
