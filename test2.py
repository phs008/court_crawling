import requests

# location.SidoCd:
# - 11, 서울특별시
# - 26, 부산광역시
# - 27, 대구광역시
# - 28, 인천광역시
# - 29, 광주광역시
# - 30, 대전광역시
# - 31, 울산광역시
# - 36, 세종특별자치시
# - 41, 경기도
# - 42, 강원도
# - 43, 충청북도
# - 44, 충청남도
# - 45, 전라북도
# - 46, 전라남도
# - 47, 경상북도
# - 48, 경상남도
# - 50, 제주특별자치도


# header = {"Host": "www.courtauction.go.kr",
#           "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; ko; rv:1.9.0.14) Gecko/2009082706 Firefox/3.0.14",
#           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#           "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
#           "Accept-Charset": "windows-949,utf-8;q=0.7,*;q=0.7"
#           }
#
# get_aucsigu = 'https://www.courtauction.go.kr/RetrieveAucSigu.ajax'
# payload = {"sidoCode": 11, "id2": "idSiguCode", "id3": "idDongCode"}
# r = requests.post(get_aucsigu, headers=header, data=payload)


url = 'https://www.courtauction.go.kr/RetrieveRealEstMulDetailList.laf'
header = {"Host": "www.courtauction.go.kr",
          "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; ko; rv:1.9.0.14) Gecko/2009082706 Firefox/3.0.14",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
          "Accept-Charset": "windows-949,utf-8;q=0.7,*;q=0.7"
          }

jiwonNm1 = '전체'.encode('euc-kr')
form_params = {
    "_FORM_YN": "Y",
    "srnID": "PN0102000",
    "jiwonNm1": jiwonNm1
}

r = requests.post(url, data=form_params)
print(r)
