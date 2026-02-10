import tkinter as unak

window = unak.Tk()
window.title("student profile")
window.geometry("600x600")
window.resizable(True,True)            
window.configure(bg= "purple",cursor = "cross")

label = unak.Label(window,text = "Kristin' s Profile", font =("cooper",35),bg = "purple")
label.pack(padx = 5,pady = 20)

label = unak.Label(window,text = " Age : 18 years old", font =("garamond",20),bg = "purple")
label.pack(padx = 5,pady = 20,anchor = "w")

label = unak.Label(window,text = "Course : BSIT ", font =("garamond",20),bg = "purple")
label.pack(padx = 5,pady = 20,anchor = "w")

label = unak.Label(window,text = "Birthday : March 13, 2007  ", font =("garamond",20),bg = "purple")
label.pack(padx = 5,pady = 20,anchor = "w")

label = unak.Label(window,text = "Motto : ", font =("garamond",20),bg = "purple")
label.pack(padx = 5,pady = 20,anchor = "w")

label = unak.Label(window,text = "l i f e i s c o o l ", font =("poppins",20),bg = "purple")
label.pack(padx = 5,pady = 20 ,anchor= "center")

label = unak.Label(window,text = "- BOYNEXTDOOR", font =("poppins",15),bg = "purple")
label.pack(padx = 5,pady = 20 ,anchor= "e")





window.mainloop()
