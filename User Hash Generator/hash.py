from time import time
from random import randint

def user_hash_generator():
    n = 1
    while True:
        timestamp = int(time()*1000)
        hash_string = hex(hash((timestamp/(randint(1, 250)+n))
                          * (randint(1, 10)*5*n)))[2:14]
        n += 1
        yield hash_string

if __name__ == '__main__':
    print('Generator will create a random hash when you press only Enter.\
        \nTo exit, press any other button then Enter.')
    
    hasher = user_hash_generator()
    while True:
        ch = input()
        if ch == '':
            print(next(hasher))
        else:
            print('Terminated')
            break
