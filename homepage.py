from tkinter import *

window = Tk()
window.title("Girl Boss Clickers")
window.geometry("1600x1300")
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
titlephoto = PhotoImage(file = "Title.png")

titleLabel = Label(frame, image = titlephoto, anchor = CENTER).grid(column=1, row=0) 

Button(
    frame,
    text="Issie", image = issiephoto,
    command=gamePage, borderwidth=0
    ).grid(column=0, row=1)

#frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Ammarah", 
    image = ammarahphoto,
    command=gamePage, borderwidth=0
    ).grid(column=1, row=1)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Sumaiyah", 
    image = sumphoto,
    command=gamePage, borderwidth=0
    ).grid(column=2, row=1)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Sam", 
    image = samphoto,
    command=gamePage, borderwidth=0
    ).grid(column=0, row=2)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Chris", 
    image = chrisphoto,
    command=gamePage, borderwidth=0
    ).grid(column=1, row=2)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

Button(
    frame,
    text="Marco", 
    image = marcophoto,
    command=gamePage, borderwidth=0
    ).grid(column=2, row=2)
    #frame.pack(fill=X, expand=TRUE, side=LEFT)

frame.pack()
window.mainloop()