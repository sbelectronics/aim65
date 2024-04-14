# Offsets start at 0x8000
#
# D800 = 22528

multi.rom:
	head -c 524576 /dev/zero | sed 's/\x00/\x33/g' > multi.rom
	dd if=../display/J903-001-Z15.bin of=multi.rom bs=1 seek=22528 count=2048 conv=notrunc

clean:
	rm -f multi.rom
