from tkinter import *

root = Tk()
root.title("Physical Activity Planner and Tracker")

label1 = Label(root, text="Welcome, please select one of the three options below", height=5, font=("arial", 20))
label1.pack()

Sign_button = Button(root, text="Sign Up", width=190, height=3, bg='lightblue', font=("arial", 40))
Sign_button.pack()

Log_button = Button(root, text="Log in", width=190, height=3, bg='pink', font=("arial", 40))
Log_button.pack()

Help_button = Button(root, text="Help", width=190, height=3, bg='lightgreen', font=("arial", 40))
Help_button.pack()

root.mainloop()


