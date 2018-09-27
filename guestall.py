import os
while True:

	n = raw_input("Do you want to install guest additions for VMWare or VirtualBox? Press 1 for VMWare, 2 for VirtualBox: ");

	

	if n=="1":
		os.system('sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y');

		os.system('echo "Update part is done"');

	        os.system('sudo apt-get install virtualbox-guest-x11 -y');
		break

	elif n=="2":
		os.system('sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y');

		os.system('echo "Update part is done"');

	        os.system('sudo apt-get install open-vm-tools-desktop fuse -y')
		break

	else:

	    	pass
