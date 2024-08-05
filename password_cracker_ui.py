import tkinter as tk
from tkinter import filedialog, messagebox
import password_cracker

def browse_file():
    filename = filedialog.askopenfilename()
    entry_pass_file.delete(0, tk.END)
    entry_pass_file.insert(0, filename)

def crack_password():
    input_hash = entry_hash.get()
    pass_file_path = entry_pass_file.get()

    if not input_hash or not pass_file_path:
        messagebox.showwarning("Input Error", "Please provide both the hashed password and password file path.")
        return

    result = password_cracker.crack_password(input_hash, pass_file_path)
    messagebox.showinfo("Result", result)

app = tk.Tk()
app.title("Password Cracker")

# Hashed password input
tk.Label(app, text="Enter the hashed password:").grid(row=0, column=0, padx=10, pady=10)
entry_hash = tk.Entry(app, width=50)
entry_hash.grid(row=0, column=1, padx=10, pady=10)

# Password file path input
tk.Label(app, text="Enter passwords file path:").grid(row=1, column=0, padx=10, pady=10)
entry_pass_file = tk.Entry(app, width=50)
entry_pass_file.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=browse_file).grid(row=1, column=2, padx=10, pady=10)

# Crack password button
tk.Button(app, text="Crack Password", command=crack_password).grid(row=2, column=0, columnspan=3, pady=20)

app.mainloop()
