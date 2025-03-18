import time
from tkinter import *

class AppScreen:
    root = Tk() # class variable

    def app_start(self):
        self.main_window()
        # time.sleep(10)
        self.root.mainloop() # with this line, tkinter starts an infinite loop used to run the application,
        # wait for an event to occur and process the event as long as the window is not closed.

    def main_window(self):
        # Main Window
        self.root.title("Word")
        self.root.geometry("400x200")
        self.root.configure(bg="Sky Blue")

        # Frame 1
        frame1 = Frame(self.root, width=300, height=100)
        frame1.pack()
        label1 = Label(frame1, text="Learn New Words Everyday", font=("Arial", 22, "bold"), bg="Sky Blue", fg="Black")
        label1.pack()

        # for Entering value or numbers 1st Create and display a canvas on the GUI app
        canvas_widget = Canvas(self.root, width=300, height=150)
        canvas_widget.pack()
        # Canvas1 Header
        label2 = Label(canvas_widget, text="How many new words you learned today!", font=("Arial", 10, "bold"),
                       bg="Yellow", fg="Black"
                       )
        canvas_widget.create_window(150, 20, window=label2)

        # Create an input box for entering number in canvas 1
        enter_number = Entry(self.root, bd=3)
        canvas_widget.create_window(150, 50, window=enter_number)

        # Create canvas 1 Submit button
        submit_button = Button(text='Submit', command="submit_data")
        canvas_widget.create_window(125, 80, window=submit_button)

        # Create canvas 1 Clear button
        clear_button = Button(text='Clear', command="submit_data")
        canvas_widget.create_window(175, 80, window=clear_button)

        # Create canvas 1 Close button
        # create button to implement destroy()
        close_button = Button(self.root, text="Close", command=self.root.destroy)
        canvas_widget.create_window(150, 110, window=close_button)


