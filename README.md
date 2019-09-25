# ROP TOOLS
## PYTHON SCRIPT FILES TO PERFORM RETURN-ORIENTED PROGRAMMING (ROP) EXPLOITS ON VULNERABLE ELF FILES.

Usage: python RopCrasher.py bitterman mode

| LANGUAGE | FILENAME      | MD5 HASH                         | DESCRIPTION                                                            |
|--------  |---------      |---------                         | -----                                                                  |
| python   | RopCrasher.py | e5b3e514c168351e07cdee0d64333050 | Crash's running 64-bit ELF program to produce initial segfault offset. |

- [x] Recognised modes include: critical, debug, error, info, notset, warn and warning...
- [x] For further information see - http://docs.pwntools.com/en/stable

Return-Oriented Programming (ROP) - is an exploitation technique that bypasses DEP. It does that by chaining together legitimate code that's already in executable memory. This requires the attacker to either (a) have complete control of the stack, or (b) have control of rip/eip (the instruction pointer register) and the ability to change esp/rsp (the stack pointer) to point to another buffer.

### CONSOLE DISPLAY
![Screenshot](picture1.png)

## BITTERMAN EXPLOIT
Worked examples of the exploit using the vulnerable file - 'bitterman'.

| LANGUAGE | FILENAME      | MD5 HASH                         | DESCRIPTION     |
|--------  |---------      |---------                         | -----           |
| python   | bitterman1.py | 696abe10a83b8750df38297729387277 | Manual Exploit  |
| python   | bitterman2.py | ca992d4a6a6daf57cc6509c4b957228b | PWN Exploit     |
| elf      | bitterman     | 7bacffdf0ba71b1247f0b7359f253ecc | Vulnerable file |
| elf      | rlic.so.6     | e63efc14f34504f4ac4cf7d63ed229ca | Called Library  |




