from bs4 import BeautifulSoup

bsobj = BeautifulSoup("<html><body><h1>안녕하세요</h1></body></html>", "html.parser")
print(bsobj)

h1 = bsobj.find("h1") # h1 태그를 찾아라
print(h1)
print(h1.text) # h1 태그에서 글자만 추출