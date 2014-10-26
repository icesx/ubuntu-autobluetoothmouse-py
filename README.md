ubuntu-autobluetoothmouse-py
============================

python script to auto connect bluetooth mouse when pc booted on ubuntu14 tested.

how to use?

0、Manual connect your mouse with pc first

1、find your mouse addr as "00:1F:20:D4:D8:59" then edit bluetoothMouseAutoCon.py to change mouse_addr = "00:1F:20:D4:D8:59" as yourself.

2、install hidd use the command #sudo apt-get install bluez-compat.if your mouse is not 

3、edit your /etc/rc.local,add bluetoothMouseAutoCon.py 's full path,donot forgot to add the "&" on end

4、edit your ～.profile, add bluetoothXset 's full path,donot forgot to add the "&" on end

5、reboot your pc then all is ok.if no ,please check your mouse and press the connect button.

script note:

1、bluetoothMouseAutoCon.py 

   start pc to connect mouse
   
2、bluetoothXset.py
 
   set the mouse speed when mouse connected
