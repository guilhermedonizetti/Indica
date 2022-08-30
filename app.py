from flask import Flask, render_template, request, redirect, url_for
from config import autoload as classes

global app
app = Flask(__name__)

# Configura e inicia o BD
conn = classes.Conexao.iniciar_banco_dados(app)
print("\n\nCONEXAO: \n{}\n\n".format(conn))


# Retorna a pagina de erro
@app.errorhandler(Exception)
def error(e):
    return render_template("erro.html", e = e)

# Retorna a visualizacao da pagina inicial
@app.route("/", methods =['GET'])
def home():
    return render_template("index.html")


# Retorna a visualizacao da pagina de login
@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")


# Redireciona para o Controller de Login
@app.route("/login", methods=['POST'])
def login_usuario():
    login = classes.Login.login_usuario(request.form, conn)
    return render_template("login.html", existe = login)

# Retorna a pagina de criacao de conta (cadastro de usuario)
@app.route("/cadastro", methods=['GET'])
def cadastro():
    return render_template("cadastro.html")

# Redireciona para o Controller de Cadastro
@app.route("/cadastro", methods=['POST'])
def cadastrar():
    cadastro = classes.Usuario.registrar_novo_usuario(request.form, conn)
    print("Resposta: {}".format(cadastro))
    return render_template("cadastro.html")

# Inicia a aplicacao
if __name__ == '__main__':
    app.run()
