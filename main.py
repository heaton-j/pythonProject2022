from tkinter import *

root = Tk()
root.title("Physical Activity Planner and Tracker")

message_text = StringVar()
message_text.set("Welcome, please select one of the three options below")

Sign_button = Button(root, text="Sign Up", width=90, height=10, bg='lightblue')
Sign_button.pack()

Log_button = Button(root, text="Log in", width=90, height=10, bg='pink')
Log_button.pack()

Help_button = Button(root, text="Help", width=90, height=10, bg='lightgreen')
Help_button.pack()

root.mainloop()

def help():
    print("Help")
    Back_button = Button(root, text="Back")
    Back_button.pack()

