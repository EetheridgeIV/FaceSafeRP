# FaceSafeRP

Utilizes RPi.GPIO Python3 Library found here: https://pypi.org/project/RPi.GPIO/

## send_photo.sh
send_photo.sh takes one argument, the path to the picture you want to send to the server.
`./send_photo.sh <IMAGE_PATH>`

You might need to convert the bash script into an executable on your own machine: `chmod u+x send_photo.sh`

## take_photo.sh
take_photo.sh takes 0 arguments. It is responsible for taking an image using the basic USB webcam connected to the Pi. It utilizes the fswebcam library in order to take a 1280x720 image. Here is the link for more information: https://www.raspberrypi.org/documentation/usage/webcams/

## VerifyIdentity.py
VerifyIdentity.py is the main driver code that runs on our Raspberry Pi 3A+. It is supported by two bash scripts, send_photo.sh and take_photo.sh.

To run: `python3 VerifyIdentity.py`

Press enter to take a photo or, comment line 25 and uncomment line 26 to send a default picture to the server. You must specify the path to the image in line 26 if you choose to do so.
