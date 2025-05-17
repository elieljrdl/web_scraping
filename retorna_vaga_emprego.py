import requests
from bs4 import BeautifulSoup
import json
import re
from unidecode import unidecode

url = "https://vagasbauru.com.br/vagas/?&meta=cidade:Bauru"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


div = soup.find_all("div", class_="elementor-element elementor-element-493d089 e-flex e-con-boxed e-con e-child")
#print(div)
dados = []
arquivo = "vagas.json"

def formated (preco_str):
    preco_str = preco_str.replace("R$ ", "")
    preco_str = preco_str.replace(".", "")
    preco_str = preco_str.replace(",", ".")
    return float(preco_str)

def ajusta_link(nomevaga):
    nomevaga = unidecode(nomevaga)
    nomevaga = nomevaga.lower()
    nomevaga = re.sub(r'[ /]+', '-', nomevaga)
    return nomevaga

for item in div:
    
    vaga = item.find("h3", class_="elementor-heading-title elementor-size-default").get_text(strip=True) if item else "N/A"
    
    empresa = item.find("h2", class_="elementor-heading-title elementor-size-default").get_text(strip=True) if item else "N/A"
    
    cidade = item.find("div", class_="elementor-element elementor-element-66bbd480 elementor-icon-list--layout-inline elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list").get_text(strip=True) if item else "N/A"
    
    periodo = item.find("div", class_="elementor-element elementor-element-258e24 elementor-icon-list--layout-inline elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list").get_text(strip=True) if item else "N/A"
    
    if item.find("div", class_="elementor-element elementor-element-524d146 elementor-icon-list--layout-inline elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list"):
        salario = item.find("div", class_="elementor-element elementor-element-524d146 elementor-icon-list--layout-inline elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list").get_text(strip=True)
        salario = formated(salario)
        if salario == 0.00:
            salario = "N/A"
    else:
        salario = "N/A"
    
    link = f"https://vagasbauru.com.br/vaga/{ajusta_link(vaga)}/"    
    
    dados.append({
        "Vaga": vaga,
        "Empresa": empresa,
        "Cidade": cidade,
        "Período": periodo,
        "Salário": salario,
        "Link": link
    })

    
with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)