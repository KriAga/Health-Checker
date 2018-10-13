from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

DRIVER = '''chromedriver'''

medicalCondition = "Flu"
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(DRIVER)
driver.set_window_size(1366, 768)
driver.get('http://www.google.com')
search = driver.find_element_by_name('q')
search.send_keys(medicalCondition)
search.send_keys(Keys.RETURN)
try:
    driver.find_element_by_css_selector(".knowledge-health__tab-item.knowledge-health__tab-treatment").click()
    sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    treatmentTab = soup.find("div", {"class": "kno-himx"})
    treatmentTextDiv = treatmentTab.find_all("div", {"class": "mWyH1d"})
    treatmentData = {}
    for eachType in treatmentTextDiv:
        div = eachType.find("div")
        for j in div.find_all("div"):
            if j.find("span") is not None:
                key = j.text
            else:
                treatmentData[key] = j.text

    for key, value in treatmentData.items():
        print("----------")
        print(key)
        print(value)
except:
    print("No data found, I am sorry!")
