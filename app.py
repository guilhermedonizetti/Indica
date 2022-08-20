from flask import Flask, render_template, request, redirect, url_for
from controller import loginController
from config.connection import Conexao as conexao

global app
app = Flask(__name__)

# Configura e inicia o BD
conn = conexao.iniciar_banco_dados(app)
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
    login = loginController.Login.login_usuario(request.form, conn)
    return render_template("login.html", existe = login)


# Inicia a aplicacao
if __name__ == '__main__':
    app.run()
