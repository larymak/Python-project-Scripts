import time
import aiohttp
import asyncio
from json import dumps
from random import choice
from bs4 import BeautifulSoup as Beau_Soup

def get_syn_ant(word: str, page: str):
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

async def get_page(session, word: str):
    # get the HTML code of the word page 
    url_to_get = f"https://www.thesaurus.com/browse/{word}"
    async with session.get(url_to_get) as response:
        result_data = await response.text()

    return get_syn_ant(word, result_data)


async def get_all_pages() :
    words_to_look_for =  input("Enter the words to look for : ").split()
    words_to_look_for = [word.strip() for word in words_to_look_for if word != '']

    tasks = list()
    async with aiohttp.ClientSession() as session:
        for word in words_to_look_for:
            task = asyncio.ensure_future(get_page(session, word))
            tasks.append(task)

        return await asyncio.gather(*tasks)

    

if '__main__' == __name__:
    begin_time  = time.time()
    
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    syn_ant_for_words = asyncio.run(get_all_pages())
    for word_detail in syn_ant_for_words:
        print(dumps(word_detail, indent=4))
    
    print("--- %s seconds ---" % (time.time() - begin_time))

