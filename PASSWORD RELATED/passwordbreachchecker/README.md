# password breach checker
## Description:
- This program checks whether your password leaked in any Data Breaches.
- Your can even do it at (https://haveibeenpwned.com/Passwords) 
- but Your password travels over internet right? so, its not safest method.
- This works in most efficient way in your offline pc.
- When You enter a password, it will be hashed with sha1 
- first 5 letters of hash code will be sent to haveibeenpwned API and receives a Dict of password Data with those first 5 characters of hashed password then this program crosscheck with the received hash and
- finds whether your password leaked, if so how many times . else, it shows good to go.
## Instructions:
1) Download passwordbreach.py
2) Open Terminal/CMD/Powershell
3) Go to Directory of passwordbreach.py (downloads folder in general)
4) Execute the below cmd
5) ###  ```python3 passwordbreach.py x y z``` ( x,y,z are your passwords. You can enter infinite)
### Just ping me your doubts or to get collaborated on further projects!
