from tkinter import *

window = Tk()
window.title("Girl Boss Clickers")
window.geometry("1150x1250")
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
    frame,
    text="Issie", image = issiephoto,
    command=gamePage
    ).grid(column=0, row=0)

#frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Ammarah", 
    image = ammarahphoto,
    command=gamePage
    ).grid(column=1, row=0)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Sumaiyah", 
    image = sumphoto,
    command=gamePage
    ).grid(column=2, row=0)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Sam", 
    image = samphoto,
    command=gamePage
    ).grid(column=0, row=1)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Chris", 
    image = chrisphoto,
    command=gamePage
    ).grid(column=1, row=1)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Marco", 
    image = marcophoto,
    command=gamePage
    ).grid(column=2, row=1)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

frame.pack()
window.mainloop()