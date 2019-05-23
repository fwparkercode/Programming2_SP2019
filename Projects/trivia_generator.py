

from bs4 import BeautifulSoup
import requests

url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=medium&type=multiple"

page = requests.get(url)
#print(page)
#print(page.text)

questions = str(page.text)

questions = questions[questions.find("[{"):-1]
print(questions)
questions = eval(questions)
print(type(questions))



