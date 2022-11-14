from bs4 import BeautifulSoup
import requests

url = "https://www.allrecipes.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

list_urls = []
for i in soup.findAll("a"):
    link = str(i.get("href"))
    if "https://" in link:
        list_urls.append(link)
list_urls = list_urls[:100]

with open(r"urls.txt", "w") as file:
    for item in list_urls:
        file.write(item + "\n")
