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


class StartPage():
    def __init__(self, parent, controller):

        # label of frame Layout 2
        label = tkinter.Label(self, text="Welcome, please select one of the three options below", font = 'arial')

        button1 = tkinter.Button(self, text="Sign in",
        command=lambda: controller.show_frame(Page1))

        ## button to show frame 2 with text layout2
        button2 = tkinter.Button(self, text="Log in",
        command=lambda: controller.show_frame(Page2))

        button3 = tkinter.Button(self, text="Help"),

# second window frame page1
class Page1():

    def __init__(self, parent, controller):

        Tk.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Page 1", font = 'arial')

        # button to show frame 2 with text
        # layout2
        button1 = tkinter.Button(self, text="StartPage",
                            command=lambda: controller.show_frame(StartPage))

        # button to show frame 2 with text
        # layout2
        button2 = tkinter.Button(self, text="Page 2",
                            command=lambda: controller.show_frame(Page2))

# third window frame page2
class Page2():

    def __init__(self, parent, controller):

        Tk.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Page 2", font='arial')

        # button to show frame 2 with text
        # layout2
        button1 = tkinter.Button(self, text="Page 1",
                            command=lambda: controller.show_frame(Page1))

        # button to show frame 3 with text
        # layout3
        button2 = tkinter.Button(self, text="Startpage",
                            command=lambda: controller.show_frame(StartPage))

class Page3():
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Help", font='arial')

        button1 = tkinter.Button(self, text="Log in")


        button2 = tkinter.Button(self, text="Sign in")

root.mainloop()


