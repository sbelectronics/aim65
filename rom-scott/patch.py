# Quick and dirty patch tool for patching bytes and words in
# the ROMs

import sys

data = open(sys.argv[1],"rb").read()

data = bytearray(data)

for arg in sys.argv[2:]:
   if arg.startswith("w") or arg.startswith("W"):
      word = 1
      arg = arg[1:]
   else:
      word = 0
   (addr,x) = arg.split(":")
   (origv,newv) = x.split("=")
   addr = int(addr,16) - 0x8000
   origv = int(origv,16)
   newv = int(newv,16)

#   print("%4x" % addr, "%2x" % data[addr], "%2x" % data[addr+1])

   orig_lo = origv & 0xFF
   new_lo = newv & 0xFF
   if data[addr]!=orig_lo:
      print("mismatch at ",arg)
      sys.exit(-1)
   data[addr] = new_lo

   if word:
     orig_hi = origv >> 8
     new_hi = newv >> 8
     if data[addr+1] != orig_hi:
        print("mismatch at ",arg)
        sys.exit(-1)
     data[addr+1] = new_hi

open(sys.argv[1],"wb").write(data)
