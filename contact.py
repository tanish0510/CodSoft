import tkinter as tk
from tkinter import messagebox

# Define a more professional color palette with black text
primary_color = '#F5F5F5'  # Light gray background
secondary_color = '#000000'  # Black text
accent_color = '#007BFF'  # Deep blue accent
highlight_color = '#FF8C00'  # Amber highlight

# Define font styles with black text
label_font = ('Arial', 16, 'bold')
entry_font = ('Arial', 14)
button_font = ('Arial', 14, 'bold')

# Create a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        contacts.append(contact)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required.")

# Function to update the contact list display
def update_contact_list(found_contacts=None):
    contact_list.delete(0, tk.END)
    contacts_to_display = found_contacts if found_contacts else contacts
    for contact in contacts_to_display:
        name = contact['Name']
        phone = contact['Phone']
        contact_list.insert(tk.END, f'{name}: {phone}')

# Function to search for a contact by name or phone number
def search_contact():
    search_query = search_entry.get().lower()
    found_contacts = []
    for contact in contacts:
        if search_query in contact['Name'].lower() or search_query in contact['Phone']:
            found_contacts.append(contact)
    update_contact_list(found_contacts)

# Function to update contact details
def update_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    for contact in contacts:
        if selected_contact.startswith(f'{contact["Name"]}: {contact["Phone"]}'):
            contact['Name'] = name_entry.get()
            contact['Phone'] = phone_entry.get()
            contact['Email'] = email_entry.get()
            contact['Address'] = address_entry.get()
            update_contact_list()
            clear_entries()
            return

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.get(contact_list.curselection())
    for contact in contacts:
        if selected_contact.startswith(f'{contact["Name"]}: {contact["Phone"]}'):
            contacts.remove(contact)
            update_contact_list()
            clear_entries()
            return

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("Contact Management System")
root.geometry("800x600")
root.configure(bg=primary_color)

# Create and place frames for different sections of the GUI
input_frame = tk.Frame(root, bg=primary_color)
input_frame.pack(pady=20)

result_frame = tk.Frame(root, bg=primary_color)
result_frame.pack()

search_frame = tk.Frame(root, bg=primary_color)
search_frame.pack()

# Create input labels and entry fields with black text
name_label = tk.Label(input_frame, text="Name:", font=label_font, bg=primary_color, fg=secondary_color)
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(input_frame, font=entry_font)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(input_frame, text="Phone:", font=label_font, bg=primary_color, fg=secondary_color)
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(input_frame, font=entry_font)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(input_frame, text="Email:", font=label_font, bg=primary_color, fg=secondary_color)
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(input_frame, font=entry_font)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(input_frame, text="Address:", font=label_font, bg=primary_color, fg=secondary_color)
address_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
address_entry = tk.Entry(input_frame, font=entry_font)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons for adding, updating, and deleting contacts
add_button = tk.Button(input_frame, text="Add Contact", font=button_font, bg=accent_color, fg='black', command=add_contact)
add_button.grid(row=4, column=0, pady=10)

update_button = tk.Button(input_frame, text="Update Contact", font=button_font, bg=accent_color, fg='black', command=update_contact)
update_button.grid(row=4, column=1, pady=10)

delete_button = tk.Button(input_frame, text="Delete Contact", font=button_font, bg=accent_color, fg='black', command=delete_contact)
delete_button.grid(row=5, column=0, pady=10)

# Create a label to display the contact list
contact_list = tk.Listbox(result_frame, font=entry_font, selectbackground=secondary_color, selectforeground=primary_color)
contact_list.pack()

# Create a search field and button with a different color scheme
search_label = tk.Label(search_frame, text="Search:", font=label_font, bg=primary_color, fg=secondary_color)
search_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
search_entry = tk.Entry(search_frame, font=entry_font)
search_entry.grid(row=0, column=1, padx=10, pady=5)
search_button = tk.Button(search_frame, text="Search", font=button_font, bg=highlight_color, fg='black', command=search_contact)
search_button.grid(row=0, column=2, pady=10)

# Start the Tkinter main loop
root.mainloop()
