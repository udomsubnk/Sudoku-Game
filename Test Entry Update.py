from tkinter import *

def callback(sv):
    print (sv.get())

root=Tk()


sv = StringVar()
sv1 = StringVar()

sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
sv1.trace("w", lambda name, index, mode, sv1=sv1: callback(sv1))
Entry(root, textvariable=sv).grid(row=0, column=1)
Entry(root, textvariable=sv1).grid(row=1, column=1)

root.mainloop() 
