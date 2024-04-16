# Offsets start at 0x8000
#
# 9000 - 4096
# 9800 = 6144
# B000 = 12288
# C000 = 16384
# D000 = 20480
# D800 = 22528
# E000 = 24576
# F000 = 28672
#
# This will build up multi.rom that contains a set of
# 32KB images, each of which contains a full working AIM-65
# with monitor and language.
#   0 - basic
#   1 - extended basic by GWK
#   2 - forth
#   3 - pl65
#   4 - diagnostics

build/multi.rom: build/basic.rom build/extbasic.rom build/forth.rom build/pl65.rom build/diags.rom
	dd if=build/basic.rom of=build/multi.rom
	dd if=build/extbasic.rom of=build/multi.rom oflag=append conv=notrunc	
	dd if=build/forth.rom of=build/multi.rom oflag=append conv=notrunc
	dd if=build/pl65.rom of=build/multi.rom oflag=append conv=notrunc 	 
	dd if=build/diags.rom of=build/multi.rom oflag=append conv=notrunc 
	cp build/multi.rom build/00-multi.rom

build/monitor.rom:
	mkdir -p build
	head -c 32768 /dev/zero | sed 's/\x00/\x33/g' > build/monitor.rom
	dd if=../roms/R3223-monitor-E.bin of=build/monitor.rom bs=1 seek=24576 count=4096 conv=notrunc
	dd if=../roms/R3222-monitor-F.bin of=build/monitor.rom bs=1 seek=28672 count=4096 conv=notrunc

build/monitor_display.rom: build/monitor.rom
	cp build/monitor.rom build/monitor_display.rom
	dd if=../display/reloc9800.bin of=build/monitor_display.rom bs=1 seek=6144 count=2048 conv=notrunc
	#dd if=../display/J903-001-Z15.bin of=build/monitor_display.rom bs=1 seek=22528 count=2048 conv=notrunc

build/basic.rom: build/monitor_display.rom
	cp build/monitor_display.rom build/basic.rom
	dd if=../roms/R3226-11-basic-B.bin of=build/basic.rom bs=1 seek=12288 count=4096 conv=notrunc
	dd if=../roms/R3225-11-basic-C.bin of=build/basic.rom bs=1 seek=16384 count=4096 conv=notrunc
	# Move basic program and variable start to after 0400 to make room for display vars
	python ./patch.py build/basic.rom cf71:11=00 cf73:02=04

build/extbasic.rom: build/monitor_display.rom
	cp build/monitor_display.rom build/extbasic.rom
	dd if=../roms/EXTENDED-BASIC-V2.3-Z26-B.bin of=build/extbasic.rom bs=1 seek=12288 count=4096 conv=notrunc
	dd if=../roms/EXTENDED-BASIC-V2.3-Z25-C.bin of=build/extbasic.rom bs=1 seek=16384 count=4096 conv=notrunc
	dd if=../roms/EXTENDED-BASIC-V2.3-Z24-D.bin of=build/extbasic.rom bs=1 seek=20480 count=4096 conv=notrunc

build/forth.rom: build/monitor_display.rom
	cp build/monitor_display.rom build/forth.rom
	dd if=../roms/4thz-26.bin of=build/forth.rom bs=1 seek=12288 count=4096 conv=notrunc
	dd if=../roms/4thz-25.bin of=build/forth.rom bs=1 seek=16384 count=4096 conv=notrunc
	# move TASK from 0300 to 0400 to make room for display vars
	python ./patch.py build/forth.rom wb00A:0300=0400 wB028:0300=0400 wC295:0300=0400 wb01C:030B=040B wb01A:0300=0400

build/pl65.rom: build/monitor_display.rom
	cp build/monitor_display.rom build/pl65.rom
	dd if=../roms/PL65@Z26-B.bin of=build/pl65.rom bs=1 seek=12288 count=4096 conv=notrunc
	dd if=../roms/PL65@Z25-C.bin of=build/pl65.rom bs=1 seek=16384 count=4096 conv=notrunc	

build/diags.rom:
	mkdir -p build
	head -c 32768 /dev/zero | sed 's/\x00/\x33/g' > build/monitor.rom
	dd if=../aim65_memtest/memtest.bin of=build/diags.rom bs=1 seek=28672 count=4096 conv=notrunc

clean:
	rm -f build/*.rom
