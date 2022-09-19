from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title("Physical Activity Planner and Tracker")
root.geometry("800x575")

Home = Frame(root)
Tracker = Frame(root)
Help = Frame(root)
Day_entry = Frame(root)

for frame in (Home, Tracker, Help):
    frame.grid(row=100, column=100, sticky='NEWS')

# creating the labels and buttons that will be shown on the home page
Label(Home, text='Home', width=8, height=4, font='sans 16 bold').pack()

Label(Home, text='Please select one of the options below to continue', width=90, height=6, font=100).pack()
home_tracker= Button(Home, text='Tracker', width=90, height=6, font=50, bg='lightgreen', command=lambda: raise_frame(Tracker)).pack()
home_help = Button(Home, text='Help', width=90, height=6, font=50, bg='lightpink', command=lambda: raise_frame(Help)).pack()
Button(Home, text='Log Out', width=90, height=6, font=50, bg='red', command=root.destroy).pack()

# creating the labels and buttons that will be shown on the tracker page
Label(Tracker, text='Tracker', width=90, height=3, font='sans 11 bold').pack()

Label(Tracker, text='Click on the box below to enter hours for each day where physical activity was completed :', bg='lightpink').pack()

Label(Tracker, text='!!!Remember at least 30 minutes of moderate physical activty is recommended each day!!!').pack()

Label(Tracker, text='The amount of physical activity done for this day :', font=50, height=3).pack()




# Label and combobox where users select the day they want to enter their data
Label(Tracker, text='Day : (eg. Thursday)', width=25, height=2, font=20).pack(pady=2, padx=3)
day_choice = StringVar()
Day_frame = ttk.Entry(Tracker, textvariable=day_choice, width=25)
Day_frame.pack(pady=2, padx=3)



# Label and combobox where users enter how much time they've done of physical activity
Label(Tracker, text='Time done : (eg. 95)', width=25, height=1, font=10).pack(pady=2, padx=3)
hour_choice = StringVar()
Hour_frame = ttk.Entry(Tracker, textvariable=hour_choice, width=25)
Hour_frame.pack(pady=2, padx=3)


# Window that pops up with calculations
def trackerMessage():
   day = Day_frame.get()
   time = Hour_frame.get()
   messagebox.showinfo(print('Day: {}', 'Time: {}'.format(day, time)))


def print(Tracker):
    print(Day_frame.get())
    print(Hour_frame.get())


# Button for user to enter their data chosen
Enter_button = ttk.Button(Tracker, text='Enter', width=10, command=trackerMessage).pack(pady=5)


# button that allows users to go back to the home page
Button(Tracker, text='Home', width=15, height=1, font=50, bg='lightblue', command=lambda: raise_frame(Home)).pack(
    ipadx=10, ipady=10, expand=True, side='left')

# creating the labels and buttons that will be shown on the help page
Label(Help, text='Help', width=90, height=5, font=80).pack()
Label(Help, text='Welcome to the Help Page', width=50, height=3, font=50).pack()


Button(Help, text='Home', width=30, height=2, font=50, bg='lightblue', command=lambda: raise_frame(Home)).pack()

raise_frame(Home)

root.mainloop()
