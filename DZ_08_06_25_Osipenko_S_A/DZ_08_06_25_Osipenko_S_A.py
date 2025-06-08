import requests
from bs4 import BeautifulSoup
import csv
import re


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    @staticmethod
    def refined(s):
        return re.sub(r"\D+", "", s)

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        cars = self.html.find_all("div", class_="css-1f68fiz ea1vuk60")
        for item in cars:
            title = item.find("h3").text
            description = item.find("span", class_="css-1l9tp44 e162wx9x0").text
            price = item.find("span", {"data-ftid": "bull_price"}).text
            ref = self.refined(price)

            self.res.append({
                "Название": title,
                "Описание": description,
                "Цена": ref
            })

    def save(self):
        with open(self.path, "w") as f:
            for item in self.res:
                f.write(f"Название: {item['Название']}\nОписание: {item['Описание']}\n"
                        f"Цена: {item['Цена']}\n\n{'*' * 50}\n")

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


def main():
    for i in range(1, 4):
        url = Parser(f"https://auto.drom.ru/all/page{i}/", "cars.csv")
        url.run()


if __name__ == '__main__':
    main()
