from tkinter import *
from PIL import ImageTk,Image
root =Tk()
root.title("learn gui")
root.iconbitmap("")
my_img=ImageTk.PhotoImage(Image.open("D:\car2.jpg"))
label=Label(root,image=my_img)
label.pack()
root.mainloop()
