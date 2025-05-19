import csv
import time
from collections import Counter

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://ru.wikipedia.org"
START_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"


def get_animals_by_letter():
    counts = Counter()
    next_page = START_URL
    while next_page:
        response = requests.get(next_page)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select(".mw-category-group ul li a")
        for item in items:
            text = item.text.strip()
            if text:
                first_letter = text[0].upper()
                counts[first_letter] += 1
        next_link = soup.find("a", string="Следующая страница")
        if next_link:
            next_page = BASE_URL + next_link["href"]
            time.sleep(1)
        else:
            next_page = None
    with open("beasts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter, count in sorted(counts.items()):
            writer.writerow([letter, count])


if __name__ == "main":
    get_animals_by_letter()
