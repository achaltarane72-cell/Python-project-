import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x400")

entry = tk.Entry(root, font=("Arial", 20), bd=8, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

def press(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

frame = tk.Frame(root)
frame.pack()

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','C','=','+']
]

for i in range(4):
    for j in range(4):
        text = buttons[i][j]
        
        if text == "C":
            btn = tk.Button(frame, text=text, width=5, height=2, command=clear)
        elif text == "=":
            btn = tk.Button(frame, text=text, width=5, height=2, command=equal)
        else:
            btn = tk.Button(frame, text=text, width=5, height=2,
                            command=lambda t=text: press(t))
        
        btn.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
