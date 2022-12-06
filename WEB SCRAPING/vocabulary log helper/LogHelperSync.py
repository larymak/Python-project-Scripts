import time
import requests
from json import dumps
from typing import Dict
from random import choice
from bs4 import BeautifulSoup as Beau_Soup



def get_page(word: str) -> str:    
    # get the HTML code of the word page 
    word = word.strip()
    url_to_get = f"https://www.thesaurus.com/browse/{word}"
    response = requests.get(url=url_to_get)

    return response.text


def get_syn_ant(word: str) -> Dict[str, str]:
    page = get_page(word=word)
    soup =  Beau_Soup(page,'html.parser')
    synonyms_list = list()
    antonyms_list = list()
    
    # getting all the synonyms
    for a in soup.select('ul a.css-1kg1yv8'):
        synonyms_list.append(a.text)

    for a in soup.select('ul.css-1gyuw4i'):
        synonyms_list.append(a.text)

    for a in soup.select('ul.css-1n6g4vv'):
        synonyms_list.append(a.text)
    
    # getting all the antonyms
    for a in soup.select('ul a.css-15bafsg'):
        antonyms_list.append(a.text)

    # chosing random synonym and antonym then return with the word
    return {
        'word': word,
        'synonym' : choice(synonyms_list).strip() if synonyms_list else 'No synonym',
        'antonym': choice(antonyms_list).strip() if antonyms_list else 'No antonym'
    }




def get_syn_ant_for_words() :
    words_to_look_for =  input("Enter the words to look for : ").split()
    words_to_look_for = [word.strip() for word in words_to_look_for if word != '']

    result = [get_syn_ant(word) for word in words_to_look_for]
    return result


if '__main__' == __name__:
    begin_time  = time.time()
    
    syn_ant_for_words = get_syn_ant_for_words()
    for word_detail in syn_ant_for_words:
        print(dumps(word_detail, indent=4))
    
    print("--- %s seconds ---" % (time.time() - begin_time))