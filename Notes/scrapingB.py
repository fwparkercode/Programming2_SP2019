# Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"  # uniform resource locator

page = requests.get(url)
#print(page)
#print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify())

# find data in my soup object
# by tagname
title = soup.findAll("title")  # returns a list of all tags <title>
print(title)

# by attribute
fontsize = soup.findAll(style="font-size: 8px")
print(fontsize)
for fonts in fontsize:
    print(fonts.text)

# by css class
quotes = soup.findAll(class_="quote")
print(quotes)

for quote in quotes:
    print(quote.text)


# combine any of the above
quotes = soup.findAll("span", class_="text")

for quote in quotes:
    print(quote.text.strip())

# find all authors
authors = soup.findAll("small", class_="author", itemprop="author")

for author in authors:
    print(author.text)

print(len(quotes), len(authors))

for i in range(len(quotes)):
    print()
    print(quotes[i].text)
    print("\t-", authors[i].text)


# target this ---->  <a href="/author/Marilyn-Monroe">(about)</a>

links = soup.findAll("a")
print(links)