
# git clone https://github.com/Majdawad88/ECET411_PhoneProject.git
from tkinter import *
import time
root = Tk()
root.title("Phone")
e = Entry(root, width = 50,borderwidth = 25)
e.grid(row=0, column=0, columnspan=3,padx=10,pady=10)
phoneNumberInt = 0

def button_click(number):
        global phoneNumberInt
        e.insert(12,str(number))
        phoneNumberString = e.get()
        phoneNumberInt = int(phoneNumberString)

def button_clear():
        global phoneNumberInt
        phoneNumberInt = 0
        e.delete(0,END)

def button_hang():
        global phoneNumberInt
        phoneNumberInt = 0
        e.delete(0,END)
        e.insert(0, "Hanging")


def button_call():

        global phoneNumberInt
        f_num = phoneNumberInt
        if f_num > 1000000000 and f_num < 10000000000:
                e.delete(0,END)
                e.insert(0, "Calling......(" + str(f_num)+")")
        else:
                e.delete(0,END)
                e.insert(0, "Wrong Number Entered!")

button_7 = Button(root, text="7",padx=50, pady=20, command = lambda:button_click(7))
button_8 = Button(root, text="8",padx=50, pady=20, command = lambda:button_click(8))
button_9 = Button(root, text="9",padx=50, pady=20, command = lambda:button_click(9))
button_4 = Button(root, text="4",padx=50, pady=20, command = lambda:button_click(4))
button_5 = Button(root, text="5",padx=50, pady=20, command = lambda:button_click(5))
button_6 = Button(root, text="6",padx=50, pady=20, command = lambda:button_click(6))
button_1 = Button(root, text="1",padx=50, pady=20, command = lambda:button_click(1))
button_2 = Button(root, text="2",padx=50, pady=20, command = lambda:button_click(2))
button_3 = Button(root, text="3",padx=50, pady=20, command = lambda:button_click(3))
button_0 = Button(root, text="0",padx=50, pady=20, command = lambda:button_click(0))
button_call = Button(root, text="Call",padx=100, pady=20,fg = "white",bg = "green", command = button_call)
button_clear = Button(root, text="Clear",padx=40, pady=20, command = button_clear)
button_Hang = Button(root, text="Hang",padx=96, pady=20,fg = "white",bg = "red", command = button_hang)




button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_call.grid(row=4, column=1,columnspan=2)
button_clear.grid(row=5, column=0)
button_Hang.grid(row=5, column=1,columnspan=2)

root.mainloop()

