from tkinter import *
import random

WHITE = "#FFFFFF"
BLACK = "#000000"
PURPLE = "#8F6570"
DARKBLUE = "#4B5166"
GREEN = "#E50038"
YELLOW = "#EFE0A0"
NEUTRAL = "#F0EFE6"
RED = "#E50038"
GREY = "#818589"
FONT_NAME = "Calibri"
H1_FONT_SIZE = 25
H2_FONT_SIZE = 15
P_FONT_SIZE = 15
TIMER_FONT_SIZE = 30
TRANS_COLOR = "#E51Af0"
text_string = None
timer_on = False
seconds = 60
restart_button = None

# ---------------------- Retrieve Words ---------------------- #
with open("wordlist.txt") as file:
    lines = file.readlines()
    words = [line.strip().lower() for line in lines]
    random.seed(43)
    text_list = random.choices(words, k=100)
    text_string = " ".join(text_list)

# ---------------------- Functions ---------------------- #
def start_timer():
    count_down()

def count_down():
    global seconds
    time_num.configure(text=f"{seconds}")
    if seconds > 0:
        seconds -= 1
        window.after(1000, count_down)
    else:
        input['state'] = 'disabled'
        show_results()

def show_results():
    global restart_button
    typed = input.get("1.0", "end").replace("\n", "")
    char = len(typed)
    characters_num.config(text=char)
    err = 0
    for index in range(0,len(typed)):
        if typed[index] != text_string[index]:
            err += 1
    errors_num.config(text=err)
    typed_list = typed.split(" ")
    words_min = 0
    text_string_list = text_string.split(" ")
    for index, word in enumerate(typed_list):
        if word == text_string_list[index]:
            words_min += 1
    speed_num.config(text = words_min)

    #change display
    time_label.config(text = "")
    time_num.config(text = "")
    # Restart button
    restart_button = Button(text="Restart", command=restart, width=15, font=(FONT_NAME, H2_FONT_SIZE),
                            compound="center", background=DARKBLUE, fg=YELLOW)
    restart_button.grid(column=4, row=7, columnspan=1)

def on_key_press(event):
    global timer_on
    if timer_on == False:
        time_label.config(text="Seconds Remaining:")
        time_num.config(text=seconds)
        timer_on = True
        start_timer()

def on_key_release(event):
    test_text.tag_remove('highlightline', "1.0", "end")
    typed = input.get("1.0", "end").replace("\n","")
    for index in range(0,len(typed)):
        if typed[index] != text_string[index]:
            test_text.tag_add('highlightline', f'1.0+{index}c', f'1.0+{index+1}c')
            test_text.tag_configure('highlightline', background='yellow')
            test_text.delete(f'1.0+{index}c', f'1.0+{index+1}c')
            test_text.insert(f'1.0+{index}c', text_string[index], ('highlightline'))

def restart():
    global timer_on
    global seconds
    timer_on = False
    seconds = 5
    restart_button.destroy()
    time_label.config(text = "")
    time_num.config(text="Start typing to begin test")
    characters_num.config(text="0")
    errors_num.config(text="0")
    test_text.tag_remove('highlightline', "1.0", "end")
    input['state'] = 'normal'
    input.delete('1.0', 'end')


window = Tk()
window.title("Typing Test")
window.config(padx = 100, pady = 50, bg=PURPLE)

title = Label(text="TEST YOUR TYPING SPEED", font = (FONT_NAME,H1_FONT_SIZE, "bold"), fg = YELLOW, background=PURPLE, compound = "center")
title.grid(column=4, row=0, columnspan = 1)

speed = Label(text="Words per Minute:", font = (FONT_NAME,H2_FONT_SIZE), fg = WHITE, background=PURPLE, compound = "center")
speed.grid(column=4, row=2, columnspan = 1)

speed_num = Label(text="0", font = (FONT_NAME,H2_FONT_SIZE), fg = WHITE, background=PURPLE, compound = "center")
speed_num.grid(column=4, row=3, columnspan = 1)

characters = Label(text="Characters:", font = (FONT_NAME,H2_FONT_SIZE), fg = WHITE, background=PURPLE, compound = "center")
characters.grid(column=3, row=4, columnspan = 1)

characters_num = Label(text="0", font = (FONT_NAME,H2_FONT_SIZE), fg = WHITE, background=PURPLE, compound = "center")
characters_num.grid(column=3, row=5, columnspan = 1)

errors = Label(text="Errors:", font = (FONT_NAME,H2_FONT_SIZE), fg = WHITE, background=PURPLE, compound = "center")
errors.grid(column=5, row=4, columnspan = 1)

errors_num = Label(text="0", font = (FONT_NAME,H2_FONT_SIZE), fg = WHITE, background=PURPLE, compound = "center")
errors_num.grid(column=5, row=5, columnspan = 1)

# Time label
time_label = Label(text="", font=(FONT_NAME, H2_FONT_SIZE), fg=WHITE, background=PURPLE,compound="center")
time_label.grid(column=4, row=6, columnspan=1)

# Time_num
time_num = Label(text="Start typing to begin test", font=(FONT_NAME, TIMER_FONT_SIZE), fg=WHITE, background=PURPLE, compound="center")
time_num.grid(column=4, row=7, columnspan=1)

spacer2 = Label(text = "", background = PURPLE)
spacer2.grid(column=5, row=8, columnspan = 1)

test_text = Text(width = 80, height = 7 , fg = GREY, font = (FONT_NAME,P_FONT_SIZE),
           wrap = "word")
test_text.insert("1.0", chars =text_string ) #TEXT_STRING
#test_text['state'] = 'disabled'
test_text.grid(column = 0, row = 9, columnspan = 9)

spacer1 = Label(text = "", background = PURPLE)
spacer1.grid(column=4, row=10, columnspan = 1)

input = Text(width = 80, height = 7 , fg = GREY, font = (FONT_NAME,P_FONT_SIZE),wrap = "word")
input.grid(column = 0, row = 11, columnspan = 9)
input.bind("<KeyRelease>", on_key_release)
input.bind("<KeyPress>", on_key_press)

window.mainloop()


