#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                  PYTHON UTILITY SCRIPT FILE FOR ROP EXPLOITATION
#               BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load any required imports and initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
#import binascii
#import linecache
from pwn import *						# pip install pwn
from termcolor import colored					# pip install termcolor

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Conduct simple and routine tests on user supplied arguements.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if os.geteuid() != 0:
    print "\nPlease run this python script as root..."
    exit(True)

if len(sys.argv) < 2:
    print "\nUse the command: python RopCrasher.py rop_file mode..."
    exit(True)

ropFile = sys.argv[1]

if os.path.exists(ropFile) == 0:
    print "\nFile " + ropFile + " was not found, did you spell it correctly?.."
    exit(True)

if len(sys.argv) < 3:
    print "\nUse the command: python RopCrasher.py rop_file mode..."
    exit(True)

ropMode = sys.argv[2]

chkMode = False
sysMode = ["critical", "debug", "error", "info", "notset", "warn", "warning"]

for mode in sysMode:
   if mode == ropMode:
      chkMode = True

if chkMode == False:
   print "Error - Recognised modes include: critical, debug, error, info, notset, warn and warning..."
   exit (True)

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Create function calls for main.
# Modified: N/A                                                              
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# INFORMAT: Display my universal header.
# -------------------------------------------------------------------------------------

def header():
   os.system("clear")
   print " ____   ___  ____     ____ ____      _    ____  _   _ _____ ____   "
   print "|  _ \ / _ \|  _ \   / ___|  _ \    / \  / ___|| | | | ____|  _ \  "
   print "| |_) | | | | |_) | | |   | |_) |  / _ \ \___ \| |_| |  _| | |_) | "
   print "|  _ <| |_| |  __/  | |___|  _ <  / ___ \ ___) |  _  | |___|  _ <  "
   print "|_| \_|\___/|_|      \____|_| \_\/_/   \_\____/|_| |_|_____|_| \_\ "
   print "                                                                   "
   print "       BY TERENCE BROADBENT BSc CYBER SECURITY (FIRST CLASS)       "
   print "\nROP PROGRAM:",
   print colored (ropFile.upper(),'white')
   print "DEBUG MODE :",
   print colored(ropMode.upper() + "\n",'white')

# -------------------------------------------------------------------------------------
# INFORMAT: Print message to the screen in standard format.
# -------------------------------------------------------------------------------------

def message(message):
   print "[" + colored("-",'yellow') + "]",
   print colored(message,'white')

# -------------------------------------------------------------------------------------
# INFORMAT: Check if ELF or BINary file.
# -------------------------------------------------------------------------------------

def executable():
   debug("Finding executable")
   ropType = "NOT FOUND"
   with open("file.log") as search:
      for line in search:
         if "ELF" in line:
            ropType = "ELF"
   if ropType == "NOT FOUND":
      print "Error"
      exit(1)
   else:
      if ropMode == "info":
         print"\tFound: " + ropType
   return(ropType)

# -------------------------------------------------------------------------------------
# INFORMAT: Check architechure
# -------------------------------------------------------------------------------------

def architecture():
   debug("Finding architecture")
   ropArch = "NOT FOUND"
   with open("file.log") as search:
      for line in search:
         if "powerpc642" in line:
            ropArch = "powerpc642"
         if "arch64" in line:
            ropArch = "arch64"
         if "powerpc" in line:
            ropArch = "powerpc"
         if "sparc64" in line:
            ropArch = "sparc64"
         if "mips64" in line:
            ropArch = "mips64"
         if "msp430" in line:
            ropArch = "msp430"
         if "alpha" in line:
            ropArch = "alpha"
         if "x86-64" in line:					# Checked
            ropArch = "amd64" 
         if "thumb" in line:
            ropArch = "thumb"
         if "sparc" in line:
            ropArch = "sparc"
         if "s390" in line:
            ropArch = "s390"
         if "cris" in line:
            ropArch = "cris" 
         if "i386" in line:
            ropArch = "i386" 
         if "ia64" in line:
            ropArch = "ia64" 
         if "mips" in line:
            ropArch = "mips"
         if "m68k" in line:
            ropArch = "m68k"
         if "arm" in line:
            ropArch = "arm"
         if "vax" in line:
            ropArch = "vax"
         if "avr" in line:
            ropArch = "avr" 
   if ropArch == "NOT FOUND":
      print "Error"
      exit(1)
   else:
      if ropMode == "info":
         print"\tFound: ",
         print colored(ropArch,'yellow')
   return(ropArch)

