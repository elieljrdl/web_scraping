import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO


url = "https://en.wikipedia.org/wiki/2025_Campeonato_Brasileiro_S%C3%A9rie_A"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
tabela = pd.read_html(response.text)
df = tabela[9]
print(df)
