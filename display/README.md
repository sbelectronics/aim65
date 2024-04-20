Display Board for Rockwell AIM-65
Scott Baker, https://www.smbaker.com/

This is a display board based on the RM65 display board.

Supports up to 512KB of onboard ROM, which will be addressed into
the 24KB address space starting at 0x9000. The 0xA000 range is left
empty for onboard peripherals. The four-position dipswitch controls
which 32KB segment of the 512KB ROM is mapped. It is recommended to
use 39SF040 or similar flash device.

Remove all ROMs from the motheboard. (Alternatively, edit the PLD
to set the BASEROM_EN to 0, and it will only fill 9000 to 9FFF)

Also fills all RAM from 1000 to 7FFF, bringing RAM up to a full
32KB. Leave the RAM chips on the motherboard. You can edit the PLD
to set PRAM_EN to 0 if you do not want the RAM.

The display adapter maps itself to 9000 to 9FFFF:

* 9000-97FF: Display RAM

* 9800-9801: CRTC IO

* 9880: Display refresh flag, for updating during refresh

* 9900 - 9FFF: Display adapter RAM.

Use the following to switch to video display:

```keyboard
*
9900
<enter>
G
<enter>
```
