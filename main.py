from tkinter import *

root = Tk()
root.title("Physical Activity Planner and Tracker")

label1 = Label(root, text="Welcome, please select one of the three options below", height=5, font=("arial", 20))
label1.pack()

def sign_page ():
    print("Please create a password between 4-8 characters long")
    Enter_button = Button(root, text="Enter", width=50, height=5, command=sign_page)
    Enter_button.pack()


Sign_button = Button(root, text="Sign Up", width=150, height=3, bg='lightblue', font=("arial", 40), command=sign_page)
Sign_button.pack()

Log_button = Button(root, text="Log in", width=150, height=3, bg='pink', font=("arial", 40))
Log_button.pack()

Help_button = Button(root, text="Help", width=150, height=3, bg='lightgreen', font=("arial", 40))
Help_button.pack()

root.mainloop()


