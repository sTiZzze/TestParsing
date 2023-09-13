import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from src.yapdomik.addition.constants import DOMAINS


def retrieve_data(url):
    response = requests.get(url)
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    driver.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    name = soup.find("div", class_="site-header__wrapper").find("a", class_="site-logo").find("img").get("alt")

    city = soup.find("div", class_="site-header__right").find("a", class_="city-select__current link link--underline").text
    print(name)
    print(city)
    li_elements = driver.find_elements(By.CSS_SELECTOR, "div.container.container--shops.addressList li")

    for li in li_elements:
        # Получаем атрибуты из JavaScript с использованием execute_script
        latitude = driver.execute_script("return arguments[0].getAttribute('data-latitude');", li)
        longitude = driver.execute_script("return arguments[0].getAttribute('data-longitude');", li)

        address = li.find_element(By.CSS_SELECTOR, "span.link.link--black").text
        print("Address:", address)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("\n")

    phones = soup.find('div', class_='contacts__phone').find_all('a')
    for phone in phones:
        print(phone.text)

    work_days = driver.find_element(By.ID, 'del_map').find_element(By.XPATH, "//div[@class='work-time']")
    print(work_days)

    for work_day in work_days:
        work_day = work_day.find_all("div")
        day = work_day[0].text
        time = work_day[1].text
        print(day)
        print(time)
    driver.quit()


for first_domain in DOMAINS:
    url = f'https://{first_domain}.yapdomik.ru/about'
    retrieve_data(url)
