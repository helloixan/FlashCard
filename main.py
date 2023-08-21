from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 80, "bold")
#------------------------- NEW FLASHCARD --------------------------#
try :
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError :
    data = pandas.read_csv('./data/korean_words.csv')
finally :
    to_learn = data.to_dict(orient="records")
current_word = {}
# known_words = []

def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(to_learn)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(word, text=current_word['Korean'], fill="black")
    canvas.itemconfig(title, text="Korean", fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(word, text=current_word['English'], fill="white")
    canvas.itemconfig(title, text="English", fill="white")

def known_card():
    # known_words.append(current_word)
    # unknown_words = [word for word in to_learn if word not in known_words]
    print(len(to_learn))
    to_learn.remove(current_word)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# -------------------------- UI SETUP -------------------------------#
window = Tk()
window.title("FLASHCARD APP")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

## Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./Images/card_front.png")
card_back_img = PhotoImage(file="./Images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=LANG_FONT)
word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)


## button
wrong_img = PhotoImage(file="./Images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="./Images/right.png")
known_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()