#!/bin/sh

if [ -z "$1" ];then
   echo "Usage: $0 [reboot|halt]"
   exit
fi
if [ "$1" = "reboot" ]; then
   zenity --question --ok-label "Reboot" --text "Reboot $HOST?" && sudo /sbin/reboot
elif [ "$1" = "halt" ] && zenity --question --ok-label "Shudown" --text "Shutdown $HOST?"; then
  sudo /sbin/halt -p
  /bin/date +"-- %a %d.%m.%Y %H:%M" >> /home/tant/Raphael/zeiten/login.time
fi       
