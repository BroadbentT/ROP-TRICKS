# R2LIBCROP
## AN EXPERIMENTAL PYTHON SCRIPT FILE TO PERFORM RETURN-ORIENTED PROGRAMMING (ROP) EXPLOITS ON VULNERABLE ELF FILES.

Usage: python R2LibcRop.py rop_file mode

| LANGUAGE | FILENAME      | MD5 HASH                         | EXPLOIT METHOD |
|--------  |---------      |---------                         | -----          |
| python   | bitterman1.py | 696abe10a83b8750df38297729387277 | Manual         |
| python   | bitterman2.py | ca992d4a6a6daf57cc6509c4b957228b | Semi Automatic |
| python   | R2libcRop.py  |                                  | Automatic      |
| elf      | bitterman     | 7bacffdf0ba71b1247f0b7359f253ecc |                |
| elf      | rlic.so.6     | e63efc14f34504f4ac4cf7d63ed229ca |                |

- [x] For further information see - http://docs.pwntools.com/en/stable
- [ ] R2LibcRop currently not shown - updating files.

Return-Oriented Programming (ROP) - is an exploitation technique that bypasses DEP. It does that by chaining together legitimate code that's already in executable memory. This requires the attacker to either (a) have complete control of the stack, or (b) have control of rip/eip (the instruction pointer register) and the ability to change esp/rsp (the stack pointer) to point to another buffer.

### CONSOLE DISPLAY
![Screenshot](picture1.png)

