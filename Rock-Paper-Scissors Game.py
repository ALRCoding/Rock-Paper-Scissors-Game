import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.choices = ["rock", "paper", "scissors"]
        self.computer_choice = random.choice(self.choices)

        self.result_label = tk.Label(root, text="Choose rock, paper, or scissors:")
        self.result_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.check_result("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.check_result("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.check_result("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_text = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_text)
        self.result_label.pack(pady=10)

    def check_result(self, player_choice):
        self.computer_choice = random.choice(self.choices)

        if player_choice == self.computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and self.computer_choice == "scissors") or \
             (player_choice == "paper" and self.computer_choice == "rock") or \
             (player_choice == "scissors" and self.computer_choice == "paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        self.result_text.set(f"Your choice: {player_choice}\nComputer's choice: {self.computer_choice}\nResult: {result}")

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
