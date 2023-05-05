import sys
# from load import load_strings

# names = load_string[sys.argv[1]]

search_names = ["habib", "adam", "nasir", "jelilat"]


def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None


for n in search_names:
    index = index_of_item(search_names, n)
    print(index)
