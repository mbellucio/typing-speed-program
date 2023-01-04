import tkinter as tk
import tkinter.messagebox
from words import words
from random import choice


#====================== FUNCTIONS AND VARIABLES ===========================#
WORD_LIST = []
WORD_OBJ_LIST = []
TIME = 60
timer_switch = False
word_count = 0


def gen_words():
    global WORD_LIST
    WORD_LIST = []
    for i in range (1, 121):
        word = choice(words)
        WORD_LIST.append(word)
    
    column = 0
    row = 2

    for item in WORD_LIST:
        if column == 6:
            column = 0
            row += 1
        word = tk.Label(text=item, font=('arial', 10, 'bold'), bg=BACKGROUND, fg='white', justify='left')
        word.grid(row=row, column=column)
        WORD_OBJ_LIST.append(word)
        column += 1


def check_words():
    global WORD_LIST, WORD_OBJ_LIST
    words_typed = text_entry.get("1.0",'end-1c')
    typed_words = words_typed.split()
    for item in typed_words:
        idx = typed_words.index(item)
        if typed_words[idx] == WORD_LIST[idx]:
            word_to_change = WORD_OBJ_LIST[idx]
            word_to_change.config(fg='#9CFF2E')
        else:
            word_to_change = WORD_OBJ_LIST[idx]
            word_to_change.config(fg='#FF1E00')
    window.update()


def check_wpm():
    global word_count
    typed_words = text_entry.get("1.0",'end-1c')
    typed_words = typed_words.split()
    for item in typed_words:
        idx = typed_words.index(item)
        if typed_words[idx] == WORD_LIST[idx]:
            word_count += 1


def clear_labels():
    global WORD_OBJ_LIST
    for item in WORD_OBJ_LIST:
        idx = WORD_OBJ_LIST.index(item)
        WORD_OBJ_LIST[idx].destroy()
    WORD_OBJ_LIST = []
    

def start():
    global timer_switch, word_count
    word_count = 0
    clear_labels()
    gen_words()
    timer_switch = True
    clock()
    Start_btn.config(text='Stop', command=stop)
    text_entry.config(state='normal')
    text_entry.delete("1.0",'end-1c')
    window.update()

def stop():
    global timer_switch
    timer_switch = False
    # clock()
    text_entry.delete("1.0",'end-1c')
    window.update()


def clock():
    global TIME, timer_switch, word_check, word_count
    if TIME != 0 and timer_switch:
        TIME -= 1
        time_label.config(text=f'Time Left:{TIME}')
        window.update()
        window.after(1000, func=clock)
    else:
        Start_btn.config(text='Start', command=start)
        timer_switch = False
        TIME = 60
        time_label.config(text=f'Time Left:{TIME}')
        check_wpm()
        text_entry.config(state='disabled')
        tkinter.messagebox.showinfo('Words Per Minute rate', f'Your words per minute rate is: {word_count}')
        
        window.update()

    
def rules():
    tkinter.messagebox.showinfo('Rules', 
    f'Once you press start:\n'
    f'\n1- You must type the words line by line\n'
    f'from left to right, separated by space.\n'
    f'\n2- You must type all characters correctly\n'
    f'in order to count as a correct typed word.\n'
    f'\n3- Once the timer ends, you can check\n'
    f'all correct and incorret words you typed\n'
    f'by pressing the "check words" button'
    )


#===================== GUI ======================#

BACKGROUND = '#495579'

#window
window = tk.Tk()
window.title('Typing Speed')
window.config(padx=20, pady=20, background=BACKGROUND)

#canvas
canvas1 = tk.Canvas(width=600, height=4, bg=BACKGROUND, highlightthickness=0)
canvas1.grid(row=23, column=0, columnspan=6)
canvas2 = tk.Canvas(width=600, height=4, bg='grey', highlightthickness=0)
canvas2.grid(row=1, column=0, columnspan=6)
canvas3 = tk.Canvas(width=600, height=4, bg='grey', highlightthickness=0)
canvas3.grid(row=24, column=0, columnspan=6)

#labels
time_label = tk.Label(text=f'Time Left:{TIME}', font=('arial', 22, 'bold'), bg=BACKGROUND, fg='white')
time_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)


#buttons
Start_btn = tk.Button(highlightthickness=0, bg='#ECE8DD', text='Start', padx=15, pady=2, command=start)
Start_btn.grid(column=5, row=0)
word_check = tk.Button(highlightthickness=0, bg='#ECE8DD', text='Check words', padx=15, pady=2, command=check_words)
word_check.grid(row=0, column=4)
rules_btn = tk.Button(highlightthickness=0, bg='#ECE8DD', text='Rules', padx=15, pady=2, command=rules)
rules_btn.grid(row=0, column=3)

#entry
text_entry = tk.Text(width=73, height=26)
text_entry.grid(row=25, column=0, columnspan=6)

gen_words()



#------------------
window.mainloop()
#------------------

 