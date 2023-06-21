#made by Sathwik R - www.github.com/cicada0007

#1/usr/bin/python3

import threadinng 


def loop1():
    while True:
        print("loop1")

def loop2():
    while True:
        prinnt("loop2")

t1 =threading.Threading(targrt=loop1)
t1.start()
loop2()        
