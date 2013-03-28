python-racadm
=============

Implementation of racadm in pure Python

The local racadm command line interface provides access to the iDRAC management features. racadm provides access to the same features as the iDRAC web interface however, racadm can be used in scripts to ease configuration of multiple servers and iDRACs, where the Web interface is more useful for interactive management.

Usage
=============


PXE boot a host

./racadm.py -H 10.0.0.100 -u admin -p password123 -c "config -g cfgServerInfo -o cfgServerFirstBootDevice pxe"
./racadm.py -H 10.0.0.100 -u admin -p password123 -c "config -g cfgServerInfo -o cfgServerBootOnce 1"
./racadm.py -H 10.0.0.100 -u admin -p password123 -c "serveraction powercycle"


License
=============

The current license for this version is the "MIT License" as described by the Open Source Initiative.

Copyright 2013 Seth Miller
	
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.