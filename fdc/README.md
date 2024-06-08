# AIM-65 Floppy Controller

Scott Baker, https://www.smbaker.com/

## Jumper Settings

These are the settings I used on the board:

* JP1: 2-3 (interrupt is IRQ)

* JP2: 1-2 (5.25" floppy)

* JP3: 2-3 (2-head drive)

* JP4: 1-2 (enables ROM)

* JP5: 2-3 (always ready)

* JP6: 1-2 (always enable precomp -- seems odd, but verified this is E1=A on the RM65 FDC schematic and set as shown)

* JP7: 1-2 (enable mini floppy)

* JP8: 1-2 (5.25" floppy)

* JP9: Unpopulated unless setting the trimmers

* JP10: positions 1, 3, 4, 6. (only positions 2 and 5 are unpopulated)

  * 1 MOTEA to HL signal (populate)

  * 2: MOTEA is DS4 (leave empty)

  * 3: DSB is DS2 (populate)

  * 4: DSA is DS1 (populate)

  * 5: MOTEB is DS3 (leave empty)

  * 6: MOTEA to HL signal (populate)
