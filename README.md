# PDF CRACKER
## A PYTHON SCRIPT FILE TO PERFORM RETURN-ORIENTED PROGRAMMING (ROP) EXPLOITS SEMI-AUTOMATICALLY.

Usage: python R2LibcRop.py rop_file mode


| LANGUAGE | FILENAME     | MD5 HASH                         | 
|--------  |---------     |---------                         | 
| python   | R2LibcRop.py | |
| bin      | bitterman    | | 

- [x] For further information see - http://docs.pwntools.com/en/stable/
- [ ] Currently working on fully automating the process, but this is proving difficult.

Return-Oriented Programming (ROP) - is an exploitation technique that bypasses DEP. It does that by chaining together legitimate code that's already in executable memory. This requires the attacker to either a) have complete control of the stack, or b) have control of rip/eip (the instruction pointer register) and the ability to change esp/rsp (the stack pointer) to point to another buffer.

### CONSOLE DISPLAY
![Screenshot](picture1.png)

