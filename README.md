ubuntu-autobluetoothmouse-py
============================

python script to auto connect bluetooth mouse when pc booted on ubuntu14 tested.

how to use?

0、Manual connect your mouse with pc first

1、install hidd use the command #sudo apt-get install bluez-compat.if your mouse is not 

2、edit your /etc/rc.local,add bluetoothMouseAutoCon.py 's full path

3、edit your ～.profile, add bluetoothXset 's full path

4、reboot your pc then all is ok.if no ,please check your mouse and press the connect button.

script note:
1、bluetoothMouseAutoCon.py

   start pc to search mouse
   
2、bluetoothXset.py

   set the mouse speed when mouse connected
