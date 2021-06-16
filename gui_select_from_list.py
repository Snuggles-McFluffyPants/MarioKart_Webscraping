from tkinter import *

big_list = ['apples','pears','oranges','blueberries','grapes']
part_list = ['apples']

#Function that opens a gui where characters to evaluate are selected
def tkinter_stuff(title, big_list, part_list = []):
    # define gui window dimensions
    root=Tk()
    sizex = 600
    sizey = 400
    posx  = 40
    posy  = 20
    root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

    # Add in the title
    root.title(title)

    # Listbox attributes
    mylistbox=Listbox(root,width=60,height=10,font=('times',13))
    mylistbox.place(x=32, y=90)

    # Specify the original list of selected items
    output_list = []
    output_list = part_list + output_list
    for names in big_list:
        mylistbox.insert("end", names)
        mylistbox.itemconfig("end", bg = "blue" if names in output_list else "white")

    # Cause clicking on item to add item to output_list
    def CurSelet(event):
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])

        #Add clicked items to output_list
        if picked not in output_list:
            output_list.append(picked)
            position = big_list.index(picked)
            mylistbox.itemconfig(position, {'bg': 'blue'})

    mylistbox.bind('<<ListboxSelect>>',CurSelet)

    # Add a button labeled "Back that takes away last added item to
    # output_list out of output_list
    def callback():
        if len(output_list)>0:
            position = big_list.index(output_list[-1])
            mylistbox.itemconfig(position, {'bg': 'white'})
            output_list.remove(output_list[-1])
        else:
            pass

    b = Button(root, text="Back", command=callback)
    b.pack(side = BOTTOM)

    root.mainloop()
    return(output_list)


# # Open gui to select which character's value to analyze
# output_list = tkinter_stuff('characters to evaluate',big_list,part_list)
#
# print(output_list)