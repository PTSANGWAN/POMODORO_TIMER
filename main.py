from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
mark=""
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(c):
    c_min=math.floor(c/60)
    c_sec=c%60
    
    if c_sec<10:
        c_sec='0'+f'{c_sec}'
    my_canvas.itemconfig(timer_text, text=f"{c_min}:{c_sec}")
    if c>0:
        global timer
        timer=app_window.after(10,count_down,c-1)
    if c==0:
        
        if reps%2!=0:
            global mark
            mark+="✔"
            
            l2.config(text=mark) 
        start_action()
        
        

# ---------------------------- UI SETUP ------------------------------- #
app_window=Tk()
app_window.title("POMODORO TIMER")
app_window.config(padx=100,pady=50, bg=YELLOW)

my_canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img=PhotoImage(file="pomodoro_technique/tomato.png")

my_canvas.create_image(100,112,image=img)
timer_text=my_canvas.create_text(100,132,text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
my_canvas.grid(row=2,column=2)

# Labels
l1=Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
l1.grid(row=1, column=2)

l2=Label(fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
l2.grid(row=4,column=2)

# Button actions
def start_action():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    if reps==8:
        count_down(long_break_sec)
        l1.config(text="Break", fg=RED) 
    elif reps<8:
        if reps%2 == 0:
            count_down(short_break_sec)
            l1.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)    
            l1.config(text="Work", fg=GREEN)


def reset_action():
    app_window.after_cancel(timer)
    l2.config(text="")
    l1.config(text="Timer")
    my_canvas.itemconfig(timer_text, text="00:00")
    global mark,reps
    mark=""
    reps=0

# Buttons
b1=Button(text="Start", command=start_action)
b1.grid(row=3, column=1)

b2=Button(text="Reset", command=reset_action)
b2.grid(row=3, column=3)



app_window.mainloop()