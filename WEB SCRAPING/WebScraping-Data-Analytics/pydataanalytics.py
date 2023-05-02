import requests 
from bs4 import BeautifulSoup
url =  'https://www.totaljobs.com/jobs/in-london'

r = requests.get(url)

#print(r)

html_soup= BeautifulSoup(r.content, 'html.parser')
#print(html_soup.prettify())






