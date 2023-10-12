from tkinter import *

window = Tk()
window.title("Girl Boss Clickers")
window.geometry("1000x1000")
window.resizable(width=False, height=False)
bg = PhotoImage(file = "background.png")

bgLabel = Label(window, image = bg)
bgLabel.place(x=0, y=0)

window.mainloop()