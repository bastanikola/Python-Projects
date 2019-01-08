#Question:
'''
Create a program that asks the user to submit a string or number through a
graphical user interface (GUI), and that string or number is stored as a new
line in an existing text file. Please have three buttons:
Add Line , Save Changes , and Save and Close.

Hint: Use the tkinter library.
'''
#Answer:
'''
from tkinter import *

window = Tk()

file = open("user_gui.txt", "a+")

def add():
    file.write(user_value.get() + "\n")
    entry.delete(0, END)

def save():
    global file
    file.close()
    file = open("user_gui.txt", "a+")

def close():
    file.close()
    window.destroy()

user_value = StringVar()
entry = Entry(window, textvariable=user_value)
entry.grid(row=0, column=0)

button_add = Button(window, text="Add line", command=add)
button_add.grid(row=0, column=1)

button_save = Button(window, text="Save changes", command=save)
button_save.grid(row=0, column=2)

button_close = Button(window, text="Save and Close", command=close)
button_close.grid(row=0,column=3)

window.mainloop()

Explanation:

We're using the standard tkinter  library here. In line 3 we create the window
of the interface and then we open a text file in a+  mode and we create three
functions. These functions will be executed when the user presses one of the
three buttons defined in line 24 through line 31. For example, button_add  is
attached to the add  function, so when the button is pressed, the text that was
entered in the Entry widget defined in line 21 is written in the text file. 
'''
