#ARITHMETIC CALCULATOR

from tkinter import *

window = Tk()
window.title("Arithmetic Calculator")
window.geometry('800x200')

def calculate():
   
    try:
        num1 = float(e1.get())
        num2 = float(e2.get())
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return

    operation = operation_var.get()
    

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result_label.config(text="Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        result_label.config(text="Please select an operation.")
        return
    
    result_label.config(text=f"Result: {result}")


l1 = Label(window, text="Number 1:")
l1.grid(row=0, column=0, padx=10, pady=5)

e1 = Entry(window)
e1.grid(row=0, column=1, padx=10, pady=5)


l2 = Label(window, text="Number 2:")
l2.grid(row=1, column=0, padx=10, pady=5)

e2 = Entry(window)
e2.grid(row=1, column=1, padx=10, pady=5)

operation_var = StringVar()
operation_var.set("+")

l3 = Label(window, text="Operation:")
l3.grid(row=2, column=0, padx=10, pady=5)

operations_frame = Frame(window)
operations_frame.grid(row=2, column=1, padx=10, pady=5)

radio_add = Radiobutton(operations_frame, text="+", variable=operation_var, value="+")
radio_add.pack(side=LEFT)

radio_subtract = Radiobutton(operations_frame, text="-", variable=operation_var, value="-")
radio_subtract.pack(side=LEFT)

radio_multiply = Radiobutton(operations_frame, text="*", variable=operation_var, value="*")
radio_multiply.pack(side=LEFT)

radio_divide = Radiobutton(operations_frame, text="/", variable=operation_var, value="/")
radio_divide.pack(side=LEFT)

submit_b = Button(window, text="Calculate", command=calculate)
submit_b.grid(row=3, column=0, columnspan=2, pady=10)

result_label = Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()