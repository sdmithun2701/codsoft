import tkinter as tk
from tkinter import messagebox

# Initial contact list
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

# Function to view all contacts
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search a contact
def search_contact():
    search_term = search_entry.get()
    if search_term:
        results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        contact_list.delete(0, tk.END)
        for contact in results:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to update a contact
def update_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        contact = contacts[index]
        
        name = name_entry.get() or contact['name']
        phone = phone_entry.get() or contact['phone']
        email = email_entry.get() or contact['email']
        address = address_entry.get() or contact['address']
        
        if name and phone:
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            update_contact_list()
            clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required!")
    else:
        messagebox.showerror("Error", "No contact selected!")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        index = selected_contact[0]
        contacts.pop(index)
        update_contact_list()
    else:
        messagebox.showerror("Error", "No contact selected!")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("Contact Book")

# Frames for better organization
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

# Input fields
tk.Label(input_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(input_frame, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(input_frame, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(input_frame, width=30)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=0, padx=10)

view_button = tk.Button(button_frame, text="View All Contacts", command=update_contact_list)
view_button.grid(row=0, column=1, padx=10)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact)
search_button.grid(row=0, column=2, padx=10)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
update_button.grid(row=0, column=3, padx=10)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=0, column=4, padx=10)

# Search field
tk.Label(input_frame, text="Search").grid(row=4, column=0, padx=5, pady=5)
search_entry = tk.Entry(input_frame, width=30)
search_entry.grid(row=4, column=1, padx=5, pady=5)

# Contact listbox
contact_list = tk.Listbox(list_frame, height=15, width=50)
contact_list.pack()

# Initialize contact list display
update_contact_list()

# Run the application
root.mainloop()
