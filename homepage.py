from tkinter import *

window = Tk()
window.title("Girl Boss Clickers")
window.geometry("1000x500")
#window.resizable(width=False, height=False)
#bg = PhotoImage(file = "background.png")

#bgLabel = Label(window, image = bg)
#bgLabel.place(x=0, y=0)

def gamePage():
    window.destroy()
    #import girlbossclickers

frame = Frame(window)


issiephoto = PhotoImage(file = "izzyface.png")
ammarahphoto = PhotoImage(file = "ammarahface.png")
samphoto = PhotoImage(file = "samface.png")
sumphoto = PhotoImage(file = "sumface.png")
chrisphoto = PhotoImage(file = "chrisface.png")
marcophoto = PhotoImage(file = "marcoface.png")

Button(
    window,
    text="Issie", image = issiephoto,
    command=gamePage
    ).grid(column=0, row=0)

frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Ammarah", 
    image = ammarahphoto,
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Sumaiyah", 
    image = sumphoto,
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Sam", 
    image = samphoto,
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Chris", 
    image = chrisphoto,
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Marco", 
    image = marcophoto,
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

window.mainloop()