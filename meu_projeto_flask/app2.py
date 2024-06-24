from flask import Flask, render_template, request, redirect, url_for, 
from validate_docbr import CPF


cpf = CPF()

novo_cpf_um = cpf.generate() 
novo_cpf_dois = cpf.generate(True)

cpf.validate_list(["012.345.678-90", "012.345.678-91"])  


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("gerador_cpf.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/validar cpf")
def cpf():
    return render_template("validar_cpf.html")

@app.route("/cpf valido")
def validar_cpf():
    for  in validar_cpf:
        if 
