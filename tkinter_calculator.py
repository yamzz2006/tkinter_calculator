import tkinter as tk
from tkinter import messagebox

def calculator():
 try:
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    op = operator.get() 

    if op == "+":
      result = num1 + num2
    elif op == "-":
      result = num1 - num2    
    elif op == "*":
      result = num1 * num2
    elif  op == "/":
      if num2 == 0:
         messagebox.showerror("error","cannot divide by 0")
         return
      result = num1 / num2
    else:
        messagebox.showerror("Error","incorrect operator",)

    result_label.config(text=f"Result: {result}")

 except ValueError:
    messagebox.showerror("Enter valid number")  

 #tkintersetup
root = tk.Tk()
root.title("Simple calculator")

tk.Label(root, text="enter the first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="enter the second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root) 
entry2.grid(row=1, column=1, padx=10, pady=5)       

tk.Label(root, text="choose operator:" ).grid(row=2, column=0, padx=10, pady=5)
operator = tk.StringVar()
operator.set('+')
tk.OptionMenu(root,operator,'+','-','*','/').grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Calculate", command=calculator).grid(row=3, column=0, padx=10, pady=5)

result_label = tk.Label(root, text="result :")
result_label.grid(row=4, columnspan=2,  pady=5)






root.mainloop()   