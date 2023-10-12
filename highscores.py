from tkinter import *

def load_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            high_scores = [line.strip().split("-") for line in file]
            high_scores = reversed(high_scores)
        return high_scores
    except FileNotFoundError:
        return []


window = Tk()
window.title("High Scores")
window.geometry("1000x1000")

title_label = Label(window, text = "High Scores").pack(pady=10)

scores_frame = Frame(window).pack()

high_scores_data = load_high_scores()
for i, (name, score) in enumerate(high_scores_data):
    data = Label(scores_frame, text=f"{i+1}. {name}: {score}")
    data.pack()

window.mainloop()