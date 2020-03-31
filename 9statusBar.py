from tkinter import *
from PIL import ImageTk, Image

updatedNum = 0
initialNum = None
myLabel = None
pics = None
backwardBtn = None
forwardBtn = None

root = Tk()

root.title('Image viwer')
root.iconbitmap('./extra/fileicon.ico')

pic1 = ImageTk.PhotoImage(Image.open('./extra/pic1.png'))
pic2 = ImageTk.PhotoImage(Image.open('./extra/pic2.png'))
pic3 = ImageTk.PhotoImage(Image.open('./extra/pic3.png'))
pic4 = ImageTk.PhotoImage(Image.open('./extra/pic4.jfif'))

pics = [pic1, pic2, pic3, pic4]

myLabel = Label(image=pic1)
myLabel.grid(row=0, column=0, columnspan=3)

# creating status bar
# bd: border
# relief: refers to certain simulated 3-D effects around the outside of the widget (FLAT, RAISED, SUNKEN, GROOVE, RIDGE )
# anchor: used to define where text is positioned relative to a reference point (E, W, N, S)
myStatus = Label(text='Image '+ str(updatedNum + 1)+' of '+ str(len(pics)), bd=2, relief=SUNKEN, anchor=E)

def backword():
  global updatedNum, myLabel, pics, backwardBtn, forwardBtn
  updatedNum = updatedNum - 1
  if updatedNum == 0:
    backwardBtn.grid_forget()
    backwardBtn = Button(root, text='<<', command=backword, state=DISABLED)
    backwardBtn.grid(row=1, column=0)
  
  if updatedNum < 3:
    forwardBtn.grid_forget()
    forwardBtn = Button(root, text='>>', command=forward)
    forwardBtn.grid(row=1, column=2)

  myLabel.grid_forget()
  myLabel = Label(image=pics[updatedNum])
  myLabel.grid(row=0, column=0, columnspan=3)

  # updating status bar
  myStatus = Label(text='Image '+ str(updatedNum +1)+' of '+ str(len(pics)), bd=2, relief=SUNKEN, anchor=E)
  # displaying status
  myStatus.grid_forget()
  myStatus.grid(row=2, column=0, columnspan=3, sticky=W+E, padx=5, pady=3)

def forward():
  global updatedNum, myLabel, pics, backwardBtn, forwardBtn
  updatedNum = updatedNum + 1
  if updatedNum > 0:
    backwardBtn.grid_forget()
    backwardBtn = Button(root, text='<<', command=backword)
    backwardBtn.grid(row=1, column=0)
  
  if updatedNum == 3:
    forwardBtn.grid_forget()
    forwardBtn = Button(root, text='>>', command=forward, state=DISABLED)
    forwardBtn.grid(row=1, column=2)

  myLabel.grid_forget()
  myLabel = Label(image=pics[updatedNum])
  myLabel.grid(row=0, column=0, columnspan=3)

  # updating status bar
  myStatus = Label(text='Image '+ str(updatedNum + 1)+' of '+ str(len(pics)), bd=2, relief=SUNKEN, anchor=E)
  # displaying status
  myStatus.grid_forget()
  myStatus.grid(row=2, column=0, columnspan=3, sticky=W+E, padx=5, pady=3)


backwardBtn = Button(root, text='<<', command=backword, state=DISABLED)
quitBtn = Button(root, text='close', command=root.quit)
forwardBtn = Button(root, text='>>', command=forward)

backwardBtn.grid(row=1, column=0)
quitBtn.grid(row=1, column=1)
forwardBtn.grid(row=1, column=2, pady=5)

# displaying status bar
# sticky: expands the widget [N: top, S: down, E: right, W:left]
myStatus.grid(row=2, column=0, columnspan=3, sticky=W+E, padx=5, pady=3)

root.mainloop()