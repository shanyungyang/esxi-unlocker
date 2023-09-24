#!/usr/bin/env python
"""
The MIT License (MIT)

Copyright (c) 2014-2018 Dave Parsons & Sam Bingner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import datetime
import subprocess
import sys


if sys.version_info < (2, 7):
    sys.stderr.write('You need Python 2.7 or later\n')
    sys.exit(1)

# TODO: Change for a new release
VERSION = '3.0.2'
FILEVER = '302'
FILENAME = 'esxi-unlocker-302.tgz'

TIMESTAMP = '{:%Y%m%d%H%M.%S}'.format(datetime.datetime.now())
TOUCH = 'touch -t ' + TIMESTAMP
GTARUNLOCKER = 'gtar czvf unlocker.tgz etc'
GTARDISTRIB = 'gtar czvf ' + FILENAME + \
              ' unlocker.tgz esxi-install.sh esxi-uninstall.sh esxi-smctest.sh readme.txt'


def main():

    # Timestamp files for release
    print('\nTimestamping files...')
    subprocess.call(TOUCH + ' readme.txt', shell=True)
    subprocess.call(TOUCH + ' esxi-install.sh', shell=True)
    subprocess.call(TOUCH + ' esxi-uninstall.sh', shell=True)
    subprocess.call(TOUCH + ' esxi-smctest.sh', shell=True)
    subprocess.call(TOUCH + ' etc', shell=True)
    subprocess.call(TOUCH + ' etc/rc.local.d', shell=True)
    subprocess.call(TOUCH + ' etc/rc.local.d/unlocker.py', shell=True)

    # Build the gzipped tar file unlocker.tgz
    print('\nCreating unlocker.tgz...')
    subprocess.call(GTARUNLOCKER, shell=True)
    subprocess.call(TOUCH + ' unlocker.tgz', shell=True)

    # Build the distribution file esxi-unlocker-VER.tgz
    print('\nCreating ' + FILENAME + '...')
    subprocess.call(GTARDISTRIB, shell=True)
    subprocess.call(TOUCH + ' ' + FILENAME, shell=True)


if __name__ == '__main__':
    if sys.platform == 'darwin':
        print('ESXi-Build for macOS')
        main()
    else:
        print('ESXi-Build only supported on macOS')
