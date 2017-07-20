#!/bin/bash

#### Shoot and Upload Script ####
#The script will take a photo to the temp ramdrive, 
#upload it to the specified folder 
#and delete the temp file if the upload was successful.  
#If the upload failed, it will copy the photo to non-volatile storage 
#so that it can be manually downloaded.


start=$SECONDS

#### Original Pic Script ####
DATE=$(date +"%Y-%m-%dT%H%M%S")
raspistill -vf -hf -o /tmp/$DATE.jpg
/home/pi/gdrive upload /tmp/$DATE.jpg -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk
if [ $? -eq 0 ]
then 
  rm /tmp/$DATE.jpg
else 
  mv /tmp/$DATE.jpg /home/pi/Pictures/$DATE.jpg
fi

DATE=$(date +"%Y-%m-%dT%H%M%S")
raspistill -vf -hf -o /tmp/$DATE.jpg
/home/pi/gdrive upload /tmp/$DATE.jpg -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk
if [ $? -eq 0 ]
then 
  rm /tmp/$DATE.jpg
else 
  mv /tmp/$DATE.jpg /home/pi/Pictures/$DATE.jpg
fi

DATE=$(date +"%Y-%m-%dT%H%M%S")
raspistill -vf -hf -o /tmp/$DATE.jpg
/home/pi/gdrive upload /tmp/$DATE.jpg -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk
if [ $? -eq 0 ]
then 
  rm /tmp/$DATE.jpg
else 
  mv /tmp/$DATE.jpg /home/pi/Pictures/$DATE.jpg
fi

echo ----
duration=$(( SECONDS - start ))

echo Script took $duration seconds to run


# time lapse
#raspistill -t 30000 -tl 2000 -o image%04d.jpg
# very two seconds (2000ms), over a total period of 30 seconds (30000ms), 
# named image0001.jpg, image0002.jpg, and so on


#/home/pi/gdrive upload -f /home/pi/image.jpg -p 0B9eFHCUtj


#### Vid Script ####

#raspivid -t 5000 -vf -hf -o /tmp/VID_$DATE.h264
#MP4Box -add /tmp/VID_$DATE.h264 /tmp/VID_$DATE.mp4
#/home/pi/gdrive upload /tmp/VID_$DATE.mp4 -p 0B9eFHCUtjPEbWjFJdzNpRW10Tlk







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
#* 7-20 * * * /home/pi/Github/MyProject/RaspberryPi/MyJoy/scripts/PicNLoad_20170719.sh > /home/pi/Github/MyProject/RaspberryPi/MyJoy/scripts/PicNLoad_20170719.log 2>&1






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

#python documentation
#http://picamera.readthedocs.io/en/release-1.12/index.html

# to connect to gdrive
# http://kylehase.blogspot.co.uk/2015/10/simple-raspberry-pi-interval-camera.html
# http://olivermarshall.net/how-to-upload-a-file-to-google-drive-from-the-command-line/

# to create vid
# https://www.linux.com/learn/give-your-raspberry-pi-night-vision-pinoir-camera

# from h264 to mp4
# http://raspi.tv/2013/another-way-to-convert-raspberry-pi-camera-h264-output-to-mp4

# gdrive rpi download
# https://github.com/prasmussen/gdrive

# night vision with ir cut
# http://www.waveshare.com/wiki/RPi_IR-CUT_Camera

# trying to get night vision
# https://www.raspberrypi.org/forums/viewtopic.php?f=43&t=186006

# time lapse
# https://www.raspberrypi.org/documentation/usage/camera/raspicam/timelapse.md

