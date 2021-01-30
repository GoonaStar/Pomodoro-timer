from tkinter import *
import math
from PIL import Image, ImageTk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label_timer.config(text="Timer", fg=GREEN)
    tick_symbol.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # Check if we are at reps repetition to set up the value of the timer
    if reps % 8 == 0:
        countdown(long_break_sec)
        label_timer.config(text="Long Break", fg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="Short Break", fg=PINK)
        tick_symbol.config(text="✔")
    else:
        countdown(work_sec)
        label_timer.config(text="Work", fg=RED)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_mark_str = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark_str += "✔"
            tick_symbol.config(check_mark_str)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label_timer.grid(column=2)

canvas = Canvas(width=400, height=424)
image = Image.open("322-3223817_rotten-tomatoes-logo-png.png.jpeg")
image = image.resize((600, 424))
tomato_img = ImageTk.PhotoImage(image)
canvas.create_image(200, 200, image=tomato_img)
timer_text = canvas.create_text(200, 230, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column=2)


button_start = Button(text="Start", command = start_timer, highlightthickness=0)
button_start.grid(row = 2, column=1)

button_reset = Button(text="Reset", command = reset_timer, highlightthickness=0)
button_reset.grid(row = 2, column = 3)

tick_symbol = Label(font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
tick_symbol.grid(row=3, column=2)













window.mainloop()