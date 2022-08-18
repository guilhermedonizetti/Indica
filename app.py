from flask import Flask, render_template

app = Flask(__name__)

# Retorna a pagina de erro
@app.errorhandler(Exception)
def error(e):
    return render_template("erro.html", e = e)

# Retorna a visualizacao da pagina inicial
@app.route("/")
def home():
    return render_template("index.html")


# Retorna a visualizacao da pagina de login
@app.route("/login")
def login():
    return render_template("login.html")


# Inicia a aplicacao
if __name__ == '__main__':
    app.run()
