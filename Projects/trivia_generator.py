import random
import sys
from html2text import html2text  # this library makes the text readable by removing stuff like &#039 which should just be '
import requests


category_list = []
url1 = 'https://opentdb.com/api.php?amount=5&category=10&type=multiple'
category_list.append(url1)

url = random.choice(category_list)


try:
    page = requests.get(url)
    data = page.text
    #print(data)  # look at the pulled data (it's a dict/list combo)

    data = data[data.find("[{"):-1]  # only grab the question list to simplify it  (if this doesn't work, just pull it from the dictionary)

    questions = eval(data)  # evaluate the string as python code
    print(questions)
    broken_link = False
except Exception as e:
    print("Error found:", e)
    sys.exit()



# get category (just grab ethe category of first question; all the same)
category = questions[0].get('category')
print(category)



question_list = [x.get('question').strip() for x in questions]
answers = [x.get('correct_answer').strip() for x in questions]
incorrect = [list(x.get('incorrect_answers')) for x in questions]

for i in range(len(question_list)):
    question_list[i] = html2text(question_list[i])


for i in range(len(question_list)):
    print(end="\n\n")
    print(category)
    print(question_list[i])
    print("Correct", answers[i])
    print("Incorrect", incorrect[i])





