from tkinter import *
from tkinter import messagebox

window1 = Tk()
window1.geometry("400x400")
window1.title("Register")

header = Label(window1, text="User Login", font=("arial", 30, "bold")).place(x=90, y=20)

user_lbl = Label(window1, text="Username:", font=("arial", 10, "bold")).place(x=40, y=100)
user_entry = Entry(window1)
user_entry.place(x=140, y=100)

pass_lbl = Label(window1, text="Username:", font=("arial", 10, "bold")).place(x=40, y=140)
pass_entry = Entry(window1, show="*")
pass_entry.place(x=140, y=140)

def login():
    all_users = {"siphe": "siphe123",
                 "user2": "10111"}

    username = user_entry.get()
    password = pass_entry.get()

    if(username, password) in all_users.items():
        messagebox.showinfo("Successful", "Login details correct")
        window1.withdraw()
        import excercise
        excercise.mainloop()

    else:
        messagebox.showinfo("Incorrect", "Login details Incorrect")
        user_entry.delete(0, END)
        pass_entry.delete(0, END)


login_btn = Button(window1, text="Login", bg="green", fg="white", command=login)
login_btn.place(x=240, y=180)

window1.mainloop()
