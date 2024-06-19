from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    {"nome": "Coca-cola", "descricao": "veneno", "preco": "6.00" },
    {"nome": "Pepsi", "descricao": "ruim", "preco": "6.00"},
    {"nome": "Doritos", "descricao": "delicia", "preco": "12.00", "imagem": ""},
]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos = lista_produtos) 

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return f"{produto['nome']}, {produto['descricao']}"
        
    return "Produto não existe!"

#GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

#POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():  
    nome = request.form['nome']  
    descricao = request.form['descricao']
    produto = {"nome": nome, "descricao": descricao}
    preco = request.form['preco']
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))



app.run()
