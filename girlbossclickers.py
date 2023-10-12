from tkinter import *
import tkinter as tk

score = 0

def clicker():
    global score
    score += 1
    scoreLbl.config(text='Score: {0}'.format(score))

def main():
    game = Tk()
    game.title("Girl Boss Clickers")
    game.geometry("1000x1000")

    global scoreLbl
    scoreLbl = Label(game, text ='Score: {0}'.format(score), font = "50")  
    scoreLbl.pack() 

    player = "Chris"
    if player == "issie":
        playerFace = PhotoImage(file = "resources/images/izzyface.png")
    elif player == "Ammarah":
        playerFace = PhotoImage(file = "resources/images/ammarahface.png")
    elif player == "Sumaiyah":
        playerFace = PhotoImage(file = "resources/images/sumface.png")
    elif player == "Sam":
        playerFace = PhotoImage(file = "resources/images/samface.png")
    else:
        playerFace = PhotoImage(file = "resources/images/chrisface.png")

    faceBtn = tk.Button(game, image=playerFace, command=clicker, borderwidth=0)
    faceBtn.pack()

    game.mainloop()

if __name__ == "__main__":
    main()
    