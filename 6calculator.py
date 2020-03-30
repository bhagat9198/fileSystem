# ###############################################################################################
# simple add calculator

# from tkinter import *

# # global variables 
# firstNum = None

# root = Tk()

# root.title("Simple Calculator")

# #creating input field
# e = Entry(root, width=40)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=20)

# # button function
# def numButton(number):
#   # 'get' extracts what ever is there in input box
#   current = e.get()
#   e.delete(0, END)
#   # 'insert': inserts the text in input box
#   e.insert(0, str(current) + str(number))

# def clearButton():
#   # it will only delete charater at 0th index at a time
#   # e.delete(0)
#   # it will delete all the characters from 0th index till end
#   e.delete(0, END)

# def addButton():
#   # extracting the first number
#   fNum = e.get()
#   # making 'fNum' global so that it can be used in other then this function
#   global firstNum 
#   # the number extracted in string formate, convertig it into integer
#   firstNum = int(fNum)
#   e.delete(0, END)
  

# def equalBuuton():
#   secondNumber = e.get()
#   e.delete(0, END)
#   # total = firstNum + int(secondNumber)
#   e.insert(0, firstNum + int(secondNumber))

# # creating buttons
# # adding fonts to button
# # b1 = Button(root, text="1", font=('Arial Black', '10'), padx=15, command=lambda: numButton(1))

# # here 'pady' increases the button height
# # if we have to call a function with arguments when button is clicked, we will wrapp it in lambda exprestion so that fuction does not get called before button is actually clicked
# b1 = Button(root, text="1", padx=30, pady=15, command=lambda: numButton(1))
# b2 = Button(root, text="2", padx=30, pady=15, command=lambda: numButton(2))
# b3 = Button(root, text="3", padx=30, pady=15, command=lambda: numButton(3))
# b4 = Button(root, text="4", padx=30, pady=15, command=lambda: numButton(4))
# b5 = Button(root, text="5", padx=30, pady=15, command=lambda: numButton(5))
# b6 = Button(root, text="6", padx=30, pady=15, command=lambda: numButton(6))
# b7 = Button(root, text="7", padx=30, pady=15, command=lambda: numButton(7))
# b8 = Button(root, text="8", padx=30, pady=15, command=lambda: numButton(8))
# b9 = Button(root, text="9", padx=30, pady=15, command=lambda: numButton(9))
# b0 = Button(root, text="0", padx=30, pady=15, command=lambda: numButton(0))

# bequal = Button(root, text="=", padx=75, pady=15, command=equalBuuton)
# bclear = Button(root, text="x", padx=75, pady=15, command=clearButton)
# badd = Button(root, text="+", padx=30, pady=15, command=addButton)

# # displying buttons
# # here 'pady' gives tha padding ie extra space around button
# b1.grid(row=1 ,column=0, pady=2.5)
# b2.grid(row=1 ,column=1, pady=2.5)
# b3.grid(row=1 ,column=2, pady=2.5)
# b4.grid(row=2 ,column=0, pady=2.5)
# b5.grid(row=2 ,column=1, pady=2.5)
# b6.grid(row=2 ,column=2, pady=2.5)
# b7.grid(row=3 ,column=0, pady=2.5)
# b8.grid(row=3 ,column=1, pady=2.5)
# b9.grid(row=3 ,column=2, pady=2.5)
# b0.grid(row=4 ,column=0, pady=2.5)

# bclear.grid(row=4 ,column=1, columnspan=2, pady=2.5)
# bequal.grid(row=5 ,column=1, columnspan=2, pady=2.5)
# badd.grid(row=5 ,column=0, pady=5)

# root.mainloop()

# ##############################################################################################
# simple calculator

from tkinter import *

firstNum = None
operation = None

root = Tk()

root.title("Simple Calculator")

e = Entry(root, width=40)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10, ipady=20)

def numButton(number):
  current = e.get()
  e.delete(0, END)
  e.insert(0, str(current) + str(number))

def clearButton():
  e.delete(0, END)

def addButton():
  fNum = e.get()
  global firstNum, operation
  operation = 'add'
  firstNum = int(fNum)
  e.delete(0, END)

def subButton():
  fNum = e.get()
  global firstNum, operation
  operation = 'sub'
  firstNum = int(fNum)
  e.delete(0, END)

def mulButton():
  fNum = e.get()
  global firstNum, operation
  operation = 'mul'
  firstNum = int(fNum)
  e.delete(0, END)

def divButton():
  fNum = e.get()
  global firstNum, operation
  operation = 'div'
  firstNum = int(fNum)
  e.delete(0, END)
  

def equalBuuton():
  secondNumber = e.get()
  e.delete(0, END)
  if operation == 'add':
    e.insert(0, firstNum + int(secondNumber))
  elif operation == 'sub':
    e.insert(0, firstNum - int(secondNumber))
  elif operation == 'mul':
    e.insert(0, firstNum * int(secondNumber))
  elif operation == 'div':
    e.insert(0, firstNum / int(secondNumber))
  else:
    e.insert(0, 'Invalid operation')


b1 = Button(root, text="1", padx=30, pady=15, command=lambda: numButton(1))
b2 = Button(root, text="2", padx=30, pady=15, command=lambda: numButton(2))
b3 = Button(root, text="3", padx=30, pady=15, command=lambda: numButton(3))
b4 = Button(root, text="4", padx=30, pady=15, command=lambda: numButton(4))
b5 = Button(root, text="5", padx=30, pady=15, command=lambda: numButton(5))
b6 = Button(root, text="6", padx=30, pady=15, command=lambda: numButton(6))
b7 = Button(root, text="7", padx=30, pady=15, command=lambda: numButton(7))
b8 = Button(root, text="8", padx=30, pady=15, command=lambda: numButton(8))
b9 = Button(root, text="9", padx=30, pady=15, command=lambda: numButton(9))
b0 = Button(root, text="0", padx=30, pady=15, command=lambda: numButton(0))

bequal = Button(root, text="=", padx=73, pady=15, command=equalBuuton)
bclear = Button(root, text="clear", padx=63, pady=15, command=clearButton)
badd = Button(root, text="+", padx=30, pady=15, command=addButton)
bsub = Button(root, text="-", padx=30, pady=15, command=subButton)
bmul = Button(root, text="*", padx=30, pady=15, command=mulButton)
bdiv = Button(root, text="/", padx=30, pady=15, command=divButton)

b1.grid(row=1 ,column=0, pady=2.5)
b2.grid(row=1 ,column=1, pady=2.5)
b3.grid(row=1 ,column=2, pady=2.5)
b4.grid(row=2 ,column=0, pady=2.5)
b5.grid(row=2 ,column=1, pady=2.5)
b6.grid(row=2 ,column=2, pady=2.5)
b7.grid(row=3 ,column=0, pady=2.5)
b8.grid(row=3 ,column=1, pady=2.5)
b9.grid(row=3 ,column=2, pady=2.5)
b0.grid(row=4 ,column=0, pady=2.5)

bclear.grid(row=4 ,column=1, columnspan=2, pady=2.5)
bequal.grid(row=5 ,column=1, columnspan=2, pady=2.5)
badd.grid(row=5 ,column=0, pady=5)
bmul.grid(row=6 ,column=1, pady=5)
bdiv.grid(row=6 ,column=2, pady=5)
bsub.grid(row=6 ,column=0, pady=5)


root.mainloop()