from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/from?site=github.com/getlago")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
x = soup.find_all(name="a", class_="titleline")

article_text = []
article_link = []
for y in x:
    x_text = y.getText()
    article_text.append(x_text)
    x_link = y.get("href")
    article_link.append(x_link)

print(article_link)
print(article_text)
# upvotes = soup.find(name="span", class="score").get_text()























# with open("website.html") as file:
#     files = file.read()
#
# soup = BeautifulSoup(files, "html.parser")
# k = soup.find_all(name="a")
#
# print(k)
#
# for tag in k:
#     print(tag.getText())
#     print(tag.get("href"))

