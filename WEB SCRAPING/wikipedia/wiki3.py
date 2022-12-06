import wikipedia
ny = wikipedia.page("New York")
print(ny.title)
print(ny.url)
print(ny.content)
print(ny.links[0])
# output : u'New York'
#          u'http://en.wikipedia.org/wiki/New_York'
#          u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
#          u'1790 United States Census'
