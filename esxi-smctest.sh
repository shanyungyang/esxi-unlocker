#!/bin/sh
grep -il \(c\)AppleComputerInc /bin/vmx*
vim-cmd hostsvc/hosthardware | grep smcPresent | cut -d ',' -f 1 | sed 's/^[ \t]*//'
esxcli system visorfs tardisk list | grep custom.vgz
