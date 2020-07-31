#importing tkinter
from tkinter import *

# initalizing tkinter
top = Tk()
top.geometry("400x250")

# creating labels
uname = Label(top, text = "username").place(x = 20, y = 50)
password = Label(top, text = 'Password').place(x = 20, y = 90)

# creating submit button
sbmitbtn = Button(top, text = "Submit",activebackground = "pink",activeforeground = "blue").place(x = 50, y = 120)

# creating entries
e1 = Entry(top, width = 20).place(x = 100, y = 50)
s2 = Entry(top, width = 20).place(x = 100, y = 90)

# mainLoop
top.mainloop()

