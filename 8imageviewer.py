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

# adding icon
# no need to put 'r' before path name as put "/" instaed of "\"
root.iconbitmap('./extra/fileicon.ico')

# adding all the images with path
pic1 = ImageTk.PhotoImage(Image.open('./extra/pic1.png'))
pic2 = ImageTk.PhotoImage(Image.open('./extra/pic2.png'))
pic3 = ImageTk.PhotoImage(Image.open('./extra/pic3.png'))
pic4 = ImageTk.PhotoImage(Image.open('./extra/pic4.jfif'))

# creating list of images
pics = [pic1, pic2, pic3, pic4]

# displaying first image when tkinter window will open
myLabel = Label(image=pic1)
myLabel.grid(row=0, column=0, columnspan=3)

# button functions
def backword():
  global updatedNum, myLabel, pics, backwardBtn, forwardBtn
  updatedNum = updatedNum - 1
  if updatedNum == 0:
    # before displaying updadted widget over the previous widget, we should remove the previous widget otherwise updated widget will overlap over existing previous widget.
    # thus, we delete the previous widget by 'grid_forget'
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


# buttons
if updatedNum == 0 :
  backwardBtn = Button(root, text='<<', command=backword, state=DISABLED)
  backwardBtn.grid(row=1, column=0)

quitBtn = Button(root, text='close', command=root.quit)
forwardBtn = Button(root, text='>>', command=forward)

quitBtn.grid(row=1, column=1)
forwardBtn.grid(row=1, column=2)


root.mainloop()