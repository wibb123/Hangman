import random
import re
from tkinter import *
from tkinter import messagebox
from hangman_pics import HANGMANPICS

answer = ''
answer_array = [0]
answer_length = 0
count = 0


# FUNCTIONS
def b_click(b):
    global count
    b.config(state=DISABLED)
    if b["text"] in answer:
        positions = [m.start() for m in re.finditer(b["text"], answer)]
        for i in positions:
            answer_array[i] = b["text"]
        construct_answer_box()
    else:
        hangmanBox["text"] = HANGMANPICS[count]
        count += 1
    check_for_win_or_lose()


def check_for_win_or_lose():
    if count == 7:
        messagebox.showinfo(title="Hangman", message="Loser!, the word was " + answer)
        disable_all_buttons()
    elif 0 not in answer_array:
        messagebox.showinfo(title="Hangman", message="Congratulations, you have won!")
        disable_all_buttons()
    else:
        pass


def construct_answer_box():
    global answer_length
    answerBox["text"] = ""
    for i in answer_array:
        if i == 0:
            answerBox["text"] = answerBox["text"] + "_" + " "
        else:
            answerBox["text"] = answerBox["text"] + str(i) + " "


def new_game():
    global answer, answer_array, answer_length, count
    b_a.config(state=ACTIVE)
    b_b.config(state=ACTIVE)
    b_c.config(state=ACTIVE)
    b_d.config(state=ACTIVE)
    b_e.config(state=ACTIVE)
    b_f.config(state=ACTIVE)
    b_g.config(state=ACTIVE)
    b_h.config(state=ACTIVE)
    b_i.config(state=ACTIVE)
    b_j.config(state=ACTIVE)
    b_k.config(state=ACTIVE)
    b_l.config(state=ACTIVE)
    b_m.config(state=ACTIVE)
    b_n.config(state=ACTIVE)
    b_o.config(state=ACTIVE)
    b_p.config(state=ACTIVE)
    b_q.config(state=ACTIVE)
    b_r.config(state=ACTIVE)
    b_s.config(state=ACTIVE)
    b_t.config(state=ACTIVE)
    b_u.config(state=ACTIVE)
    b_v.config(state=ACTIVE)
    b_w.config(state=ACTIVE)
    b_x.config(state=ACTIVE)
    b_y.config(state=ACTIVE)
    b_z.config(state=ACTIVE)
    with open("./standard-words", "r") as file:
        txt = file.read()
        words = txt.splitlines()
        random_word = random.choice(words)
    answer = random_word
    answer_length = len(answer)
    answer_array = [0 for _ in answer]
    construct_answer_box()
    hangmanBox["text"] = ''
    count = 0


# disable all buttons
def disable_all_buttons():
    b_a.config(state=DISABLED)
    b_b.config(state=DISABLED)
    b_c.config(state=DISABLED)
    b_d.config(state=DISABLED)
    b_e.config(state=DISABLED)
    b_f.config(state=DISABLED)
    b_g.config(state=DISABLED)
    b_h.config(state=DISABLED)
    b_i.config(state=DISABLED)
    b_j.config(state=DISABLED)
    b_k.config(state=DISABLED)
    b_l.config(state=DISABLED)
    b_m.config(state=DISABLED)
    b_n.config(state=DISABLED)
    b_o.config(state=DISABLED)
    b_p.config(state=DISABLED)
    b_q.config(state=DISABLED)
    b_r.config(state=DISABLED)
    b_s.config(state=DISABLED)
    b_t.config(state=DISABLED)
    b_u.config(state=DISABLED)
    b_v.config(state=DISABLED)
    b_w.config(state=DISABLED)
    b_x.config(state=DISABLED)
    b_y.config(state=DISABLED)
    b_z.config(state=DISABLED)


# Initialising window
window = Tk()


# UI CONFIG
# making answer box
answerBox = Label(window, text="", height=2, width=30, font=("Arial", 10), bg="#4c4c4d", fg="white")

# making hangman box
hangmanBox = Label(window, text="", height=10, width=15, font=("Arial", 20), bg="#363636", fg="white")

# alphabet buttons
b_a = Button(window, text="a", height=1, width=2, font=("Arial", 10),
             command=lambda: b_click(b_a))
b_b = Button(window, text="b", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_b))
b_c = Button(window, text="c", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_c))
b_d = Button(window, text="d", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_d))
b_e = Button(window, text="e", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_e))
b_f = Button(window, text="f", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_f))
b_g = Button(window, text="g", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_g))
b_h = Button(window, text="h", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_h))
b_i = Button(window, text="i", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_i))
b_j = Button(window, text="j", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_j))
b_k = Button(window, text="k", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_k))
b_l = Button(window, text="l", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_l))
b_m = Button(window, text="m", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_m))
b_n = Button(window, text="n", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_n))
b_o = Button(window, text="o", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_o))
b_p = Button(window, text="p", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_p))
b_q = Button(window, text="q", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_q))
b_r = Button(window, text="r", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_r))
b_s = Button(window, text="s", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_s))
b_t = Button(window, text="t", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_t))
b_u = Button(window, text="u", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_u))
b_v = Button(window, text="v", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_v))
b_w = Button(window, text="w", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_w))
b_x = Button(window, text="x", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_x))
b_y = Button(window, text="y", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_y))
b_z = Button(window, text="z", height=1, width=2, font=("Arial", 10), 
             command=lambda: b_click(b_z))

# Grid set up
answerBox.grid(row=1, column=1, columnspan=9)
hangmanBox.grid(row=2, column=1, columnspan=9)

b_a.grid(row=3, column=1)
b_b.grid(row=3, column=2)
b_c.grid(row=3, column=3)
b_d.grid(row=3, column=4)
b_e.grid(row=3, column=5)
b_f.grid(row=3, column=6)
b_g.grid(row=3, column=7)
b_h.grid(row=3, column=8)
b_i.grid(row=3, column=9)

b_j.grid(row=4, column=1)
b_k.grid(row=4, column=2)
b_l.grid(row=4, column=3)
b_m.grid(row=4, column=4)
b_n.grid(row=4, column=5)
b_o.grid(row=4, column=6)
b_p.grid(row=4, column=7)
b_q.grid(row=4, column=8)
b_r.grid(row=4, column=9)

b_s.grid(row=5, column=1)
b_t.grid(row=5, column=2)
b_u.grid(row=5, column=3)
b_v.grid(row=5, column=4)
b_w.grid(row=5, column=5)
b_x.grid(row=5, column=6)
b_y.grid(row=5, column=7)
b_z.grid(row=5, column=8)

new_game_button = Button(text="Start New Game", height=1, width=15, font=("Arial", 10), command=new_game)
new_game_button.grid(row=6, column=1, columnspan=9)

disable_all_buttons()
# main loop
window.mainloop()
