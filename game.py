import tkinter as tk
import random
# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
# Function to update the score and display the result
def play(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")
# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
# Initialize scores
user_score = 0
computer_score = 0
# Create and place widgets
tk.Label(root, text="Choose rock, paper, or scissors:", font=("Arial", 14)).pack()
tk.Button(root, text="Rock", font=("Arial", 12), command=lambda: play("rock")).pack()
tk.Button(root, text="Paper", font=("Arial", 12), command=lambda: play("paper")).pack()
tk.Button(root, text="Scissors", font=("Arial", 12), command=lambda: play("scissors")).pack()
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()
score_label = tk.Label(root, text=f"Score: You {user_score} - Computer {computer_score}", font=("Arial", 14))
score_label.pack()
# Start the GUI event loop
root.mainloop()
