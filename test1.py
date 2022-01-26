from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.courtauction.go.kr/RetrieveMainInfo.laf'
driver.get(url)
