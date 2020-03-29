from tkinter import * 

root = Tk();

# to create anything on tkinter, its two step process
# 1. defining that widget
# 2. displaying on screen ir putting up on screen

# using labels
# defining label widget
# root: where label should be put   
mylabel = Label(root, text='Hello World')

# displaying the label widget into the window
# pack: puting on screen at first spot avilable
mylabel.pack()

# this now "hello world" will be displayed always in first row and in the center of window whenever we resize it.

root.mainloop()