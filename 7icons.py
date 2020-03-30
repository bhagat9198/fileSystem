from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# adding title to window
root.title('Hello!!!')

# adding the custom icon on window inplace of default icon of tkinter
# we can add absolute or realtive of the image, but before the path appned "r" at begining 
root.iconbitmap(r'.\extra\fileicon.ico')
root.iconbitmap()

# adding the image file as title which is not .ico file
# root.iconbitmap(r'.\extra\index.png')
# root.iconbitmap()
# as file is too big, it will not get displayed!!

# adding images : its a 3 step process
# 1: specifing the image
# 2: putting the image inside some widget(label, text, etc)
# 3: displating the widget

# 1
# we can add absolute or realtive of the image
myImg = ImageTk.PhotoImage(Image.open('./extra/vscode.jpg'))
# 2
myLabel = Label(image=myImg)
# 3
myLabel.pack()

# adding another image
# myImg1 = ImageTk.PhotoImage(Image.open('./extra/bracket.ico'))
# myLabel1 = Label(image=myImg1)
# myLabel1.pack()



# creating quite button ie quite button will close the tkinter window
# root.quit : its an inbuild method
quitButton = Button(root, text='close the window', command=root.quit)
# displaying the quit button
quitButton.pack()

root.mainloop()

