import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to extract the DOM from
url = 'https://www.facebook.com'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')


    title = soup.title
    if title:
        print("Page Title:", title.text)
    else:
        print("No title tag found.")


    links = soup.find_all('a')
    print("Links in the page:")
    for link in links:
        print(link.get('href'))

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
