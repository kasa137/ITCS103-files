import tkinter as unak 

window = unak.Tk()
#window.geometry("500x250")
window.configure(bg="lightblue")
window.title("kristin")

frame = unak.Frame(window,bg ="lightgreen")
frame.grid(column=1,row=1,columnspan=6)

label = unak.Label(window,text="Profile Buider",bg="lightblue")
label.grid(column=3,row=0,columnspan=2)

ena = unak.Entry(frame)
ena.grid(column=2,row=3,columnspan=2)

fna = unak.Label(frame,text="first name",bg="lightgreen")
fna.grid(column=2,row=4,columnspan=2)

em = unak.Entry(frame)
em.grid(column=7,row=3,columnspan=2)

mna = unak.Label(frame,text="middle name",bg="lightgreen")
mna.grid(column=7,row=4,columnspan=2)

el = unak.Entry(frame)
el.grid(column=10,row=3,columnspan=2)

lna = unak.Label(frame,text="last name",bg="lightgreen")
lna.grid(column=10,row=4,columnspan=2)

bye = unak.Entry(frame)
bye.grid(column=2,row=5,columnspan=2)

by = unak.Label(frame,text="birth year",bg="lightgreen")
by.grid(column=2,row=6,columnspan=2)

old = unak.Label(frame,text="you are ??? years old",bg="lightgreen",font="poppins")
old.grid(column=7,row=6,columnspan=3)


lgender = unak.Label(frame,text="Gender",bg="lightgreen")
lgender.grid(column=1,row=7,columnspan=2)


def show():
    b = bye.get()
    ts = int(bye)
    tss = 2026 * ts
    old['text'] = f"you are {tss}"



btn = unak.IntVar()

mbutton = unak.Radiobutton(frame,text="male",variable=btn,bg="lightgreen",value=0)
mbutton.grid(column=5,row=7,columnspan=1)

fbutton = unak.Radiobutton(frame,text="female",variable=btn,bg="lightgreen",value=1)
fbutton.grid(column=7,row=7,columnspan=1)

submit = unak.Button(window,text="Submit",command=show,relief="sunken",activebackground="green",activeforeground="black",bg="lightgreen")
submit.grid(column=4,row=7,columnspan=1)


window.mainloop()