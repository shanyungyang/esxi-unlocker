macOS Unlocker V3.0.1 for VMware ESXi
=====================================

1. Introduction
---------------

Unlocker 3 for ESXi is designed for VMware ESXi 6.5, 6.7 and 7.0

The patch code carries out the following modifications dependent on the product
being patched:

* Fix vmware-vmx to allow macOS to boot
* Fix libvmkctl to allow vSphere to control the guest

The code is written in Python as it makes the Unlocker easier to run and
maintain on ESXi.

+-----------------------------------------------------------------------------+
| IMPORTANT:                                                                  |
| ==========                                                                  |
|                                                                             |
| Always uninstall the previous version of the Unlocker before using a new    |
| version. Failure to do this could render VMware unusable.                   |
|                                                                             |
+-----------------------------------------------------------------------------+

2. Installation
---------------
Copy the distribution file to the ESXi host datastore using scp or some other
data transfer system.

Decompress the file from the ESXi console or via SSH:

    tar xzvf esxi-unlocker-xxx.tgz

(xxx - will be the version number, for example, 300)

Run the command from the terminal:

    ./esxi-install.sh

Finally reboot the server.

3. Uninstallation
-----------------
Open the ESXi console or login via SSH and change to the folder where the files were extracted.

Run the command from the terminal:

    ./esxi-uninstall.sh

Finally reboot the server.

4. Notes
--------
A. There is a command added called esxi-smctest.sh which can show if the patch is successful. It must be run from a
terminal or SSH session. The output should be:

/bin/vmx
smcPresent = true
custom.vgz     false   32486592 B

Note: The uncompressed size reported for custom.vgz will vary depending on the ESXi version.

B. The unlocker can be temporarily disabled during boot by editing the boot options and adding "nounlocker".

5. Thanks
---------

Thanks to Zenith432 for originally building the C++ unlocker and Mac Son of Knife
(MSoK) for all the testing and support.

Thanks also to Sam B for finding the solution for ESXi 6 and helping me with
debugging expertise. Sam also wrote the code for patching ESXi ELF files and
modified the unlocker code to run on Python 3 in the ESXi 6.5 environment.

History
-------
26/09/18 3.0.0 - First release
01/05/20 3.0.1 - Fix for ESXi 7.0

(c) 2011-2018 Dave Parsons