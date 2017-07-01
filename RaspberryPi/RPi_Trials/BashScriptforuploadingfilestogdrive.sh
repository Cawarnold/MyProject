#### Bash Script for uploading files to gdrive ####

## Go to RPi
#to get gdrive for RPi 
wget https://docs.google.com/uc?id=0B3X9GlR6EmbnVXNLanp4ZFRRbzg&export=download

#copy the name of the downloaded file
ls

#change the name of the file to gdrive
mv uc?id=0B3X9GlR6EmbnVXNLanp4ZFRRbzg gdrive

#make executable
sudo chmod a+x gdrive

#to first connect to gdrive
./gdrive list

#get the id of the folder you want to upload to
./gdrive list

# copy the id
0B9eFHCUtjPEbWjFJdzNpRW10Tlk
