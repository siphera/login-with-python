from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x300")
window.title("Register")
# window.configure(bg="yellow")


def result():
    amount = int(num_input.get())
    try:
        if amount > 3000:
            result_lbl.configure(text="You qualify for the Malaysia trip")
        else:
            result_lbl.configure(text="Please deposit more funds for this excursion")
    except TypeError:
        result_lbl.configure(text="Please enter a number")


def clear():
    num_input.delete(0, END)
    result_lbl.configure(text="")


def exit_btn():
    message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        window.destroy()
    else:
        pass


num_input = Entry(window, width=35)
num_input.place(x=60, y=30)

btn = Button(window, text="Result", command=result, bg="green")
btn.place(x=160, y=60)

result_lbl = Label(window, text="")
result_lbl.place(x=70, y=110)

clear_button = Button(window, text="Clear", command=clear)
clear_button.place(x=60, y=150)

exit_btn = Button(window, text="Exit", bg="red", command=exit_btn)
exit_btn.place(x=280, y=150)
window.mainloop()