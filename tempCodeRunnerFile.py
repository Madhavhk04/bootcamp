from tkinter import*
root=Tk()
root.title("WELCOME")
root.geometry('350x200')
labl=Label(root, text="Hello welcome to the website!")
labl.grid()
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