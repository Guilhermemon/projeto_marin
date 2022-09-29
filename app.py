from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


app.config  ["title"] ='Projeto'

bootstrap=(app)

@app.route("/")
def Home ():
    itens = ['Amortecedor', 'vela' , 'biela', "cabeçote"]
    return render_template("home.html",itens = itens)


@app.route("/preço")
def preço ():
    itens =[{"Nome": "Amortecetor","preco":2000.15 },
             {"Nome": "vela","preco":750.99 },
            {"Nome": "biela","preco":800.55 },
            {"Nome": "cabeçote","preco":800.95 } ]     
    return render_template("preco.html",itens = itens)    

if __name__ == "__main__":

        app.run(Debug=True) 