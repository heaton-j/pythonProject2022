from tkinter import *import tkinter as tk

root = Tk()
root.title("Physical Activity Planner and Tracker")

class ActivityApp(tk.Tk):
    def __init__(self):
        Tk.Frame.__init__(self)
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class HomePage(Tk.frame):
    def __init__(self,master):
     Tk.Frame.__init__(root,master)
    Label1 = Label(root, text="Please select one of the options below")
    Calendar_Button = Tk.Button(root, text="Go to Calendar",
                                    command=lambda: master.switch_frame(CalendarPage)).pack()


class CalendarPage(Tk.frame):
    def __init__(self,master):
        Tk.Frame.__init__(root,master)
    Label2 = Label(root, text="This is the calendar page")
    Back_Button = Tk.Button(root, text="Homepage",
                                 command=lambda: master.switch_frame(HomePage)).pack()


root.mainloop()


