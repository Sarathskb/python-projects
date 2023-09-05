import tkinter as tk
from tkinter import PhotoImage
import random
from PIL import Image, ImageTk

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        outcome_label.config(text="It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        outcome_label.config(text="You win!",bg="green")
    else:
        outcome_label.config(text="Computer wins!",bg="Red")

# Create the main window
root = tk.Tk()

root.title("Rock, Paper, Scissors")

root.geometry("350x200")
root.configure(bg="black")

# Load images for Rock, Paper, and Scissors buttons
rock_image = Image.open("C:\\Users\\ELCOT\\Downloads\\mcq\\python-projects\\rps\\rock.png")
paper_image = Image.open("C:\\Users\\ELCOT\\Downloads\\mcq\\python-projects\\rps\\paper.png")
scissors_image = Image.open("C:\\Users\\ELCOT\\Downloads\\mcq\\python-projects\\rps\\scissors.png")

rock_photo = ImageTk.PhotoImage(rock_image)
paper_photo = ImageTk.PhotoImage(paper_image)
scissors_photo = ImageTk.PhotoImage(scissors_image)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.place(x=20,y=10)

# Create buttons for player choices with images
rock_button = tk.Button(root, image=rock_photo, command=lambda: play_game("Rock"))
paper_button = tk.Button(root, image=paper_photo, command=lambda: play_game("Paper"))
scissors_button = tk.Button(root, image=scissors_photo, command=lambda: play_game("Scissors"))

rock_button.place(x=30,y=50)
paper_button.place(x=100,y=50)
scissors_button.place(x=200,y=50)

# Create a label to display the game outcome
outcome_label = tk.Label(root, text="")
outcome_label.place(x=180,y=10)

# Start the GUI main loop
root.mainloop()
