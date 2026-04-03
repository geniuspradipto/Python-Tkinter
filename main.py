# Desktop App development using Tkinter
# don't write the filename as tkinter.py 
# import statements - we import all the necessary modules
# import tkinter as tk
from tkinter import * # * - import all 

root = Tk()

root.title("Pradipto's Tkinter App")
root.geometry("600x300+450+300")
root.configure(bg="yellow")


# tkinter widgets - Label for text, entry for searchbox, button,
# text - Label()
# widgets

heading = Label(root, text="Database Connectivity using Python", bg="yellow", fg="black", font=("consolas", 18, "bold"))
heading.pack()
# grid, place

name = Label(root, text="Pradipto Chatterjee", bg="yellow", fg="red", font=("consolas", 14, "bold"))
name.pack()


root.mainloop() 
