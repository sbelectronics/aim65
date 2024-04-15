pgm = open("J903-001-Z15.bin","rb").read()

pgm = bytearray(pgm)

base = 0x9800

boffs=2

for line in open("reloc.txt").readlines():
  line = line.strip()
  if not line:
    continue
  if "2byte" in line:
    boffs=1
    continue
  if line.startswith(";"):
    continue
  addr = int(line,16)
  addr = addr - base
  print("%04X" % addr, line)
  v = pgm[addr+boffs]
  if (v<0xD0) or (v>0xDf):
    print("Not valid: %s" % line)
    exit(1)

  pgm[addr+boffs] = pgm[addr+boffs] - 0xD0 + 0x90

open("reloc9800.bin","wb").write(pgm)
