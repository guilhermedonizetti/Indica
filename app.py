from flask import Flask, render_template, request, redirect, url_for
from controller import loginController

app = Flask(__name__)

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
    login = loginController.Login.login_usuario(request.form.get('login'), request.form.get('senha'))
    if login:
        return redirect(url_for('login'))


# Inicia a aplicacao
if __name__ == '__main__':
    app.run()
