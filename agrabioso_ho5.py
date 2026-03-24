import tkinter as unak

window = unak.Tk()
window.title("kristin")
window.configure(bg="white")
window.geometry("200x100")

wel = unak.Label(window,text="WELCOME",bg = "white")
wel.grid(column=2,row=0,columnspan=1)
#wel.pack()

def register():
    if re: 
        reg = unak.Toplevel(window)
        reg.title("register")

        label= unak.Label(window,text="register form")
        label.grid(column=1,row=0,columnspan=1)
        uname = unak.Label(window,text="username")
        uname.grid(column=1,row=1,columnspan=2)

        ue = unak.Entry(window)
        ue.grid(column=3,row=1,columnspan=2)

        passw = unak.Label(window,text="password")
        passw.grid(column=1,row=2,columnspan=2)

        pe = unak.Entry(window)
        pe.grid(column=3,row=1,columnspan=2)

    re.bind("<Return>",register)
    
def log():
    unak.Toplevel(window)



#sub = unak.IntVar()

re = unak.Button(window,text="REGISTER",bg = "blue",fg = "white",command = "register",relief = "sunken")
re.grid(column=2,row=1,columnspan=1)
#re.pack()

log = unak.Button(window,text="Log in",bg = "green",fg= "black",command = "log",relief = "sunken")
re.grid(column=2,row=2,columnspan=1)
#log.pack()

#regi = unak.Toplevel()
#regi.title("register")
#regi.mainloop()


window.mainloop()