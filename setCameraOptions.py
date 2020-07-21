
from tkinter import *
#import tkinter as ttk
#from ttk import *
from picamera import PiCamera
camera = PiCamera()

win = Tk()
win.title("Set Camera Otions")

# Add a grid
#mainframe = Frame(win)
#mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
#mainframe.columnconfigure(0, weight = 1)
#mainframe.rowconfigure(0, weight = 1)
#mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
currentImageEffect = StringVar(win)

# Dictionary with options
imageEffectsDict = camera.IMAGE_EFFECTS.keys()
currentImageEffect.set(camera.image_effect) # set the default option

popupMenu = OptionMenu(win, currentImageEffect, *imageEffectsDict)
Label(win, text="Select an Image Effect").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( currentImageEffect.get() )
    camera.image_effect = currentImageEffect.get()
    print(camera.image_effect)

# link function to change dropdown
currentImageEffect.trace('w', change_dropdown)

win.mainloop()
