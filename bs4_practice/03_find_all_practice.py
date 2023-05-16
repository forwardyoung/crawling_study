from bs4 import BeautifulSoup

f = open("02_ul_li.html", encoding="utf-8")


bsobj = BeautifulSoup(f.read(), "html.parser")
ul = bsobj.find("ul")
# lis = bsobj.find_all("li") # [<li>커피</li>, <li>우유</li>, <li>밀크티</li>, <li>커피</li>, <li>우유</li>, <li>밀크티</li>]
lis = ul.find_all("li") # [<li>커피</li>, <li>우유</li>, <li>밀크티</li>]

for li in lis:
    print(li.text)