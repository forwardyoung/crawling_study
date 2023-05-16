import requests
from bs4 import BeautifulSoup

def crawl(code):
    url = f"https://finance.naver.com/item/main.naver?code={code}" # code는 회사마다 다르므로 변수로 쓴다
    res = requests.get(url) # print(res.text)
    bsobj = BeautifulSoup(res.text, "html.parser")

    div_today = bsobj.find("div", {"class":"today"})
    em = div_today.find("em")
    price = em.find("span", {"class":"blind"}).text

    h_company = bsobj.find("div", {"class":"h_company"})
    name = h_company.a.text # 종목명

    div_description = bsobj.find("div", {"class":"description"})
    code = div_description.span.text # 종목코드

    table_no_info = bsobj.find("table", {"class":"no_info"})
    tds = table_no_info.tr.find_all("td")
    volume = tds[2].find("span", {"class":"blind"}).text # 거래량

    dic = {"price":price, "name":name, "code":code, "volume":volume}
    return dic

dic = crawl("352820") # 하이브의 정보
print(dic)