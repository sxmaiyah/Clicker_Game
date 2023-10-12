from tkinter import *
import tkinter as tk

score = 0

def clicker(score):
    score += 1
    scoreLbl.config(text = "Score: {0}".format(score))

game = Tk()
game.title("Girl Boss Clickers")
game.geometry("1000x1000")

scoreLbl = Label(game, text ='Score: {0}'.format(score), font = "50")  
scoreLbl.pack() 

izzy = PhotoImage(file = "izzyface.png")

faceBtn = tk.Button(game, image=izzy, command=clicker(score))
faceBtn.pack()

game.mainloop()