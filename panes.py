from tkinter import *


class Hotbar:
    def __init__(self, frame, update, calculate_grade):
        self.pane = PanedWindow(frame)
        self.name_label = Label(self.pane, text="Class:")
        self.name_label.grid(row=0, column=0, padx=0, pady=0)
        self.name_entry = Entry(self.pane, width=10)
        self.name_entry.grid(row=0, column=1, padx=0, pady=0)
        self.weighting_buttons = StringVar()
        self.points_button = Radiobutton(self.pane, text="Points", variable=self.weighting_buttons, value="points", command=update)
        self.weighted_button = Radiobutton(self.pane, text="Weighted", variable=self.weighting_buttons, value="weighted", command=update)
        self.points_button.grid(row=0, column=2, padx=0, pady=0)
        self.weighted_button.grid(row=0, column=3, padx=0, pady=0)
        self.points_button.select()
        self.calculate_grade_button = Button(self.pane, text="Calculate Grade", command=calculate_grade)
        self.calculate_grade_button.grid(row=0, column=4, padx=0, pady=0)
        self.grade_label = Label(self.pane, text="Grade:")
        self.grade_label.grid(row=0, column=5, padx=0, pady=0)



class Assignment:
    def __init__(self, frame, remove_assignment):
        self.pane = PanedWindow(frame)
        self.minus_button = Button(self.pane, text=" - ", command=lambda: remove_assignment(self))
        self.minus_button.grid(row=0, column=0, padx=0, pady=0)
        self.name_label = Label(self.pane, text="Assignment:")
        self.name_label.grid(row=0, column=1, padx=0, pady=0)
        self.name_entry = Entry(self.pane, width=20)
        self.name_entry.grid(row=0, column=2, padx=0, pady=0)
        self.grade_label = Label(self.pane, text="Grade:")
        self.grade_label.grid(row=0, column=3, padx=0, pady=0)
        self.earned_entry = Entry(self.pane, width=4)
        self.earned_entry.insert(0, "0")
        self.earned_entry.grid(row=0, column=4, padx=0, pady=0)
        self.divide_label = Label(self.pane, text="/")
        self.divide_label.grid(row=0, column=5, padx=0, pady=0)
        self.possible_entry = Entry(self.pane, width=4)
        self.possible_entry.insert(0, "100")
        self.possible_entry.grid(row=0, column=6, padx=0, pady=0)
        self.weight_label = Label(self.pane, text="Weight:")
        self.weight_label.grid(row=0, column=7, padx=0, pady=0)
        self.weight_entry = Entry(self.pane, width=4)
        self.weight_entry.insert(0, "1")
        self.weight_entry.grid(row=0, column=8, padx=0, pady=0)

    def earned(self):
        return float(self.earned_entry.get())

    def possible(self):
        return float(self.possible_entry.get())

    def weight(self):
        return float(self.weight_entry.get())

    def weighted_percentage(self):
        return float(self.earned_entry.get()) / float(self.possible_entry.get()) * float(self.weight_entry.get())



class Plusbar:
    def __init__(self, frame, create_assignment):
        self.pane = PanedWindow(frame)
        self.plus_button = Button(self.pane, text=" + ", command=create_assignment)
        self.plus_button.grid(row=0, column=0, padx=0, pady=0)