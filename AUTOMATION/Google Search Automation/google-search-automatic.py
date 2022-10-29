"""
This script can automatically perform the google search process and open the website in default web browser.
"""

from googlesearch import search
from webbrowser import open


def google_search(query, no_of_results):

    result = search(query, num=no_of_results, pause=2, stop=no_of_results)

    return result


if __name__ == "__main__":

    query = input("Enter the Query: ")
    no_of_results = int(input("Enter number of tabs open in browser: "))
    for i in google_search(query, no_of_results):
        open(i)
