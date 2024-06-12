# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Hello world")
# Set geometry (widthxheight)
root.geometry('350x200')
 
# all widgets will be here
# Execute Tkinter
root.mainloop()


# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Hello world")
# Set geometry(widthxheight)
root.geometry('350x200')
 
#adding a label to the root window
lbl = Label(root, text = "how are you?")
lbl.grid() 
 
# Execute Tkinter
root.mainloop()


# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Hello world")
# Set geometry(widthxheight)
root.geometry('350x200')
 
# adding a label to the root window
lbl = Label(root, text = "How are you?")
lbl.grid()
 
# function to display text when
# button is clicked
def clicked():
    lbl.configure(text = "clicked")
 
# button widget with red color text
# inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)
 
# Execute Tkinter
root.mainloop()


