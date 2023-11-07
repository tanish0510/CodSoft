import tkinter as tk
import random
import string
import pyperclip  # Library for clipboard operations

# Define a professional color palette
primary_color = '#282c34'  # Dark background
secondary_color = '#61dafb'  # Light blue text
accent_color = '#f15a29'  # Orange

# Define font styles
label_font = ('Arial', 16, 'bold')
entry_font = ('Arial', 14)
button_font = ('Arial', 14, 'bold')

# Create a function to generate a strong password and copy it to the clipboard
def generate_and_copy_password():
    try:
        nr_letters = int(letters_entry.get())
        nr_symbols = int(symbols_entry.get())
        nr_numbers = int(numbers_entry.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers for letters, symbols, and numbers.")
        return

    if nr_letters + nr_symbols + nr_numbers < 8:
        result_label.config(text="Password length must be at least 8 characters.")
        return

    all_characters = (
        string.ascii_letters + string.digits + string.punctuation
    )

    password_list = [random.choice(all_characters) for _ in range(nr_letters + nr_symbols + nr_numbers)]
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Copy the password to the clipboard
    try:
        pyperclip.copy(password)
        result_label.config(text=f"Your password is: {password}\nPassword copied to clipboard")
    except Exception as e:
        result_label.config(text=f"Failed to copy password to clipboard: {e}")

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("600x450")
root.configure(bg=primary_color)

# Create a main frame to hold all elements
main_frame = tk.Frame(root, bg=primary_color)
main_frame.pack(pady=20)

# Create and place frames for different sections of the GUI
input_frame = tk.Frame(main_frame, bg=primary_color)
input_frame.grid(row=0, column=0, pady=10)

result_frame = tk.Frame(main_frame, bg=primary_color)
result_frame.grid(row=1, column=0)

# Create input labels and entry fields
letters_label = tk.Label(input_frame, text="Letters:", font=label_font, bg=primary_color, fg=secondary_color)
letters_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
letters_entry = tk.Entry(input_frame, font=entry_font)
letters_entry.grid(row=0, column=1, padx=10, pady=5)

symbols_label = tk.Label(input_frame, text="Symbols:", font=label_font, bg=primary_color, fg=secondary_color)
symbols_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
symbols_entry = tk.Entry(input_frame, font=entry_font)
symbols_entry.grid(row=1, column=1, padx=10, pady=5)

numbers_label = tk.Label(input_frame, text="Numbers:", font=label_font, bg=primary_color, fg=secondary_color)
numbers_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
numbers_entry = tk.Entry(input_frame, font=entry_font)
numbers_entry.grid(row=2, column=1, padx=10, pady=5)

# Create a button to generate and copy the password
generate_button = tk.Button(input_frame, text="Generate and Copy Password", font=button_font, bg=accent_color, fg='black', command=generate_and_copy_password)
generate_button.grid(row=3, columnspan=2, pady=10)

# Create a label to display the generated password
result_label = tk.Label(result_frame, text="", font=label_font, bg=primary_color, fg=secondary_color)
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
