from tkinter import *
root=Tk()
root.geometry('300*200')

def login():
    uname = username.get()
    pwd = password.get()

    if uname =='client' and pwd == 'server':
        message.set('Login successfully')
    else:
        message.set('Try again!')

        username = StringVar()
        password = StringVar()
        message = StringVar()

        user_lab = Label(root, text='Username: ', font=30)
        username = Entry(root, width=20, borderwidth=3, textvariable='username', font=30)

    root.mainloop()