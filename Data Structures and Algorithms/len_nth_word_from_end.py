# checks the length of the nth word from the end
def len_nth_word_from_end_1(str, num):
  plc = -1

  while num != 0 and plc >= -1 * len(str):
    # accounts for the case of no space at the end of the string after the last word
    if str[plc] != ' ':
      while plc >= -1 * len(str) and str[plc] != ' ':
        plc -= 1
      else:
        start = plc +1
    # accounts for the case of at least one space at the end of the string after the last word
    else:
      while plc >= -1 * len(str) and str[plc] == ' ':
        plc -= 1
      else:
        end = plc
      while plc >= -1 * len(str) and str[plc] != ' ':
        plc -= 1
      else:
        start = plc +1
    plc = start - 1
    num -= 1
    
  else:
    if num != 0:
      return -1
    return len(str[start: end + 1])

# checks the length of the nth word from the end using split
def len_nth_word_from_end_2(str, num):
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

print(len_nth_word_from_end_1(s, 5))
print(len_nth_word_from_end_2(s, 3))
