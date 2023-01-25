# checks the length of the nth word from the end using split
def len_nth_word_from_end(str, num):
  ls = str.split(" ")
  plc = -1
  word_num = 0
  while plc >= -1 * len(ls):
    # accounts for a variable number of whitespaces between words
    if ls[plc] != '':
      word_num += 1
    if word_num == num:
      return len(ls[plc])
    else:
      plc -= 1
  else:
    return -1

s = "fly  me  to    the moon "
print(len_nth_word_from_end(s, 3))
print(len_nth_word_from_end(s, 6))
