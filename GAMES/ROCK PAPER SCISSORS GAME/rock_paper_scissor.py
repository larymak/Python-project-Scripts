#ROCK PAPER SCISSOR GAME
#PLAYER VS CPU
import random
a=0
b=0
print("WELCOME TO THE ROCK-PAPER-SCISSOR.........\nTHIS IS YOU VS PC THE 1ST ONE TO GET SCORE OF 5 WINS\nLETS START...")
while True:
   print("ENTER r-ROCK p-PAPER s-SCISSOR")
   a1=input()
   n=random.randrange(-10000,10000,1)
   if n%2==0 and n<=0:
       b1='r'
   if n%2!=0 and n<=0:
       b1='p'
   if n>=0 :
       b1='s'
   if a1=='r' and b1=='r' or a1=='p' and b1=='p'or a1=='s' and b1=='s':
       print("CURRENTLY A: ",a,"B: ",b)
       continue
   if a1=='r' and b1=='p':
       b=b+1
   if a1=='r' and b1=='s':
       a=a+1
   if a1 == 'p' and b1=='r':
       a=a+1
   if a1 == 'p' and b1 == 's':
       b = b + 1
   if a1 == 's' and b1 == 'r':
       b = b + 1
   if a1 == 's' and b1 == 'p':
       a = a + 1
   print("CURRENTLY \nA: ",a,"\nB: ",b)
   if a==5:
       print("A won")
       break
   if b==5:
       print("PC won")
