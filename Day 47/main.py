from bs4 import BeautifulSoup
import requests

re = requests.get("https://www.amazon.com/Wantjoin-Pressure-Control-Commercial-pressure/dp/B0B24WQVVC/ref=sr_1_2_sspa?crid=19EFANZYGSOB5&currency=INR&keywords=beans+pressure+cooker&qid=1671264827&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyV0pVUU1JSU42U1RJJmVuY3J5cHRlZElkPUEwNzQ5MDA4MzlUUlREVU1UQkwxNCZlbmNyeXB0ZWRBZElkPUEwMjkwODUwMlRHVVVKQ1FLWlpHOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
be = BeautifulSoup(re.text, "html.parser")
x = be.find("span", class_="a-offscreen")
print(x)
