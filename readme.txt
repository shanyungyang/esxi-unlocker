macOS Unlocker V3.0 for VMware ESXi
===================================

1. Introduction
---------------

Unlocker 3 for ESXi is designed for VMware ESXi 6.5 and 6.7.

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
TO DO

3. Uninstallation
-----------------
TO DO

4. Thanks
---------

Thanks to Zenith432 for originally building the C++ unlocker and Mac Son of Knife
(MSoK) for all the testing and support.

Thanks also to Sam B for finding the solution for ESXi 6 and helping me with
debugging expertise. Sam also wrote the code for patching ESXi ELF files and
modified the unlocker code to run on Python 3 in the ESXi 6.5 environment.

The code is available at https://github.com/DrDonk/esxi-unlocker

History
-------
24/09/18 3.0.0 - First release


(c) 2011-2018 Dave Parsons