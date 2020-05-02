from tkinter import *

root = Tk()

####################################################################

# # radiobtn syntax
# # button = Radiobutton(master, text=”Name on Button”, variable = “shared variable”, value = “values of each button”, options = values, …)

# # shared variable = A Tkinter variable shared among all Radio buttons
# # value = each radiobutton should have different value otherwise more than 1 radiobutton will get selected.

# # creating set1 radio btn

# # we have to tell what kind of value will be accepted by radiobtn, such as interger, string, boolean,etc.
# # this group accepting integer value
# group1 = IntVar()

# radio1 = Radiobutton(root, text='1', variable=group1, value=1)
# radio2 = Radiobutton(root, text='2', variable=group1, value=2)
# radio3 = Radiobutton(root, text='3', variable=group1, value=3)
# # displaying radio buttons
# radio1.pack()
# radio2.pack()
# radio3.pack()

# # set2 of radio btn
# # group accepting string value
# group2 = StringVar()

# # preselecting particular button
# group2.set('hey')

# radio4 = Radiobutton(root, text='hello', variable=group2, value='hello').pack()
# radio5 = Radiobutton(root, text='hey', variable=group2, value='hey').pack()
# radio6 = Radiobutton(root, text='hi', variable=group2, value='hi').pack()


# # set1 is grouped is by shared varaiable "group1"
# # set2 is grouped is by shared varaiable "group2"
# # hence, grouping of varaiables is done by "shared varaiable"

##################################################################################

# # showing the value of radio button which was selected by user

# group1 = IntVar()
# group1.set(2)

# def radiobtnClicked(value):
#   myLabel = Label(root, text=value).pack()

# # to exract the value, we will create a function which will execute whenever btn is clicked and then extracting its value
# # set(): used to set the value
# # get(): used to extract the value

# radio1 = Radiobutton(root, text='1', variable=group1, value=1, command =  lambda: radiobtnClicked(group1.get()))
# radio2 = Radiobutton(root, text='2', variable=group1, value=2, command =  lambda: radiobtnClicked(group1.get()))
# radio3 = Radiobutton(root, text='3', variable=group1, value=3, command =  lambda: radiobtnClicked(group1.get()))
# # displaying radio buttons
# radio1.pack()
# radio2.pack()
# radio3.pack()

# # extacting the value of last clicked radio button
# btn = Button(root, text='click me', command=lambda:radiobtnClicked(group1.get())).pack()

###############################################################################

# group of radio buttons

# creating list of all radiobtns text and value

# TREES = [
#   # each radio button is within tupel
#   # (key, value)
#   ('Mango', 'mango'),
#   ('orange', 'orange'),
#   ('apple', 'apple')
# ]

# insted of list, we can use dictionary also
TREES = {
  'Mango': 'mango',
  'orange': 'orange',
  'apple': 'apple'
}

trees = StringVar()
trees.set('apple')

# for tupel btns
# for text, value in TREES:
#   # anchor: it will align all the radio buttons from west side ir left align 
#   Radiobutton(root, text=text, variable=trees, value=value).pack(anchor=W)

# for dictionary
for text, value in TREES.items():
  # anchor: it will align all the radio buttons from west side ir left align 
  Radiobutton(root, text=text, variable=trees, value=value).pack(anchor=W)


def printValue(value):
  print(value)
  mylabel = Label(root, text=value).pack()

myBtn = Button(text="get the value", command=lambda: printValue(trees.get())).pack()


root.mainloop()