import tkinter as tk
from tkinter import messagebox
import random

def add():
    num1 = float(user_num1_entry.get())
    num2 = float(user_num2_entry.get())
    #try:
    if type(num1) and type(num2) is int or float:
        addition = num1 + num2
        messagebox.showinfo(title= "Addition", message= f"Addition of {num1} and {num2} is {addition}")
        user_num1_entry.delete(0,tk.END)
        user_num2_entry.delete(0,tk.END)

def sub():
    num1 = float(user_num1_entry.get())
    num2 = float(user_num2_entry.get())
    if type(num1) and type(num2) is int or float:
        subtraction = num1 - num2
        messagebox.showinfo(title= "Subtraction", message= f"Subtraction of {num1} and {num2} is {subtraction}")
        user_num1_entry.delete(0,tk.END)
        user_num2_entry.delete(0,tk.END)
    
def mul():
    num1 = float(user_num1_entry.get())
    num2 = float(user_num2_entry.get())
    if type(num1) and type(num2) is int or float:
        multiplication = num1 * num2
        messagebox.showinfo(title= "Multiplication", message= f"Multiplication of {num1} and {num2} is {multiplication}")
        user_num1_entry.delete(0,tk.END)
        user_num2_entry.delete(0,tk.END)
        
def div():
    num1 = float(user_num1_entry.get())
    num2 = float(user_num2_entry.get())
    if type(num1) and type(num2) is int or float:
        division = num1 / num2
        messagebox.showinfo(title= "Division", message= f"Division of {num1} and {num2} is {division}")
        user_num1_entry.delete(0,tk.END)
        user_num2_entry.delete(0,tk.END)

game = tk.Tk()
game.title("Simple Calculator")
           
user_input_label = tk.Label(game, text="Simple Calculator", font = ("Helvetica", 13, "bold"), fg = "#FFFFFF", bg = "#808A87", padx=100, pady=10) 
user_input_label.pack()
user_input_label = tk.Label(game, text="First Number", font = ("Helvetica", 12, "bold"), fg = "#FFFFFF", bg = "#008080", padx=119, pady=10) 
user_input_label.pack()

user_num1_entry= tk.Entry(game, width=50, font=('Arial', 8))
user_num1_entry.pack(pady=10)

user_input_label = tk.Label(game, text="Second Number", font = ("Helvetica", 12, "bold"), fg = "#FFFFFF", bg = "#008080", padx=106, pady=10) 
user_input_label.pack()

user_num2_entry= tk.Entry(game, width=50, font=('Arial', 8))
user_num2_entry.pack(pady=10)

add_button = tk.Button(game, text="Addition", command=add, width=15, font = ("Helvetica", 10, "bold")) 
add_button.pack(pady=8)
sub_button = tk.Button(game, text="Subtraction", command=sub, width=15, font = ("Helvetica", 10, "bold")) 
sub_button.pack(pady=8)
mul_button = tk.Button(game, text="Multiplication", command=mul, width=15, font = ("Helvetica", 10, "bold")) 
mul_button.pack(pady=8)
div_button = tk.Button(game, text="Division", command=div, width=15, font = ("Helvetica", 10, "bold")) 
div_button.pack(pady=8)  

game.mainloop()
