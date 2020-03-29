from tkinter import * 

root = Tk()

# creating input box

# Entry : creates the text box
# root: 1st argument, tells in which widget to place the text box
e1 = Entry(root)
e1.pack()

# passing optional parameters

# width: increases width of textbox
# borderwidth : increases border width
e2 = Entry(root, width=50, fg="white", bg="black", borderwidth=10)
e2.pack()

def onClick():
  # grabbing the text from the input box : boxName.get()
  enteredText = e1.get()
  # concatenating 'hello' to inputed text
  enteredText = 'Hello ' + enteredText
  # putting the label as enteredText
  mylabel = Label(root, text=enteredText)
  mylabel.pack()

mybutton = Button(root, text="Click Me", command=onClick).pack()

root.mainloop()