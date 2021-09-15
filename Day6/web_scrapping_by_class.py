import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

soup = bs4.BeautifulSoup(result.text, 'lxml')

class_content = soup.select('.toctext')[0].getText()

print(class_content)