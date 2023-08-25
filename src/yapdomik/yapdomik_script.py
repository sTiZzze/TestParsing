import requests
from bs4 import BeautifulSoup

from src.yapdomik.addition.constants import DOMAINS


def retrieve_data(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.find("div", class_="site-header__wrapper").find("a", class_="site-logo").find("img").get("alt")

    city = soup.find("div", class_="site-header__right").find("a", class_="city-select__current link link--underline").text

    street = soup.find("div", class_="container container--shops addressList").find("ul", class_="mb-6 mt-6").find("span", class_="link link--black").text

    print(street)


for first_domain in DOMAINS:
    url = f'https://{first_domain}.yapdomik.ru/about'
    retrieve_data(url)
