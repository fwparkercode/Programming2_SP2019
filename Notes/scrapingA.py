# Web Scraping with Beautiful Soup
import time
import urllib.request

import certifi
from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com"

page = requests.get(url)  # get request to that url
print(page)
#print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
#print(soup.prettify())

# findAll function to grab a list
# search for tagnames, attributes(kwargs), css class, text strings

# By tagname
titles = soup.findAll(name="title")
print(titles)  # list
print(titles[0]) # just the tag
print(titles[0].text)  # text inside the tag

# By attribute
keywords = soup.findAll(itemprop="keywords")
for word in keywords:
    print(word)

print("\n" * 10)
# By css class
quotes = soup.findAll(class_="quote")

for quote in quotes:
    print(quote)

print("\n" * 10)
print(quotes[0].prettify())


# By combinations
quotes = soup.findAll("span", class_="text")

for quote in quotes:
    print(quote.text)

quote_list = [x.text for x in quotes]
print(quote_list)

# By text
einsteins = soup.findAll(text="Albert Einstein")
for e in einsteins:
    print(e)

# Find authors
authors = soup.findAll("small", class_="author")
print(authors[0].text)
author_list = [x.text.strip() for x in authors]

# print all my quotes
for i in range(len(quote_list)):
    print()
    print(quote_list[i])
    print("\t-", author_list[i])


# BELOW IS SOME CODE I WROTE FOR DYNAMIC WEBSITE SCRAPING
# I also added code to download pictures from instagram

#launch url
url = "https://www.instagram.com/instagram/"

from selenium import webdriver

# create a new chrome session
# need to have chromedriver executable in project for this
driver = webdriver.Chrome("data/chromedriver")
driver.implicitly_wait(15)  # wait 15 sec to load page
driver.get(url)


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")


x = 0

while x < 20:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    x += 1
    # Wait to load page
    time.sleep(1)  # seconds to let it load

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # reached the bottom
    last_height = new_height



# use lxml here, html.parser isn't lenient enough for this site
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify())


pics = soup.findAll("img", class_="FFVAD") # image tags
links = [x.get("src") for x in pics] # grab src attribute from img

# At first I got a certificate authentication error.
# I ran the following two files to install cert.
# this seems to be a python 3.6 or greater thing
# Install Certificates.command
# Update Shell Profile.command
# worked immediately for me after doing this


# code below grabs all the instagram pics from the page.
# if you add some code to scroll down, you could grab more.
for i in range(len(links)):
    urllib.request.urlretrieve(links[i], 'data/pics/' + str(i) + ".jpg")



