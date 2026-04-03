

'''
grid structure 
      col0.  col1.  col2.  col3..
row 0
row 1
row 2
row 3


place structure

you specify the acurate pixel

'''



from tkinter import *

def add():
    # by default entry takes string type input
    a = int(entry1.get()) # get will fetch the value written inside your entry field
    b = int(entry2.get())
    c = a+b
    s = f"The result of {a} + {b} = {c}"
    res.configure(text=s)

def sub():
    a = int(entry1.get()) # get will fetch the value written inside your entry field
    b = int(entry2.get())
    c = a-b
    s = f"The result of {a} - {b} = {c}"
    res.configure(text=s)

def mul():
    a = int(entry1.get()) # get will fetch the value written inside your entry field
    b = int(entry2.get())
    c = a*b
    s = f"The result of {a} x {b} = {c}"
    res.configure(text=s)

def fun(event=None):
    a = int(entry1.get())
    b = int(entry2.get())
    s = f"{a} + {b} = {a+b}\n  {a} - {b} = {a-b}\n   {a} x {b} = {a*b}"
    res.configure(text=s, bg="navy", fg="white")

window = Tk()

window.configure(bg="white")
window.title("Simple Calculator")
window.geometry("400x300+500+300")

heading = Label(window, text="Simple Calculator", bg="white", fg="red", font=('times new roman', 18, "bold"))
heading.place(x=120,y=10)

num1 = Label(window, text="Enter the first number",bg="white", fg="black", font=('times new roman', 16))
num1.place(x=20, y=60)

entry1 = Entry(window, width=10, bg="lightblue", fg="black")
entry1.place(x=200, y=60)

num2 = Label(window, text="Enter the second number",bg="white", fg="black", font=('times new roman', 16))
num2.place(x=20, y=90)

entry2 = Entry(window, width=10, bg="lightblue", fg="black")
entry2.place(x=200, y=90)

btn1 = Button(window, text="Add", command=add) #function binding : you only write the fncn name
btn1.place(x=70, y=140)

btn2 = Button(window, text="Sub", command=sub) #function binding : you only write the fncn name
btn2.place(x=150, y=140)

btn3 = Button(window, text="Mul", command=mul) #function binding : you only write the fncn name
btn3.place(x=240, y=140)

# if you want to bind keyboard key with the functionality
window.bind("<Return>", fun) #enter key in your keyboard

res = Label(window, text="The result is:  ", bg="yellow", fg="black", font=('times new roman', 16, "italic"))
res.place(x=50, y=200)
window.mainloop()

