# v klasa sala nauczyciel opisany w kns.txt
kns = "o24"
strona = "https://zstrybnik.pl/html/plany/o1.html"
#zastępuje domyślny plan na wpisany powyżej 

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
from termcolor import colored, cprint
    #import przydatnych bibliotek


url = re.sub("o1", kns, strona)
print(url)
req = requests.get(url)
zupka = BeautifulSoup(req.content, "html.parser")
datadzis = datetime.now().weekday()
    #bazowe zmienne

dni = [" Poniedziałek", " Wtorek", " Środa", " Czwartek", " Piątek"]
wirsze = zupka.select("table tr")
plan = {d:[] for d in dni}
    #ustawienie przydatnych zmiennych do wypisania planu

info = zupka.select_one("tr td[align=left]")
    #Wybiera fragment pliku html o oznaczeniu <tr> i potem <td>

print() #Wypisuje jednego entera dla lepszego wyglądu :)

if info:
    print(" ", info.get_text(strip=True)) 
    #Wypisuje z kiedy jest plan zdobyty chwilę temu 

for w in wirsze:
    godzinka = w.select_one("td.g")
    lekcje = w.select("td.l")
    if godzinka and lekcje:
        for i, l in enumerate(lekcje):              # i jest numerkiem wpisu w liście "l"
            if i >= len(dni):                       #<< zabezpieczenie przed opuszczeniem zakresu
                break
            text = l.get_text().replace("\xa0", "") # Usunięcie twardych spacji z html'a :)
            plan[dni[i]].append((godzinka.get_text(), text))
                                                    #Chyba wypisuje goziny do dnia czy cos
for dzienr, (dzień, zajemcia) in enumerate(plan.items()):
    if dzienr == datadzis:
        cprint(f'\n {dzień}:', 'red')
        for godz, lekcja in zajemcia:
            if lekcja:
                lemkcja = re.sub(r'[(][^)]*[)]', '', lekcja)
                cprint(f' {godz} > {lemkcja}', 'red')   #to od #45 jest kolorowe a za tym zwykłe białe
    else:
        print(f'\n {dzień}:')
        for godz, lekcja in zajemcia:
            if lekcja:
                lemkcja = re.sub(r'[(][^)]*[)]', '', lekcja)
                print(f' {godz} > {lemkcja}')    
