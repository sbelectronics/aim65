resources:
  * http://cini.classiccmp.org//systems.htm

Bus
  * W = not-R/!W - appears to be an inverted R/!W
  * V = sys R/!W - not-R/!W inverted
  * Z = ram R/!W - not-sys-R/!W nand SYS_O2
  * U = SYS_O2 - not-O2 inverted
  * Y = not-O2 - the O2 from the CPU, inverted


Possible Basic set of start program
  cf70: a2 11     ldx #$11
  cf72: a0 02     ldy #$02
  cf74: 86 73     stx $73
  cf76: 84 74     sty $74

Possible Forth set of start program
  c28f: a0 0b     ldy #$0b
  c291: b9 31 ca  lda $ca31, y
  c294: 99 00 03  sta $0300, y
  c297: 88        dey
  c298: 10 f7     bpl $c291

  first is copies B00E/B00F to A4/A5
  then it overwrites B00A/B00B onto the address pointed by A4/A5
    copies a total of 12 bytes
 
  B00A - probably program start addr        (65/40 docs: looks incorrect)
  B01A - unknown, but likely                (65/40 docs: forget protection point)
  B01C - pointer to next free - confirmed   (65/40 docs: dictionary pointer)
  B028 - linkage from last word in the word list - confirmed   (65/40 docs: vocab pointer)
  C290 - probably not, but maybe
