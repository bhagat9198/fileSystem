from tkinter import *

root = Tk()

# creating frame
# 'padx' 'pady' : will give the padding within the frame
myFrame = LabelFrame(root, text='Enter frame text', padx=10, pady=10)

# displaying frame
# 'padx' 'pady' : will give the padding outside of the frame
myFrame.pack(padx=100, pady=50)

# creating widgets inside of frame
mybutton = Button(myFrame, text='Click Me')
mybutton.pack()


# frame2
# we cant use 'pack' and 'grid' at the same time when two widgets are one inside another. but "LabelFrame" is the exception, hece no errors
myFrame = LabelFrame(root, text='Enter frame text2', padx=10, pady=30)
myFrame.pack(padx=100, pady=50)

mybutton = Button(myFrame, text='Click Me 2')
mybutton.grid(row=1, column=1)

# frame3
# ommiting the frame text
myFrame = LabelFrame(root, padx=20, pady=10)
myFrame.pack(padx=100, pady=50)

mybutton = Button(myFrame, text='Click Me 2')
mybutton.grid(row=1, column=1)

root.mainloop()