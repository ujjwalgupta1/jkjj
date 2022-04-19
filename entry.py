from tkinter import *
root=Tk()
e=Entry(root,width=50,bg="white",borderwidth=5)
e.grid(row=3,column=4)
e.insert(0,"enteryourname")

def myclick():

    mylabel=Label(root,text=e.get())
    mylabel.grid(row=4,column=2)

def myclick1():
    e.delete(0,END)
button=Button(root,text="click me",command=myclick,fg="blue",bg="#ffffff")
button.grid(row=0,column=1)

button2=Button(root,text="delete text",command=myclick1,fg="blue",bg="#ffffff")
button2.grid(row=1,column=2)
root.mainloop()

