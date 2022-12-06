"""
Example input : https://github.com/Dhrumil-Zion/Python-project-Scripts
"""

import pyshorteners

link = input("\nEnter your link : ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("\nShorted link is : "+x)