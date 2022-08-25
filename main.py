from tkinter import *
import calendar

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title("Physical activity planner and tracker")
root.geometry("775x600")

Home = Frame(root)
Calendar = Frame(root)
Tracker = Frame(root)
Help = Frame(root)

for frame in (Home, Calendar, Tracker, Help):
    frame.grid(row=100, column=100, sticky='news')

# creating the labels and buttons that will be shown on the home page
Label(Home, text='Home', width=90, height=5, font=190).pack()
Label(Home, text='Please select one of the options below to continue', width=90, height=5, font=100).pack()
Button(Home, text='Calendar', width=90, height=5, font=50, bg='lightblue', command=lambda: raise_frame(Calendar)).pack()
Button(Home, text='Tracker', width=90, height=5, font=50, bg='lightgreen', command=lambda: raise_frame(Tracker)).pack()
Button(Home, text='Help', width=90, height=5, font=50, bg='lightpink', command=lambda: raise_frame(Help)).pack()
Button(Home, text='Log Out', width=90, height=5, font=50, bg='red', command=root.destroy).pack()

# creating the labels and buttons that will be shown on the calendar page
Label(Calendar, text='Calendar', width=90, height=5, font=80).pack()
Label(Calendar, text='Welcome to the Calendar Page', width=50, height=3, font=50).pack()
Button(Calendar, text='Home', width=30, height=2, font=50, bg='lightyellow', command=lambda: raise_frame(Home)).pack()

# creating the labels and buttons that will be shown on the tracker page
Label(Tracker, text='Tracker', width=90, height=5, font=80).pack()
Label(Tracker, text='Welcome to the Tracker Page', width=50, height=3, font=50).pack()
Button(Tracker, text='Home', width=30, height=2, font=50, bg='lightyellow', command=lambda: raise_frame(Home)).pack()

# creating the labels and buttons that will be shown on the help page
Label(Help, text='Help', width=90, height=5, font=80).pack()
Label(Help, text='Welcome to the Help Page', width=50, height=3, font=50).pack()
Button(Help, text='Home', width=30, height=2, font=50, bg='lightyellow', command=lambda: raise_frame(Home)).pack()

raise_frame(Home)

root.mainloop()


