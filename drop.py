from tkinter import *
 
def print_it(event):
    print (var.get())
 
root = Tk()
var = StringVar()
var.set("a")
OptionMenu(root, var, "a","b","c", command=print_it).pack()
root.mainloop()
