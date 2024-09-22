from fakepintrest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

# Carrega o usuário
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# Modelo de usuário
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    user_name = database.Column(database.String(150), nullable=False)
    email = database.Column(database.String(150), nullable=False, unique=True)
    senha = database.Column(database.String(150), nullable=False)
    fotos = database.relationship('Foto', backref='usuario', lazy=True)

# Modelo de foto
class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
