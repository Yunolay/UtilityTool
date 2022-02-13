#!/bin/bash
file $1 > file.txt
checksec.sh --file $1
ldd $1 > ldd.txt
objdump -d -M intel $1 > objdump.txt
readelf -a $1 > readelf.txt
rp --file $1 --unique --rop 5