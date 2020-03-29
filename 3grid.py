from tkinter import * 

root = Tk();
  
mylabel1 = Label(root, text='Hello Alex')
mylabel2 = Label(root, text='Hello Bob')

# using pack to display labels : lables will be displayed one below the another at the center of the screen.
# mylabel1.pack()
# mylabel2.pack()

# but if we want to to place labels at some specific place, we use grid 
mylabel1.grid(row=0, column=1)
mylabel2.grid(row=5, column=450)

# note: although for mylabel2, column is 450. still it will be displayed at 2nd column. this because columns are relatives to each other. as there is nothing between 2-449 column, 450th column will act as 2nd column.

# python is object oriented, we can do something like this:
# thus, creating and displaying in one line
mylabel3 = Label(root, text='Hello Alex').grid(row=3, column=10)
mylabel4 = Label(root, text='Hello Bob').grid(row=4, column=50)


root.mainloop()