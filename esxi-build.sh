#!/bin/sh
set -e
touch esxi-install.sh esxi-uninstall.sh bin bin/smctest.sh etc etc/rc.local.d etc/rc.local.d/unlocker.py 
tar czvf unlocker.tgz bin etc
tar czvf unlocker-esxi-300.tgz unlocker.tgz esxi-install.sh esxi-uninstall.sh
