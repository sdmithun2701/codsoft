import tkinter as tk
from tkinter import messagebox
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numeric values.")
root = tk.Tk()
root.title("Simple Calculator")
bg_color = "#f0f0f0"
button_color = "#4CAF50"
button_fg = "white"
font = ("Helvetica", 12)
root.config(bg=bg_color)
tk.Label(root, text="Number 1:", bg=bg_color, font=font).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry1 = tk.Entry(root, width=15, font=font)
entry1.grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="Number 2:", bg=bg_color, font=font).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry2 = tk.Entry(root, width=15, font=font)
entry2.grid(row=1, column=1, padx=10, pady=10)
button_frame = tk.Frame(root, bg=bg_color)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="+", command=lambda: calculate('+'), bg=button_color, fg=button_fg, font=font, width=5).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="-", command=lambda: calculate('-'), bg=button_color, fg=button_fg, font=font, width=5).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="*", command=lambda: calculate('*'), bg=button_color, fg=button_fg, font=font, width=5).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="/", command=lambda: calculate('/'), bg=button_color, fg=button_fg, font=font, width=5).grid(row=0, column=3, padx=5, pady=5)

result_label = tk.Label(root, text="Result: ", bg=bg_color, font=font)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
root.mainloop()
