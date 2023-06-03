from bs4 import BeautifulSoup
import requests

 
import webbrowser




booklinks = []
booktitles = []

def findfromgoldenaudiobooks(bookname):
    URL = "https://goldenaudiobooks.com/?s="
    r = requests.get(URL + bookname)
    soup = BeautifulSoup(r.content, 'html5lib')
    booklist = soup.findAll('h2', attrs = {'class':'entry-title'}) 

    for book in booklist:
        booklinks.append(book.a['href'])
        booktitles.append(book.a.text)

def findfromfindaudiobooks(bookname):
    URL = "https://findaudiobook.com/?s="
    r = requests.get(URL + bookname)
    soup = BeautifulSoup(r.content, 'html5lib')
    booklist = soup.findAll('h2', attrs = {'class':'entry-title post-title'}) 

    for book in booklist:
        booklinks.append(book.a['href'])
        booktitles.append(book.a.text)
    
def findfromfullengthaudiobooks(bookname):
    URL = "https://fulllengthaudiobooks.com/?s="
    r = requests.get(URL + bookname)
    soup = BeautifulSoup(r.content, 'html5lib')
    booklist = soup.findAll('h2', attrs = {'class':'entry-title post-title'}) 

    for book in booklist:
        booklinks.append(book.a['href'])
        booktitles.append(book.a.text)


def findfrom101audiobooks(bookname):
    URL = "https://101audiobooks.net/?s="
    r = requests.get(URL + bookname)
    soup = BeautifulSoup(r.content, 'html5lib')
    booklist = soup.findAll('h2', attrs = {'class':'entry-title'}) 

    for book in booklist:
        booklinks.append(book.a['href'])
        booktitles.append(book.a.text)

search = input("search for a book ")

findfromgoldenaudiobooks(search)
findfromfindaudiobooks(search)
findfromfullengthaudiobooks(search)
findfrom101audiobooks(search)

for x in range(1, len(booktitles) + 1):
    print(str(x) + ": " + booktitles[x-1])

booknum = int(input("select a book number "))
print("opening " + str(booklinks[booknum - 1]))
webbrowser.open(str(booklinks[booknum - 1]), new=2)

        