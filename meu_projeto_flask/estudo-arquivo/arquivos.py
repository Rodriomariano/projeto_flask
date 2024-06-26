# arquivos

# ler 
file = open("dados.txt")
print(file)
# print(file.read())
# conteudo = file.read()
# print(conteudo)
print(file.readlines())
file.close()


with open("dados.txt") as file:
    conteudo = file.read()
    print(conteudo)
    print(conteudo)
    
    print("hahahaha")

    with open("dados.txt", "r") as file:
        file.write("/nBANANA VERDE")

    with open("dados.txt", "a") as file:
        file.write("/nUVA VERDE")

# Lista_produtos => lista dict (nome,descricao,preco,imagem)
# ler produtos.csv ----> lista_produtos

# 1. abrir o arquivo produtos.csv
def obter_produtos():
    with open("produtos.csv", "r"):
        lista_produtos = []

        # 2. ler usando o readlines()
        linhas = file.readlines()

        # 3. Para cada linha criar um dict com chave-valor 
        for linha in linhas:
            nome, descricao, preco, imagem = linha.strip().split(",")
            # valores = linha.split(",")
            # nome = valores[0]
            # descricao = valores[1]
            # preco = valores[2]
            # imagem = valores[3] 

            produto = {
            "nome": nome,
            "descricao": descricao,
            "preco": preco,
            "imagem": imagem
        }


        # 4. Colocar esse novo dict em uma lista
        
            lista_produtos.append(produto)
        
        return lista_produtos
    

obter_produtos()

# adicionar novo produto no arquivo produtos.csv
# entrada? dict representa produto
# saída? sem saída

def adicionar_produto(produto):
    with open("produtos.csv", "a") as file:
        linha = f"/n{produto['nome']}, {produto['descricao']}, {produto['preco']}, {produto['imagem']}"
        file.write(linha)

p1 = {
    "nome": "Teclado mecânico",
    "descricao": "joga fora acorda o bairro todo",
    "preco": 250.00,
    "imagem": "teclado.jpg"
}

adicionar_produto(p1)


        