# Beautisoup and a lot about Web scrapping
# HTML parser
from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title, "\n")
print(soup.title.string, "\n")
print(soup.title.name, "\n")
print(soup.prettify())
print(soup.a)
