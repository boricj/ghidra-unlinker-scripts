TOOLCHAIN?=mipsel-unknown-linux-gnu
CFLAGS?=-Os -g -ffreestanding -fno-pic -fno-plt -mno-abicalls -mno-check-zero-division
LDFLAGS?=-static -nostdlib

.PHONY: all clean

all: linux/asciiTable.elf linux/helloWorld.elf testcases/testData.elf testcases/testFlow.elf testcases/testSmallData.elf

clean:
	rm -f */*.elf */*.o

linux/asciiTable.elf: linux/asciiTable.o linux/ctype.o
	$(TOOLCHAIN)-cc -o $@ $(LDFLAGS) $^

linux/helloWorld.elf: linux/helloWorld.o
	$(TOOLCHAIN)-cc -o $@ $(LDFLAGS) $^

testcases/testData.elf: testcases/__start.o testcases/testBss.o testcases/testData.o
	$(TOOLCHAIN)-cc -o $@ $(LDFLAGS) $^

testcases/testFlow.elf: testcases/__start.o testcases/testFlow.o
	$(TOOLCHAIN)-cc -o $@ $(LDFLAGS) $^

testcases/testSmallData.elf: testcases/__start.o testcases/testSbss.o testcases/testSdata.o
	$(TOOLCHAIN)-cc -o $@ $(LDFLAGS) $^

%.o: %.c
	$(TOOLCHAIN)-cc -c -o $@ $(CFLAGS) $<
