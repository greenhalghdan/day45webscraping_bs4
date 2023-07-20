
from bs4 import BeautifulSoup
import requests
# live site https://news.ycombinator.com/

response = requests.get("https://news.ycombinator.com/")

web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
span = soup.find_all(class_="titleline")
article_text = []
article_link = []
for article in span:
    article_text.append(article.find("a").getText())
    article_link.append(article.find("a").get("href"))
article_score = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]



print(article_text)
print(article_link)
print(article_score)
most_votes = article_score.index(max(article_score))
print(article_text[most_votes])
print(article_link[most_votes])
print(article_score[most_votes])
print



# local site


# BeautifulSoupwith open("website.html") as data:
#     contents = data.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title.string)
# # print(soup.prettify())
# print(soup.a)
# t = soup.findAll(name="a")
# print(t)
# l = soup.find(name="h1", id="name")
# print(l)
# HTMLclass = soup.find(name="h3", class_="heading")
# print(HTMLclass.getText())
# # for tag in t:
# #     #print(tag.getText())
# #     # print(tag.get("href"))
# #     print(tag)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)