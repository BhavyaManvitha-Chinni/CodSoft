import tkinter as tk
import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins"
def user_choice(choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Your choice: {choice}\nComputer's choice: {computer_choice}\nResult: {result}")
root = tk.Tk()
root.title("Rock, Paper, Scissors")
rock_button = tk.Button(root, text="Rock", command=lambda: user_choice('rock'))
rock_button.pack(pady=30)
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice('paper'))
paper_button.pack(pady=30)
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice('scissors'))
scissors_button.pack(pady=30)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=50)
root.mainloop()