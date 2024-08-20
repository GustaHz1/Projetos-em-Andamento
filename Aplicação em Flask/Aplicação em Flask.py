# Import da biblioteca flask e criando um servidor web a partir de Flask    
from flask import Flask

# Representa a aplicação web
app = Flask(__name__)

# Representa a págia padrão
@app.route("/")
# Após a execução da página a instrução a baixo é executada
def home():
    return "Hello, World!"

@app.route("/brazil")
def salvador():
    return "Hello, Brazil"

# Executa a instrução caso o nome seja __main__, o Python atribui o nome de __main__ ao executar o script    
if __name__ == "__main__":
    # Executa a aplicação 
    app.run(debug=True)