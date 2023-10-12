from tkinter import *
import girlbossclickers

window = Tk()
window.title("Girl Boss Clickers")
window.geometry("1600x1300")
#window.resizable(width=False, height=False)
#bg = PhotoImage(file = "background.png")

#bgLabel = Label(window, image = bg)
#bgLabel.place(x=0, y=0)

def gamePage():
    window.destroy()
    girlbossclickers.main()

frame = Frame(window)


issiephoto = PhotoImage(file = "resources/images/izzyface.png")
ammarahphoto = PhotoImage(file = "resources/images/ammarahface.png")
samphoto = PhotoImage(file = "resources/images/samface.png")
sumphoto = PhotoImage(file = "resources/images/sumface.png")
chrisphoto = PhotoImage(file = "resources/images/chrisface.png")
marcophoto = PhotoImage(file = "resources/images/marcoface.png")
titlephoto = PhotoImage(file = "resources/images/Title.png")

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