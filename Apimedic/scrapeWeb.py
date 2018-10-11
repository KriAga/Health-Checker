import requests
from bs4 import BeautifulSoup
from googlesearch import search
url = "https://www.google.co.in/search?q=Anorexia&oq=Anorexia&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8"
github = requests.get(url)
html = BeautifulSoup(github.content, 'html.parser')
print(html)


result = html.find("article", class_="kno-himx")
print(result)