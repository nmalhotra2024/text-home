import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        # Get user inputs
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest
        simple_interest = (principal * rate * time) / 100

        # Compound Interest
        compound_amount = principal * (1 + rate / 100) ** time
        compound_interest = compound_amount - principal

        # Update output labels
        label_si_result.config(text=f"Simple Interest: {simple_interest:.2f}")
        label_ci_result.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values!")

# Main window
root = tk.Tk()
root.title("Simple & Compound Interest Calculator")
root.geometry("400x350")
root.config(bg="#f0f0f0")

# Widgets
title = tk.Label(root, text="Interest Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

# Principal Input
tk.Label(frame, text="Principal Amount:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
entry_principal = tk.Entry(frame, width=20)
entry_principal.grid(row=0, column=1, pady=5)

# Rate Input
tk.Label(frame, text="Rate of Interest (%):", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
entry_rate = tk.Entry(frame, width=20)
entry_rate.grid(row=1, column=1, pady=5)

# Time Input
tk.Label(frame, text="Time Period (years):", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
entry_time = tk.Entry(frame, width=20)
entry_time.grid(row=2, column=1, pady=5)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"),
                          command=calculate_interest, bg="lightblue")
btn_calculate.pack(pady=10)

# Result Labels
label_si_result = tk.Label(root, text="Simple Interest: ", font=("Arial", 12), bg="#f0f0f0")
label_si_result.pack(pady=5)

label_ci_result = tk.Label(root, text="Compound Interest: ", font=("Arial", 12), bg="#f0f0f0")
label_ci_result.pack(pady=5)

# Run the application
root.mainloop()
