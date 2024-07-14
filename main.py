from tkinter import *
import math



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    window.after_cancel(timer)
    canvas.itemconfig(text_counter, text="00:00")
    timer_label.config(text="Timer", fg="green")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_counter():

    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(long_sec)
        timer_label.config(text="Break", fg=RED)


    elif reps % 2 == 0:
        count_down(break_sec)
        timer_label.config(text="Break", fg=PINK)


    else:
        count_down(work_sec)
        timer_label.config(text="Work!", fg="green")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(text_counter, text=f"{count_min}:{count_sec}")

    if count > 0:

        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_counter()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, fg="green", font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_counter = canvas.create_text(100, 112, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_counter)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(bg=YELLOW, fg="green", font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)






window.mainloop()


