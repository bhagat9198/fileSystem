# to disply GUI, importing 'tkinter'

# 1st method: by using this, there is no need write package name before writing down function name
from tkinter import * 

# 2nd method : by using this, we need to write package name before writing down function name
# import tkinter

# to create one main window
root = Tk();

# root = tkinter.Tk(); # if we are using second method to import tkinter.

# progarm will run, it will display gui once and close off. but we want gui to display as per the use wish. hence, putting the gui in infinite loop
root.mainloop()