import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")

# Display
entry = tk.Entry(root, font=("Arial", 20), bd=8, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Functions
def press(value):
    current = entry.get()
    
    # Operator replace
    if current and current[-1] in "+-*/" and value in "+-*/":
        entry.delete(len(current)-1, tk.END)
        entry.insert(tk.END, value)
    else:
        entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Frame
frame = tk.Frame(root)
frame.pack()

# Helper to create button
def create_btn(text, row, col, cmd, colspan=1):
    btn = tk.Button(frame, text=text, width=5, height=2,
                    font=("Arial", 14), command=cmd)
    btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Row 1
create_btn('7',0,0, lambda: press('7'))
create_btn('8',0,1, lambda: press('8'))
create_btn('9',0,2, lambda: press('9'))
create_btn('/',0,3, lambda: press('/'))

# Row 2
create_btn('4',1,0, lambda: press('4'))
create_btn('5',1,1, lambda: press('5'))
create_btn('6',1,2, lambda: press('6'))
create_btn('*',1,3, lambda: press('*'))

# Row 3
create_btn('1',2,0, lambda: press('1'))
create_btn('2',2,1, lambda: press('2'))
create_btn('3',2,2, lambda: press('3'))
create_btn('-',2,3, lambda: press('-'))

# Row 4
create_btn('0',3,0, lambda: press('0'))
create_btn('.',3,1, lambda: press('.'))
create_btn('C',3,2, clear)
create_btn('+',3,3, lambda: press('+'))

# Row 5 (Special layout)
create_btn('X',4,0, backspace)
create_btn('=',4,1, equal, colspan=2)   # BIG "=" button
# last column empty automatically

# Run
root.mainloop()
