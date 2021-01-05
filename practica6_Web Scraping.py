import requests
from bs4 import BeautifulSoup

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def wiki_world():
    print("LINKS:")
    soup = get_soup("http://transparencia.uanl.mx/remuneraciones_mensuales/bxd.php")
    t =dict()
    tabla = soup.table.find_all('td')
    t = [{'tr':f"{table.find_all('td')}"}
           for tablas in tabla]
    print(f"{[td['td'] for td in t]}")

if __name__ == "Principal ":
    soup = get_soup("http://transparencia.uanl.mx/remuneraciones_mensuales/bxd.php")
    t = soup.find_all(id='p-namespaces')
    print(f"(t)")

    wiki_world()
