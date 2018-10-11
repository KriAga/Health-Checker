import requests ; from bs4 import BeautifulSoup

search_item = "dengue"
base = "http://www.google.de"
url = "http://www.google.de/search?q="+ search_item

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
# for item in soup.select(".r a"):
#     print(item.text)
# for next_page in soup.select(".fl"):
#     res = requests.get(base + next_page.get('href'))
#     soup = BeautifulSoup(res.text,"lxml")
#     for item in soup.select(".r a"):
#         print(item.text)

print(soup)

result = soup.find("article", class_="kno-himx")
print(result)