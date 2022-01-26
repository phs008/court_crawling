from seleniumrequests import Chrome
from selenium import webdriver
from bs4 import BeautifulSoup
import re

sidoCode = {11: "서울특별시",
            26: "부산광역시",
            27: "대구광역시",
            28: "인천광역시",
            29: "광주광역시",
            30: "대전광역시",
            31: "울산광역시",
            36: "세종특별자치시",
            41: "경기도",
            42: "강원도",
            43: "충청북도",
            44: "충청남도",
            45: "전라북도",
            46: "전라남도",
            47: "경상북도",
            48: "경상남도",
            50: "제주특별자치도"}
sidoCode = list(sidoCode.keys())


def CreateSession():
    option = webdriver.ChromeOptions()
    option.add_argument("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; ko; rv:1.9.0.14) Gecko/2009082706 Firefox/3.0.14")
    chrome = Chrome('/home/phs/chromedriver_linux64/chromedriver', chrome_options=option)
    return chrome


def POSTRequestAPI(session, url, args):
    response = session.request('POST', url, data=args)
    return response


s = CreateSession()
url = 'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf'

form_params = {
    "_FORM_YN": "Y",
    "srnID": "PN0102000",
    "daypyoSidoCd": sidoCode[0]
}
r1 = POSTRequestAPI(s, url, form_params)
html = r1.content
soup = BeautifulSoup(html, 'html.parser')
mulgun_table = soup.select_one('table.Ltbl_list').select_one('tbody')
column = mulgun_table.select('tr')
for col in column:
    sagun_num = col.select('td')[1].text
    sagun_num = re.split(r'[\r\n\t]+', sagun_num)
    sagun_num = [num for num in sagun_num if len(num) > 0]
    sagun_court = sagun_num[0]
    sagun_num = sagun_num[1]

    sagun_purpose = col.select('td')[2]
    sagun_address = col.select('td')[3]
    sagun_remark = col.select('td')[4]
    sagun_value = col.select('td')[5]

s.close()
