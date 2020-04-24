from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(bg='black')
e = Entry(root, width=30, justify=RIGHT, borderwidth=0, bg="Black", fg="White", font="Times 16 bold")
e.grid(row=0, column=0, columnspan=5, padx=0, pady=5)


# Input function

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


global f_num
global math


def button_addition():
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_num)
    e.delete(0, END)


def button_subtraction():
    first_num = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(first_num)
    e.delete(0, END)


def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_num)
    e.delete(0, END)


def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_num)
    e.delete(0, END)


def button_module():
    global math
    global f_num
    first_num = e.get()
    math = "module"
    f_num = float(first_num)
    e.delete(0, END)


def button_equal():
    second_num = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_num))

    if math == "subtract":
        e.insert(0, f_num - float(second_num))

    if math == "divide":
        e.insert(0, f_num / float(second_num))

    if math == "multiply":
        e.insert(0, f_num * float(second_num))

    if math == "module":
        e.insert(0, f_num % float(second_num))


# Define buttons

button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_clear = Button(root, text="clear", padx=20, pady=31, command=button_clear, bg="Black", fg="White", activebackground='black', activeforeground='white')
button_add = Button(root, text="+", padx=20, pady=10, command=button_addition, bg="Black", fg="White", activebackground='black', activeforeground='white')
button_subtra = Button(root, text="-", padx=23, pady=10, command=button_subtraction, bg="Black", fg="White", activebackground='black', activeforeground='white')
button_divi = Button(root, text="/", padx=23, pady=10, command=button_divide, bg="Black", fg="White", activebackground='black', activeforeground='white')
button_mul = Button(root, text="*", padx=22, pady=10, command=button_multiply, bg="Black", fg="White", activebackground='black', activeforeground='white')
button_eql = Button(root, text="=", padx=30, pady=31, command=button_equal, bg="Black", fg="White", activebackground='black', activeforeground='white')
button_dot = Button(root, text=".", padx=21, pady=10, command=lambda: button_click('.'), bg="Black", fg="White", activebackground='black', activeforeground='white')
button_mod = Button(root, text="%", padx=17, pady=10, command=button_module, bg="Black", fg="White", activebackground='black', activeforeground='white')

# Puts button on screen

button_9.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_clear.grid(row=1, column=4, rowspan=2)

button_6.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=2)
button_subtra.grid(row=2, column=3)

button_3.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=2)
button_mul.grid(row=3, column=3)
button_eql.grid(row=3, column=4, rowspan=2)

button_0.grid(row=4, column=0,)
button_dot.grid(row=4, column=1)
button_mod.grid(row=4, column=2)
button_divi.grid(row=4, column=3)

root.mainloop()
