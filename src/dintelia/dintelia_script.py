import requests
from bs4 import BeautifulSoup

url = 'https://dentalia.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")