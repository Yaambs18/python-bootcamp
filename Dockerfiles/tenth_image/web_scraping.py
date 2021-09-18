import requests
import bs4

result = requests.get('http://example.com')

# print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)

title = soup.select('p')[0].getText()
print(title)