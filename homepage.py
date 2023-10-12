import tkinter as tk

window = tk()
window.title("Girl Boss Clickers")
window.geometry("1000*1000")
bg = PhotoImage(file = "background.png")

bgLabel = Label(window, image = bg)
bgLabel.place(x=0, y=0)

window.mainloop()