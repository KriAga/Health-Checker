from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def scrapeGoogle(disease):
    global key
    DRIVER = '''chromedriver'''  # name of the driver used (.exe file in this directory)

    medicalCondition = disease
    chrome_options = Options()
    chrome_options.add_argument("--headless")   #

    driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)
    driver.set_window_size(1366, 768)
    driver.get('http://www.google.com')
    search = driver.find_element_by_name('q')
    search.send_keys(medicalCondition)  # typing the medical condition into the search bar at google.com
    search.send_keys(Keys.RETURN)
    try:
        driver.find_element_by_css_selector(".knowledge-health__tab-item.knowledge-health__tab-treatment").click()  # selecting the treatment section of the
        sleep(1)    # waiting for the process to complete
        soup = BeautifulSoup(driver.page_source, "html.parser")
        treatmentTab = soup.find("div", {"class": "kno-himx"})
        treatmentTextDiv = treatmentTab.find_all("div", {"class": "mWyH1d"})
        treatmentData = {}  # dictionary to store a key-value pair for treatment

        for eachType in treatmentTextDiv:
            div = eachType.find("div")
            for j in div.find_all("div"):
                if j.find("span") is not None:
                    key = j.text
                else:
                    treatmentData[key] = j.text

        # In case typing error is there then we get the right word from the Google page itself to be stored correctly in the database
        disease = soup.find("div", {"class": "kno-ecr-pt"}).text
        return disease, treatmentData   # returning both the disease name as well as the treatments for that disease
    except:
        return {"No Data": "No Data"}   # just in case something goes wrong