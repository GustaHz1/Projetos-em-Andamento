from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepintrest.models import Usuario

# Classes de criação de formulário, os validators são validações para os campos, cada campo tem seu tipo[String, Password,Submit]
class FormLogin(FlaskForm):
    email = StringField("E-mail!", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    button = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmar_senha = PasswordField("Confirmar senha", validators=[DataRequired(), EqualTo("senha")])
    button = SubmitField("Criar conta")
    
    # Função para validar se o email já foi cadastrado, o emai dentro da def é do forms
    def validate_email(self, email):
        # Importamos a classe Usuario do arquivo models e fazemos um comparativo filtrando apenas o email de Usuario pelo email de FormCriarConta
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            return ValidationError("E-mail já cadastrado, faça login para continuar")