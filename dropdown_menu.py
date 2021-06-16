from tkinter import *

master = Tk()

sizex = 600
sizey = 400
posx = 40
posy = 20
master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

var = StringVar(master)
var.set("Drivers") # initial value

option = OptionMenu(master, var, 'Drivers', 'Karts', 'Gliders')
option.pack()


selection = ''

def ok():
    # print ("value is", var.get())
    global selection
    selection = var.get()
    # print(selection)
    return selection
    # master.quit()

button = Button(master, text="Commit", command=ok)
button.pack()

mainloop()

print(selection)


