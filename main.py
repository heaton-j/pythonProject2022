from tkinter import *
from tkinter import ttk

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.title("Physical Activity Planner and Tracker")
root.geometry("775x600")

Home = Frame(root)
Calendar = Frame(root)
Tracker = Frame(root)
Help = Frame(root)
Day_entry = Frame(root)

for frame in (Home, Calendar, Tracker, Help):
    frame.grid(row=100, column=100, sticky='NEWS')

# creating the labels and buttons that will be shown on the home page
Label(Home, text='Home', width=90, height=5, font=190).pack()
Label(Home, text='Please select one of the options below to continue', width=90, height=5, font=100).pack()
home_calendar = Button(Home, text='Calendar', width=90, height=5, font=50, bg='lightblue', command=lambda: raise_frame(Calendar)).pack()
home_tracker= Button(Home, text='Tracker', width=90, height=5, font=50, bg='lightgreen', command=lambda: raise_frame(Tracker)).pack()
home_help = Button(Home, text='Help', width=90, height=5, font=50, bg='lightpink', command=lambda: raise_frame(Help)).pack()
Button(Home, text='Log Out', width=90, height=5, font=50, bg='red', command=root.destroy).pack()

# creating the labels and buttons that will be shown on the calendar page
Label(Calendar, text='Calendar', width=90, height=5, font=80).pack()
Label(Calendar, text='Welcome to the Calendar Page', width=50, height=3, font=50).pack()
Button(Calendar, text='Home', width=30, height=2, font=50, bg='lightyellow', command=lambda: raise_frame(Home)).pack()

# creating the labels and buttons that will be shown on the tracker page
Label(Tracker, text='Tracker', width=90, height=3, font=80).pack()
Label(Tracker, text='Welcome to the Tracker Page', width=50, height=1, font=50).pack()
Label(Tracker, text='Click on the box below to enter hours for each day where physical activity was completed :', bg='lightpink').pack()

Label(Tracker, text='The amount of physical activity done for the past week :', font=50, height=3).pack()

Label(Tracker, text='Day :', width=25, height=2, font=20).pack(pady=2, padx=3)
day_choice = StringVar()
Day_frame = ttk.Combobox(Tracker, textvariable=day_choice, width=25, height=8)
Day_frame['state'] = 'readonly'
Day_frame['values'] = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Day_frame.pack(pady=2, padx=3)

Label(Tracker, text='Hours and Minutes done :', width=25, height=2, font=20, ).pack(pady=2, padx=3)
hour_choice = StringVar()
Hour_frame = ttk.Combobox(Tracker, textvariable=hour_choice, width=25, height=8)
Hour_frame['state'] = 'readonly'
Hour_frame['values'] = ('0 hr', '1 hr', '2 hr', '3 hr', '4 hr', '5 hr')
Hour_frame.pack(pady=2, padx=3)
minute_choice = StringVar()
Minute_frame = ttk.Combobox(Tracker, textvariable=minute_choice, width=25, height=8)
Minute_frame['state'] = 'readonly'
Minute_frame['values'] = ('5 minutes', '10 minutes', '15 minutes', '20 minutes', '25 minutes', '30 minutes', '35 minutes',
                          '40 minutes', '45 minutes', '50 minutes', '55 minutes')
Minute_frame.pack(pady=20, padx=3)

# button for user to enter their data chosen
Button(Tracker, text='Enter', width=10, height=3).pack(pady=5)

# button that allows users to go back to the home page
Button(Tracker, text='Home', width=30, height=2, font=50, bg='lightyellow', command=lambda: raise_frame(Home)).pack()

# creating the labels and buttons that will be shown on the help page
Label(Help, text='Help', width=90, height=5, font=80).pack()
Label(Help, text='Welcome to the Help Page', width=50, height=3, font=50).pack()
Button(Help, text='Home', width=30, height=2, font=50, bg='lightyellow', command=lambda: raise_frame(Home)).pack()

raise_frame(Home)

root.mainloop()
