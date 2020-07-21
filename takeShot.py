from picamera import PiCamera
#from time import sleep
from tkinter import *
import datetime

# make unique file name for picture
## TODO clean up, get rid of colons etc

# print (photoName)

# make camera object
camera = PiCamera()
camera.resolution=(2028,1520)
# turn on preview
camera.start_preview(fullscreen=False, window = (50, 150,1024,576))
def takeSnap(*args):
    photoName = "/home/pi/Desktop/Photo_" + str(datetime.datetime.now()) + ".jpg"
    camera.capture(photoName)
    


win = Tk()
button = Button(win,text = "Snapperoux!", command = takeSnap).grid(row = 0, column = 0)
mainloop()
