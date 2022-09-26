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
home_tracker = Button(Home, text='Tracker', width=90, height=6, font=50, bg='lightgreen', command=lambda: raise_frame(Tracker)).pack()
home_help = Button(Home, text='Help', width=90, height=6, font=50, bg='light pink', command=lambda: raise_frame(Help)).pack()
Button(Home, text='Log Out', width=90, height=6, font=50, bg='red', command=root.destroy).pack()

# creating the labels and buttons that will be shown on the tracker page
Label(Tracker, text='Tracker', width=90, height=3, font='sans 11 bold').pack()
Label(Tracker, text='Click on the box below to enter hours for each day where physical activity was completed :', bg='light pink').pack()
Label(Tracker, text='!!!Remember at least 60 minutes of moderate physical activity is recommended each day!!!').pack()
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

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_entry = Day_frame.get()
# check day entered is in days
def checking():
   if day_entry in days:
       print(day_entry)
   elif day_entry not in days:
       day_error.config(text="Please re-enter a day of the week", fg='red')

day_error = Label(Tracker, text='')
day_error.pack()

# print day entered by user into text format
def check_day(Day_frame):
    day_entry = Day_frame.get()
    print("On {},".format(day_entry))

# function for numbers not in range 1 - 1440
def number_restrict(Hour_frame):
   number_entry = int(Hour_frame.get())
   if number_entry in range(1, 1441):
       print("The amount of physical activity you did is {} minutes".format(number_entry))
   elif number_entry not in range(1, 1441):
       restrict.config(text="Please re-enter a number between 1 and 1440", fg='red')

restrict = Label(Tracker, text='')
restrict.pack()

required_time = 60
def time():
    number_entry = int(Hour_frame.get())
    if number_entry == 60:
        print("You have reached the required time of physical activity for today")
    elif number_entry > 60:
        print("You have reached the required time of physical activity for today")
    else:
        print("You have not reached the required time of physical exercise for today")

# print minutes entered by users into text format
def check_number(Hour_frame):
   number_entry = int(Hour_frame.get())
   print("")

# validate input of Hour_frame in any other cases other than numbers are entered
def number():
  try:
      int(Hour_frame.get())
      answer.config(text="")
  except ValueError:
      answer.config(text="! Please enter a number !", fg='red')

answer = Label(Tracker, text='')
answer.pack(pady=5)

# button for entry that runs every function
Main_button = ttk.Button(Tracker, text="Enter", command=lambda: [check_day(Day_frame), number(), checking(),
number_restrict(Hour_frame), check_number(Hour_frame), time()]).pack()


# button that allows users to go back to the home page
Button(Tracker, text='Home', width=15, height=1, font=50, bg='lightblue', command=lambda: raise_frame(Home)).pack(
    ipadx=10, ipady=10, expand=True, side='left')


# creating the labels and buttons that will be shown on the help page
Label(Help, text='Help', width=90, height=3, font='sans 11 bold').pack()

Label(Help, text='To go back to main menu', font='sans 11 bold').pack()
Label(Help, text='Click on the "Home" button at bottom of this page').pack()

Label(Help, text='To go to tracker page', font='sans 11 bold').pack()
Label(Help, text='1: click on "Home" button at the bottom of this page').pack()
Label(Help, text='2: click on the light green button on the top of the home page titled "Tracker"').pack()

Label(Help, text='To end program', font='sans 11 bold').pack()
Label(Help, text='1: click on "Home" button at the bottom of this page').pack()
Label(Help, text='2: Click on the red button at the bottom of the home page titled "Log Out"').pack()

Label(Help, text='To choose day where physical activity was done', font='sans 11 bold').pack()
Label(Help, text='1: Go to home page and click on the light green button on the top of the page titled "Tracker"').pack()
Label(Help, text='2: Click on first entry widget below the "Day" title').pack()
Label(Help, text='3: Click on the button titled "Enter Day"').pack()

Label(Help, text='To enter time of physical activity done', font='sans 11 bold').pack()
Label(Help, text='1: Go to home page and click on the light green button at the top of the page titled "Tracker"').pack()
Label(Help, text='2: Click on the second entry widget below the "Minutes done" title').pack()
Label(Help, text='3: Click on the button titled "Enter Minutes"').pack()

Button(Help, text='Home', width=30, height=2, font=50, bg='lightblue', command=lambda: raise_frame(Home)).pack(pady=50, padx=2)

raise_frame(Home)

root.mainloop()
