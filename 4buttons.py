from tkinter import * 

root = Tk();
  
############################################################################
# # creating buttons
# # bydefault buttons are in active state
# mybutton0 = Button(root, text="Click Me")
# # we can define the state of the button by 'state' argument
# mybutton1 = Button(root, text="Click Me", state=ACTIVE)
# mybutton2 = Button(root, text="Click Me", state=DISABLED)

# # pack will display buttons one below the othere at the center of the screen
# mybutton0.pack()
# mybutton1.pack()
# mybutton2.pack()

#################################################################################

# # indenting the button
# # padx: increases the button width
# # pady: increases the button height

# mybutton = Button(root, text='Click Me!', padx=50)
# mybutton.pack()

# mybutton1 = Button(root, text='Click Me!', pady=50).pack()
# mybutton2 = Button(root, text='Click Me!', padx=50, pady=20).pack()

# # fg : forground color
# # bg : background color 
# mybutton3 = Button(root, text="Click Me!", fg="red", bg="yellow").pack()
# # we can use colors in hexadeciaml form also
# mybutton3 = Button(root, text="Click Me!", fg="#ffffff", bg="#000000").pack()

##################################################################################

def onClick():
  mylabel = Label(root, text="button clicked  ")
  # mylabel.grid(row=1, column=1)
  mylabel.pack()

mybutton = Button(root, text="Click Me", command=onClick).pack()
# mybutton = Button(root, text="Click Me", command=onClick(10)).grid(row=0, column=0)


#################################################################################
root.mainloop()