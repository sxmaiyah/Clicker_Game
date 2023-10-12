from tkinter import *

window = Tk()
window.title("Girl Boss Clickers")
window.geometry("1000x1000")
window.resizable(width=False, height=False)
#bg = PhotoImage(file = "background.png")

#bgLabel = Label(window, image = bg)
#bgLabel.place(x=0, y=0)

def gamePage():
    window.destroy()
    #import girlbossclickers

Button(
    window,
    text="Issie",
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Ammarah",
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Sumaiyah",
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window,
    text="Sam",
    command=gamePage
    ).pack(fill=X, expand=TRUE, side=LEFT)

window.mainloop()