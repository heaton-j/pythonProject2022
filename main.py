from tkinter import *
import tkinter

root = Tk()
root.title("Physical Activity Planner and Tracker")

label1 = Label(root, text="Welcome, please select one of the three options below", height=5, font=("arial", 20))
label1.pack()

def sign_page():
    sign_pagetext.pack()

def log_page():
    log_pagetext.pack()

def help_page():
    help_pagetext.pack()

Sign_button = tkinter.Button(root, text="Sign Up", width=15, height=1, bg='lightblue', font=("arial", 30), command=sign_page)
Sign_button.pack()

Log_button = tkinter.Button(root, text="Log In", width=15, height=1, bg='pink', font=("arial", 30), command=log_page)
Log_button.pack()

Help_button = tkinter.Button(root, text="Help", width=15, height=1, bg='lightgreen', font=("arial", 30), command=help_page)
Help_button.pack()

sign_pagetext = tkinter.Label(root, text="Please create a password between 3-6 characters")
log_pagetext = tkinter.Label(root, text="Please enter your password below")
help_pagetext = tkinter.Label(root, text="Please read below for help")

root.mainloop()


