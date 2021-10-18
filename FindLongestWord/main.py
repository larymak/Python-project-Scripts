import os.path


def find_longest_words(file_content):
    last_length = 0
    words = []
    # the first loop is on each line
    for line in file_content:
        # gradually searching longest words dividing each line in a list of words and looping on the list
        for el in line.split():
            if len(el) > last_length:
                words = [el]
                last_length = len(el)
            elif len(el) == last_length:
                if el not in words:
                    words.append(el)
    return words, last_length


if __name__ == '__main__':
    input_file = input('please enter file name: ')
    file_to_open = os.path.join("files", input_file)
    try:
        fin = open(file_to_open, 'r')
        words, max_length = find_longest_words(fin)
        print('length of longest word(s): %d' % max_length)
        print('words: %s' % ', '.join(words))
    except FileNotFoundError:
        print("file not found.")
        quit()
