import os
n = raw_input("Do you want to install guest additions for VMWare or VirtualBox? \n Press 1 for VMWare, 2 for VirtualBox: ");
os.system('sudo apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y');
os.system('echo "Update part is done"');
if n==2:
        os.system('sudo apt-get install virtualbox-guest-x11 -y');
elif n==1:
        os.system('sudo apt-get install install open-vm-tools-desktop fuse -y');
