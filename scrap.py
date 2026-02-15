from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)

print()

authors = soup.find_all("small", class_="author")
for author in authors:
    print(author.text)

print()

tags = soup.find_all(soup.small)
for tag in tags:
    print(tag.text)