# -------------------------------------------------------------------------------------
# INFORMAT: Check operating system.
# -------------------------------------------------------------------------------------

def OS():
   debug("Finding operating system")
   ropOSys = "NOT FOUND"
   with open("file.log") as search:
      for line in search:
         if "windows" in line:
            ropOSys = "windows"
         if "android" in line:
            ropOSys = "android"
         if "freebsd" in line:
            ropOSys = "freebsd"
         if "linux" in line:
            ropOSys = "linux"						# Checked
         if "cgc" in line:
            ropOSys = "cgc"
   if ropOSys == "NOT FOUND":
      print "Error"
      exit(1)
   else:
      if ropMode == "info":
         print"\tFound: ",
         print colored(ropOSys,'red')
   return(ropOSys)

# -------------------------------------------------------------------------------------
# INFORMAT: Check LSB or MSB.
# -------------------------------------------------------------------------------------

def indian():
   debug("Finding significant bit")
   ropEndi = "NOT FOUND"
   with open("file.log") as search:
      for line in search:
         if "LSB" in line:
            ropEndi = "little"						# Checked
         if "MSB" in line:
            ropEndi = "big"
   if ropEndi == "NOT FOUND":
      print "Error"
      exit(1)
   else:
       if ropMode == "info":
         print"\tFound: ",
         print colored(ropEndi,'green')
   return(ropEndi)

# -------------------------------------------------------------------------------------
# INFORMAT: Check 64 or 32-bit system.
# -------------------------------------------------------------------------------------

def bits():
   debug("Finding number of bits")
   ropBits = "NOT FOUND"
   with open("file.log") as search:
      for line in search:
         if "64-bit" in line:
            ropBits = "64"						# Checked
         if "32-bit" in line:
            ropBits = "32"
   if ropBits == "NOT FOUND":
      print "Error"
      exit(1)
   else:
      if ropMode == "info":
         print"\tFound: ",
         print colored(ropBits + "-bit",'red')
   return (ropBits)

# *************************************************************************************
# INFORMAT: Start of main program.
# *************************************************************************************

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Examine file structure
# Modified: N/A                                                              
# -------------------------------------------------------------------------------------

header()
message("Examining local program")
os.system ("file " + ropFile + " > file.log")
ropType = executable()
ropOSy  = OS()
ropArch = architecture()
ropEndi = indian()
ropBits = bits()
os.remove("file.log")
success("Successfully completed")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : set PAWLIB variables based on file examination.
# Modified: N/A                                                              
# -------------------------------------------------------------------------------------

message("Assigning found values to PWNLIB")
context.clear()
context(terminal=['tmux', 'new-window'])	# GDP in new window.
context.arch      = ropArch
context.os        = ropOSy
context.endian    = ropEndi
context.bits	  = ropBits
context.log_level = ropMode
#context.log_file  = 'log.txt'
success("Successfully completed")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Stage one - Determine the segmentation-fault offset.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

message("Checking canary and pie values")
info("If NIX is enabled then the stack is read-only and you need to use return to libc exploit.")
info("If CANARY is enabled the program checks to see if the stack has been smashed.")
info("If FORTIFY is enabled then the program checks for buffer overflow.")
info("If PIE is disabled the 'program' memory locations will stay the same.")
elf = ELF(ropFile)

message("Starting local program")
p = process(elf.path)

message("Crashing program")
crash = cyclic(1024)
p.sendline(crash)
p.wait()
success("Successfully completed")

message("Examining core dump file")
core = p.corefile
rsp = core.rsp
offset = core.read(rsp, 4)
offset = cyclic_find(offset)

message("Exploit found at " + str(offset) + " bytes")
info("Segmentation error found at {a} bytes".format(a=offset))
success("Successfully completed")

#Eof


