#!/bin/bash

#### Shoot and Upload Script ####
#The script will take a photo to the temp ramdrive, 
#upload it to the specified folder 
#and delete the temp file if the upload was successful.  
#If the upload failed, it will copy the photo to non-volatile storage 
#so that it can be manually downloaded.



DATE=$(date +"%Y-%m-%dT%H%M%S")
raspistill -o /tmp/$DATE.jpg
/home/pi/gdrive upload /tmp/$DATE.jpg -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk
if [ $? -eq 0 ]
then 
  rm /tmp/$DATE.jpg
else 
  mv /tmp/$DATE.jpg /home/pi/Pictures/$DATE.jpg
fi

/home/pi/gdrive upload -f /home/pi/image.jpg -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk

## Automate with crontab
#Use a time lapse calculator to determine the best shot interval 
#for your desired video keeping in mind that Pi photos are 2.5-3MB each.  
#I setup my Pi to shoot once a minute from 7:00am until 8:59pm everyday.  
#Crontab tools are available to help with the syntax.

## crontab -e
#* 7-20 * * * /home/pi/timelapse.sh >/dev/null 2>&1
#* 7-20 * * * /home/pi/Github/MyProject/RaspberryPi/RPi_Trials/BashShootandUploadScript_CA20170701.sh >/dev/null 2>&1



#### gdrive testing ####
#Test1
./gdrive upload -f hello.txt -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk
## does not work

#Test2
./gdrive upload hello.txt -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk
## does work. remove the -f





