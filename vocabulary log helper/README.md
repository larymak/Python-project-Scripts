# Vocabulary Log Helper
### This project is used for searching synonyms and antonyms for many words as fast as it can.

## What is vocabulary log?
**vocabulary log** is a college assignment that require the student to search for the synonyms, antonyms of certain words and make a statement using that word, I am a first year college student and I had a hard time doing this assignment because the time it can take, so I decided to make a code that can help me with the assignment.

## How does the code work?
This code work as following :<br>
1. Ask the user to enter the words he want to look for.
2. request the pages from [Thesaurus website](https://www.thesaurus.com/).
3. scrape the pages and get the synonyms and antonyms for the word.
4. print out the found data as a **json** data.

## Features I want to add to this project:
- Output the data as an excel file 
- Add a GUI for better user experience 


## Files in project:
- `LogHelper.py`  : this file is an asynchronous version of the code, I made this version so I can  make the part of the code take less time.
- `LogHelperSync.py` : this is the original version of the code, it is synchronous and take much more time for much more words.

## Requirement to run this code:
- **aiohttp** module for asynchronous requests, to install run this command in the terminal

    ```bash
        pip install aiohttp
    ```
- **typing** defines a standard notation for Python function and variable type annotations. 

    ```bash
        pip install typing
    ```
- **Beautiful Soup** is a library that makes it easy to scrape information from web pages. 

    ```bash
        pip install BeautifulSoup
    ```
