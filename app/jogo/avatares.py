# import os

avatar = {
    "nome": "ana júlia",
    "arquivo": "ana-julia"
}

base_nome_de_arquivo = "avatar-"
pasta = "../assets/avatares"

def montar_nome_arquivo(avatar):
    arquivo = f"{base_nome_de_arquivo}{avatar["arquivo"]}.png"
    return f"{pasta}/{arquivo}"

print(montar_nome_arquivo(avatar))