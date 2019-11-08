# Used to do basic testing of the camera module
# rapspistill -v -o test.jpg
# above used to do a prelim test that the camera module is working properly

# The goal is to take a picture every 100ms 

from time import sleep
from picamera import PiCamera

cam = PiCamera()
cam.start_preview()
sleep(3)
for filename in cam.capture_continuous('cont_capt_imgs/img{counter:03d}.jpg'):
    print('Image %s taken' % filename)
    sleep(0.1)

