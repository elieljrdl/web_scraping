import requests
from bs4 import BeautifulSoup


url = "https://vagasbauru.com.br/vagas/?&meta=cidade:Bauru"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

div = soup.find_all("div", class_="e-con-inner")
print (div)
for item in div:
    # Titulo
    titulo = item.find("h3", class_="elementor-heading-title elementor-size-default")
    titulo_txt = titulo.get_text(strip=True) if titulo else "N/A"
    
    # falta terminar