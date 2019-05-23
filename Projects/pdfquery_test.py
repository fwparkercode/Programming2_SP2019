


from pathlib import Path
import requests


filename = Path('lunch.pdf')
my_url = 'https://www.fwparker.org/lunch'


response = requests.get(my_url)
print(response)