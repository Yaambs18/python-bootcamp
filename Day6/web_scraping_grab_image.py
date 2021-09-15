import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

soup = bs4.BeautifulSoup(result.text, 'lxml')

img = soup.select('img')[1]

img_link = requests.get("https:"+img['src'])

# print(img_link.content)

# downloading the image

f = open('python_logo.jpg', 'wb')
f.write(img_link.content)
f.close()