import tkinter as tk   # Import Tkinter library for GUI

# Create main window
root = tk.Tk()
root.title("Simple Calculator")   # Window title
root.geometry("320x400")          # Window size

# Create entry box to display numbers
entry = tk.Entry(root, font=("Arial", 20), bd=8, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Function to insert number/operator in entry box
def press(value):
    entry.insert(tk.END, value)

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def equal():
    try:
        result = eval(entry.get())   # Evaluate the expression
        entry.delete(0, tk.END)      # Clear entry
        entry.insert(0, result)      # Show result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")     # Show error if invalid input

# Create frame for buttons
frame = tk.Frame(root)
frame.pack()

# Button layout
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','C','=','+']
]

# Create buttons using loop
for i in range(4):
    for j in range(4):
        text = buttons[i][j]
        
        if text == "C":
            btn = tk.Button(frame, text=text, width=5, height=2, command=clear)  # Clear button
        elif text == "=":
            btn = tk.Button(frame, text=text, width=5, height=2, command=equal)  # Equal button
        else:
            btn = tk.Button(frame, text=text, width=5, height=2,
                            command=lambda t=text: press(t))  # Number/operator button
        
        btn.grid(row=i, column=j, padx=5, pady=5)  # Place button in grid

# Run the GUI window
root.mainloop()
