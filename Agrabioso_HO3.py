import tkinter as unak

window = unak.Tk()
window.title("kristin")
window.configure(bg="lightblue")

label = unak.Label(window, text="Simple Calculator", bg="lightblue")
label.grid(column=1, row=0, columnspan=2)

num1 = unak.Label(window, text="1st number")
num1.grid(column=0, row=1)

num1e = unak.Entry(window)
num1e.grid(column=1, row=1)

num2 = unak.Label(window, text="2nd number")
num2.grid(column=0, row=2)

num2e = unak.Entry(window)
num2e.grid(column=1, row=2)

result = unak.Label(window, text="", bg="lightblue")
result.grid(column=0, row=5, columnspan=3)


def add():
    num1 = int(num1e.get())
    num2 =int(num2e.get())
    sum = num1 + num2
    result["text"] = f"{num1} + {num2} = {sum}"

def subtract():
    num1 = int(num1e.get())
    num2 = int(num2e.get())
    sum = num1 - num2
    result["text"] = f"{num1} - {num2} = {sum}"


def multiply():
    num1 = int(num1e.get())
    num2 = int(num2e.get())
    sum = num1 * num2
    result["text"] = f"{num1} * {num2} = {sum}"


def division():
    num1 = int(num1e.get())
    num2 = int(num2e.get())
    sum = num1 / num2
    result["text"] = f"{num1} / {num2} = {sum}"


add_btn = unak.Button(window, text="Add", command=add,activebackground="green",activeforeground="lightgreen")
add_btn.grid(column=0, row=3)

sub_btn = unak.Button(window, text="Subtract", command=subtract,activebackground="green",activeforeground="lightgreen")
sub_btn.grid(column=1, row=3)

mul_btn = unak.Button(window, text="Multiply", command=multiply,activebackground="green",activeforeground="lightgreen")
mul_btn.grid(column=0, row=4)

div_btn = unak.Button(window, text="Division", command=division,activebackground="green",activeforeground="lightgreen")
div_btn.grid(column=1, row=4)

window.mainloop()