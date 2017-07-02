#!/bin/bash

#### Shoot and Upload Script ####
#The script will take a photo to the temp ramdrive, 
#upload it to the specified folder 
#and delete the temp file if the upload was successful.  
#If the upload failed, it will copy the photo to non-volatile storage 
#so that it can be manually downloaded.


#### Original Pic Script ####
DATE=$(date +"%Y-%m-%dT%H%M%S")
raspistill -vf -hf -o /tmp/$DATE.jpg
/home/pi/gdrive upload /tmp/$DATE.jpg -p 0B9eFHCUtj
if [ $? -eq 0 ]
then 
  rm /tmp/$DATE.jpg
else 
  mv /tmp/$DATE.jpg /home/pi/Pictures/$DATE.jpg
fi

#/home/pi/gdrive upload -f /home/pi/image.jpg -p 0B9eFHCUtj


#### Vid Script ####

raspivid -t 5000 -vf -hf -o /tmp/VID_$DATE.h264
MP4Box -add /tmp/VID_$DATE.h264 /tmp/VID_$DATE.mp4
/home/pi/gdrive upload /tmp/VID_$DATE.mp4 -p 0B9eFHCUtj






#### crontab ####
#Use a time lapse calculator to determine the best shot interval 
#for your desired video keeping in mind that Pi photos are 2.5-3MB each.  
#I setup my Pi to shoot once a minute from 7:00am until 8:59pm everyday.  
#Crontab tools are available to help with the syntax.

# to access crontab
# crontab -e 

## every minute between 7am and 8pm
#* 7-20 * * * /home/pi/timelapse.sh >/dev/null 2>&1
#* 7-20 * * * /home/pi/Github/MyProject/RaspberryPi/RPi_Trials/BashShootandUploadScript_CA20170701.sh >/dev/null 2>&1






#### gdrive testing ####
#Test1
#./gdrive upload -f hello.txt -p 0B9eFHCUtjP
## does not work

#Test2
#./gdrive upload hello.txt -p 0B9eFHCUtjP
## does work. remove the -f




#### Documentation ####
# to take pi 
# https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md

#  pi camera docs
# https://www.raspberrypi.org/documentation/raspbian/applications/camera.md

# to connect to gdrive
# http://kylehase.blogspot.co.uk/2015/10/simple-raspberry-pi-interval-camera.html

# to create vid
# https://www.linux.com/learn/give-your-raspberry-pi-night-vision-pinoir-camera

# from h264 to mp4
# http://raspi.tv/2013/another-way-to-convert-raspberry-pi-camera-h264-output-to-mp4

