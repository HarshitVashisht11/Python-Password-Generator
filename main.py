import random
import pyperclip
import string
import tkinter as tk
from tkinter import messagebox
def generate_password(length, include_letters, include_numbers, include_special):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if len(characters) == 0:
        messagebox.showerror("Error", "Please select at least one character type.")
        return None


    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password
    
def generate_button_click():
    length = int(length_entry.get())
    include_letters = letters_var.get()
    include_numbers = numbers_var.get()
    include_special = special_var.get()

    password = generate_password(length, include_letters, include_numbers, include_special)

    if password:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password generated and copied to clipboard!")
        
window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Password Length:")
length_label.pack(anchor = tk.W)
length_entry = tk.Entry(window)
length_entry.pack(anchor = tk.W)

letters_var = tk.BooleanVar()
letters_checkbutton = tk.Checkbutton(window, text="Include Letters", variable=letters_var)
letters_checkbutton.pack(anchor = tk.W)

numbers_var = tk.BooleanVar()
numbers_checkbutton = tk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_checkbutton.pack(anchor = tk.W)

special_var = tk.BooleanVar()
special_checkbutton = tk.Checkbutton(window, text="Include Special Characters", variable=special_var)
special_checkbutton.pack(anchor = tk.W)

generate_button = tk.Button(window, text="Generate Password", command=generate_button_click)
generate_button.pack(anchor = tk.W)

password_entry = tk.Entry(window)
password_entry.pack(anchor = tk.W)

window.mainloop()
    