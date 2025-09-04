from bs4 import BeautifulSoup
import re
import requests

url = "https://zstrybnik.pl/html/lista.html"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

def extract_code(href):
    return re.search(r'/([a-z]\d+)\.html$', href).group(1)

with open('kns.txt', 'wt' ) as f:
    f.write("Oddziały:\n")
    for a in soup.select("h4:-soup-contains('Oddziały') + ul li a"):
        tekst = a.get_text(strip=True)
        href = a["href"]
        kod = extract_code(href)
        skrot = tekst.split()[0]
        f.write(f" {skrot} - {kod}\n")

    f.write("\nNauczyciele:\n")
    for a in soup.select("h4:-soup-contains('Nauczyciele') + ul li a"):
        tekst = a.get_text(strip=True)
        href = a["href"]
        kod = extract_code(href)
        f.write(f" {tekst} - {kod}\n")

    f.write("\nSale:\n")
    for a in soup.select("h4:-soup-contains('Sale') + ul li a"):
        tekst = a.get_text(strip=True)
        href = a["href"]
        kod = extract_code(href)
        f.write(f" {tekst} - {kod}\n")