from bs4.element import ResultSet
import requests
import bs4
from requests.sessions import should_bypass_proxies

res = requests.get('https://quotes.toscrape.com/')

soup = bs4.BeautifulSoup(res.text, 'lxml')

#----------- first_page_authors --------- 
authors = soup.select('.author')
first_page_authors = set()
for i in authors:
    first_page_authors.add(i.text)
print(first_page_authors)

# ---------- first_page_quotes ----------

quotes = soup.select('.text')
first_page_quotes = set()
for i in quotes:
    first_page_quotes.add(i.text)
print(first_page_quotes)

#------------ top_ten_tags --------------

top_tags = soup.select('.tag-item')
top_ten_tags = set()
for i in top_tags:
    top_ten_tags.add(i.text.strip('\n'))
print(top_ten_tags)

#---------------- unique authors of all 10 pages ------------------- 

base_url = 'https://quotes.toscrape.com/page/{}/'

unique_authors =  set()
for i in range(1,11):
    result = requests.get(base_url.format(i))
    soup1 = bs4.BeautifulSoup(result.text, 'lxml')
    authors1 = soup1.select('.author')
    for i in authors1:
        unique_authors.add(i.text)
    
print(unique_authors)