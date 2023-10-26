import tkinter as tk


def on_button_click(text):
    if text == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        current_text = display.get()
        if current_text == "Error":
            display.delete(0, tk.END)
        display.insert(tk.END, text)


root = tk.Tk()
root.title("Calculator")

root.configure(bg='#2E3B4E')
root.geometry('400x550')

display = tk.Entry(root, width=16, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, pady=20, padx=20, ipadx=20, ipady=20)
display.configure(bg='#364C63', fg='white')

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+",
]

row, col = 1, 0
for button in buttons:
    btn = tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                    command=lambda b=button: on_button_click(b))
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.configure(bg='#49A7CC', fg='black')
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
