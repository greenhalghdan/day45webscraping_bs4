
from bs4 import BeautifulSoup

with open("website.html") as data:
    contents = data.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title.string)
# print(soup.prettify())
print(soup.a)
t = soup.findAll(name="a")
print(t)
l = soup.find(name="h1", id="name")
print(l)
HTMLclass = soup.find(name="h3", class_="heading")
print(HTMLclass.getText())
# for tag in t:
#     #print(tag.getText())
#     # print(tag.get("href"))
#     print(tag)