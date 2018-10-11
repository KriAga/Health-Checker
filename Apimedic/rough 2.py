
import requests
from bs4 import BeautifulSoup

# Home Page
url = "https://api.data.gov.in/resource/98fa254e-c5f8-4910-a19b-4828939b477d?api-key=579b464db66ec23bdd000001d7895a1764a94e755888fe167900afe5&format=json&offset=0&limit=6500"
bookToScrape = requests.get(url)
html = BeautifulSoup(bookToScrape.content, 'html.parser')

print(html)