import requests
from bs4 import BeautifulSoup
import json

arquivo = "jogos_corinthians.json"
url = "https://www.espn.com.br/futebol/time/calendario/_/id/874/corinthians"

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36" }

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
jogos = soup.find_all("tr", class_= "Table__TR Table__TR--sm Table__even")

lista_jogos = []

for jogo in jogos:
    
    colunas = jogo.find_all("td")
    #dados = [coluna.get_text(strip=True) for coluna in colunas]
    
    data = colunas[0].get_text(strip=True) if colunas else "N/A"
    time_casa = colunas[1].get_text(strip=True) if colunas else "N/A"
    time_visitante = colunas[3].get_text(strip=True) if colunas else "N/A"
    horario = colunas[4].get_text(strip=True) if colunas else "N/A"
    campeonato = colunas[5].get_text(strip=True) if colunas else "N/A"

    lista_jogos.append({
        "Data": data,
        "Time Casa": time_casa,
        "Time Visitante": time_visitante,
        "Horário": horario,
        "Campeonato": campeonato
    })
   

with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(lista_jogos, f, indent=4, ensure_ascii=False)
