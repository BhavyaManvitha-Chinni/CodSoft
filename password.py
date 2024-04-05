import random
import string
import tkinter as tk
from tkinter import ttk
def generate_password():
    password_length = length_var.get()
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
root = tk.Tk()
root.title("Password Generator")
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
length_label = ttk.Label(input_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
length_var = tk.IntVar(value=12)
length_entry = ttk.Entry(input_frame, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
generate_button = ttk.Button(input_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")
password_entry = ttk.Entry(root, font=("Courier", 12))
password_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.mainloop()