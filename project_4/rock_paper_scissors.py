import tkinter as tk
import random
import time

# Define a more professional color palette
primary_color = '#282c34'  # Dark background
secondary_color = '#61dafb'  # Light blue text
accent_color = '#f15a29'  # Orange

# Define font styles
label_font = ('Arial', 16, 'bold')
button_font = ('Arial', 14, 'bold')
radiobutton_font = ('Arial', 12)

# Define options and their winning combinations
options = ["rock", "paper", "scissors"]
win_dict = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

# Initialize score variables
user_score = 0
computer_score = 0


# Function to handle user's choice and determine the winner
def play_game(user_choice):
    global user_score, computer_score

    # Disable radio buttons after making a choice
    for button in radio_buttons:
        button.config(state="disabled")

    user_choice_label.config(text=f"Your choice: {user_choice}")

    # Simulate a delay for the computer's choice
    result_label.config(text="Computing...", fg=secondary_color)
    root.update()
    time.sleep(1)  # Delay for 1 second

    computer_choice = random.choice(options)

    # Update labels with computer's choice
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!", fg=secondary_color)
    elif win_dict[user_choice] == computer_choice:
        result_label.config(text="You win!", fg=accent_color)
        user_score += 1
    else:
        result_label.config(text="You lose!", fg=accent_color)
        computer_score += 1

    # Update score labels
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer's score: {computer_score}")

    # Create a 'Play Again' button to restart the game
    play_again_button = tk.Button(input_frame, text="Play Again", font=button_font, bg=accent_color, fg='black',
                                  command=play_again)
    play_again_button.pack(pady=10)


# Function to ask the user if they want to play again
def play_again():
    global play_again_button

    # Destroy the 'Play Again' button
    play_again_button.destroy()

    # Reset labels
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="", fg=secondary_color)

    # Reset selection
    rock_radio.select()

    # Enable all radio buttons
    for button in radio_buttons:
        button.config(state="normal")


# Initialize Tkinter GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("600x450")
root.configure(bg=primary_color)

# Create a main frame to hold all the elements
main_frame = tk.Frame(root, bg=primary_color)
main_frame.pack(pady=20)

# Create and place frames for different sections of the GUI
input_frame = tk.Frame(main_frame, bg=primary_color)
input_frame.grid(row=0, column=0, pady=10)

result_frame = tk.Frame(main_frame, bg=primary_color)
result_frame.grid(row=1, column=0)

# Create radio buttons for user's choice
user_choice = tk.StringVar()
rock_radio = tk.Radiobutton(input_frame, text="Rock", font=radiobutton_font, variable=user_choice, value="rock",
                            fg=secondary_color)
paper_radio = tk.Radiobutton(input_frame, text="Paper", font=radiobutton_font, variable=user_choice, value="paper",
                             fg=secondary_color)
scissors_radio = tk.Radiobutton(input_frame, text="Scissors", font=radiobutton_font, variable=user_choice,
                                value="scissors", fg=secondary_color)

# Pack the radio buttons
rock_radio.pack()
paper_radio.pack()
scissors_radio.pack()

# Create labels to display user's and computer's choices, and game result
user_choice_label = tk.Label(result_frame, text="", font=label_font, bg=primary_color, fg=secondary_color)
computer_choice_label = tk.Label(result_frame, text="", font=label_font, bg=primary_color, fg=secondary_color)
result_label = tk.Label(result_frame, text="", font=label_font, bg=primary_color, fg=secondary_color)

# Pack the labels
user_choice_label.pack()
computer_choice_label.pack()
result_label.pack()

# Create labels to display user's and computer's scores
user_score_label = tk.Label(result_frame, text=f"Your score: {user_score}", font=label_font, bg=primary_color,
                            fg=secondary_color)
computer_score_label = tk.Label(result_frame, text=f"Computer's score: {computer_score}", font=label_font,
                                bg=primary_color, fg=secondary_color)

# Pack the score labels
user_score_label.pack()
computer_score_label.pack()

# Create a list of radio buttons for easy enabling/disabling
radio_buttons = [rock_radio, paper_radio, scissors_radio]

# Create a 'Play' button to play the game
play_button = tk.Button(input_frame, text="Play", font=button_font, bg=accent_color, fg='black',
                        command=lambda: play_game(user_choice.get()))
play_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
