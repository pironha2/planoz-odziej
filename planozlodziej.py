# v klasa sala nauczyciel opisany w kns.txt
kns = "o24"

from bs4 import BeautifulSoup
import requests
import re

url = "https://zstrybnik.pl/html/plany/"+kns+".html"
req = requests.get(url)
zupka = BeautifulSoup(req.content, "html.parser")

dni = [" Poniedziałek", " Wtorek", " Środa", " Czwartek", " Piątek"]
wirsze = zupka.select("table tr")
plan = {d:[] for d in dni}

info = zupka.select_one("tr td[align=left]")

print()

if info:
    print(" ", info.get_text(strip=True))

for w in wirsze:
    godzinka = w.select_one("td.g")
    lekcje = w.select("td.l")
    if godzinka and lekcje:
        for i, l in enumerate(lekcje):
            if i >= len(dni):
                break
            text = l.get_text().replace("\xa0", "")
            plan[dni[i]].append((godzinka.get_text(), text))

for dzień, zajemcia in plan.items():
    print(f'\n {dzień}:')
    for godz, lekcja in zajemcia:
        if lekcja:
            lemkcja = re.sub(r'[(][^)]*[)]', '', lekcja)
            print(f' {godz} > {lemkcja}')