import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

bairro = "jardim-italia"
quartos = "2"
arquivo = "dados.json"

url = f"https://www.nostracasa.com.br/imovel/alugar/chapeco/{bairro}/{quartos}-quartos?"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

itens = soup.find_all("div", class_="text")

dados = []

def formated (preco_str):
    preco_str = preco_str.replace("R$ ", "")
    preco_str = preco_str.replace(".", "")
    preco_str = preco_str.replace(",", ".")
    return float(preco_str)

for item in itens:
    # Preço
    preco_div = item.find("div", class_="title title-3")
    texto = preco_div.get_text(strip=True) if preco_div else ""
    match = re.search(r'R\$ [\d\.,]+', texto)
    preco = match.group() if match else "N/A"
    preco = formated(preco)

    # Código
    cod_tag = item.find("span", class_="cod")
    cod = cod_tag.get_text(strip=True) if cod_tag else "N/A"

    # Link
    link_tag = item.find("a", class_="btns btn")
    link = link_tag['href'] if link_tag and link_tag.has_attr('href') else "N/A"

    dados.append({
        "Currency": "R$",
        "Preço": float(preco),
        "Código": cod,
        "Link": link
    })

# salva em um arquivo .json    
with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
    
#print(dados)

result = [item for item in dados if item["Preço"] > 2000]
