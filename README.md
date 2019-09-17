# R2LIBCROP
## A PYTHON SCRIPT FILE TO PERFORM RETURN-ORIENTED PROGRAMMING (ROP) EXPLOITS AUTOMATICALLY.

Usage: python R2LibcRop.py rop_file mode


| LANGUAGE | FILENAME      | MD5 HASH                         | EXPLOIT METHOD |
|--------  |---------      |---------                         | -----          |
| python   | bitterman1.py | 406e943588a17a7fcdaf7b707f46d120 | Manual         |
| python   | bitterman2.py | 212bbe6a9e244580f65981221090dbcd | Semi Automatic |
| python   | R2libcRop.py  |                                  | Automatic      |
| elf      | bitterman     | 7bacffdf0ba71b1247f0b7359f253ecc |                 |
| elf      | rlic.so.6     | e63efc14f34504f4ac4cf7d63ed229ca |                |

- [x] For further information see - http://docs.pwntools.com/en/stable/
- [ ] R2LibcRop currently not installed - updating files.
- [ ] Example files only shown above.

Return-Oriented Programming (ROP) - is an exploitation technique that bypasses DEP. It does that by chaining together legitimate code that's already in executable memory. This requires the attacker to either a) have complete control of the stack, or b) have control of rip/eip (the instruction pointer register) and the ability to change esp/rsp (the stack pointer) to point to another buffer.

### CONSOLE DISPLAY
![Screenshot](picture1.png)

