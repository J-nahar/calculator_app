import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x450")
root.configure(bg="skyblue")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        result = float(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sin():
    entry.delete(0, tk.END)
    entry.insert(0, str(math.sin(math.radians(30))))

def cos():
    entry.delete(0, tk.END)
    entry.insert(0, str(math.cos(math.radians(60))))

def tan():
    entry.delete(0, tk.END)
    entry.insert(0, str(math.tan(math.radians(45))))

def log():
    try:
        result = math.log10(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
('7',1,0),('8',1,1),('9',1,2),('/',1,3),
('4',2,0),('5',2,1),('6',2,2),('*',2,3),
('1',3,0),('2',3,1),('3',3,2),('-',3,3),
('0',4,0),('.',4,1),('=',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    if text == '=':
        cmd = equal
    else:
        cmd = lambda t=text: click(t)

    tk.Button(root, text=text, width=6, height=2,
              bg="white", command=cmd).grid(row=row, column=col)

tk.Button(root,text="AC",width=6,bg="orange",command=clear).grid(row=5,column=0)
tk.Button(root,text="√",width=6,bg="lightgreen",command=sqrt).grid(row=5,column=1)
tk.Button(root,text="x²",width=6,bg="lightgreen",command=square).grid(row=5,column=2)
tk.Button(root,text="log",width=6,bg="lightgreen",command=log).grid(row=5,column=3)

tk.Button(root,text="sin",width=6,bg="lightblue",command=sin).grid(row=6,column=0)
tk.Button(root,text="cos",width=6,bg="lightblue",command=cos).grid(row=6,column=1)
tk.Button(root,text="tan",width=6,bg="lightblue",command=tan).grid(row=6,column=2)
#second commit
#git add .
#git commit -m"second try"
#git push
root.mainloop()
