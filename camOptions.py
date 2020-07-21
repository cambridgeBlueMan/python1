from picamera import PiCamera
#from time import sleep
from tkinter import *

# make and name a window
win = Tk()
win.title("Set Camera Options")

# make a camera object
camera = PiCamera()

# list holding the current values for the various camera options
currentlySelectedOption = [camera.awb_mode, camera.drc_strength, camera.exposure_mode,
camera.flash_mode, camera.image_effect, camera.meter_mode]

# list holding labels for the OptionBoxes
optionBoxLabelValues = ["awb mode", "drc strength", "exposure mode", "flash mode", "image effect", "meter mode"]
# initialize lists to hold StringVars and OptionMenu objects
optionBoxLabels = []
stringVarsList = []
optionMenusList = []

# a list holding the different valid values for each of the camera options
optionsList = [camera.AWB_MODES, camera.DRC_STRENGTHS, camera.EXPOSURE_MODES,
camera.FLASH_MODES, camera.IMAGE_EFFECTS, camera.METER_MODES]

#so with each option
for i in range (len(optionsList)-1):
    optionBoxLabels.append(Label(win, text = optionBoxLabelValues[i]).grid(row = i, column = 0))
    stringVarsList.append(StringVar(win))
    stringVarsList[i].set(currentlySelectedOption[i])
    optionMenusList.append(OptionMenu(win, stringVarsList[i], *optionsList[i]))
    optionMenusList[i].grid (row = i, column = 1)
    print(i)
#
win.mainloop()
