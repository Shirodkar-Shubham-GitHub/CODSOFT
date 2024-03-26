import tkinter as tk
from tkinter import messagebox
import random

options = ["rock", "paper", "scissors"]
user_wins_count = 0
computer_wins_count = 0

def main():
    global user_wins_count, computer_wins_count
    user_input = user_input_entry.get().lower()
    if user_input not in options:
        messagebox.showinfo(message="Invalid Input Choice")
        quit()
    computer_choice = random.choice(options)
    messagebox.showinfo(message= f"Computer Picked: {computer_choice}".upper())
    
    if user_input == computer_choice:
        messagebox.showinfo(message= "Game Tied!")
    elif user_input == "rock" and computer_choice == "scissors" or user_input == "paper" and computer_choice == "rock" or user_input == "scissors" and computer_choice == "paper":
        user_wins_count += 1
        messagebox.showinfo(title='Result', message= f"User won the game")
        user_score_label.config(text = 'User Score : ' + str(user_wins_count))    
    else:
        messagebox.showinfo(message= f"Computer won the game")
        computer_wins_count += 1
        computer_score_label.config(text='Computer Score : ' + str(computer_wins_count))
    user_input_entry.delete(0,tk.END)

game = tk.Tk()
game.title("ROCK-PAPER-SCISSORS")

user_input_label = tk.Label(game, text="Choices", font = ("Helvetica", 13, "bold"), fg = "#FFFFFF", bg = "#808A87", padx=400, pady=10) 
user_input_label.pack()
user_input_label = tk.Label(game, text="ROCK/PAPER/SCISSORS", font = ("Helvetica", 12, "bold"), fg = "#2b2e30", bg = "#FFFFFF", padx=333, pady=10) 
user_input_label.pack()
user_input_label = tk.Label(game, text="Input One from Above", font = ("Helvetica", 12, "bold"), fg = "#FFFFFF", bg = "#2F4F4F", padx=348, pady=10) 
user_input_label.pack()

user_input_entry= tk.Entry(game, width=50, font=('Arial', 23))
user_input_entry.pack(pady=10)

result_button = tk.Button(game, text="Get Result", command=main, height=2, width=20, fg = "#FFFFFF", bg = "#00008B", font = ("Helvetica", 12, "bold")) 
result_button.pack(pady=4)

user_score_label = tk.Label(game, text = 'User Score : ', fg='black', font = ("Helvetica", 12, "bold"))
user_score_label.pack(pady = 5)

computer_score_label = tk.Label(game, text = 'Computer Score : ', fg = 'black', font = ("Helvetica", 12, "bold"))
computer_score_label.pack(padx = (10,0), pady = 5)

if __name__ == '__main__':
    game.mainloop()
