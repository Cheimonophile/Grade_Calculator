from tkinter import *
import filing
import os


class Info:
    # Assignments List
    assignment_panes = []
    # Name Path Map
    directory = os.getcwd() + "/saves"
    name = "Untitled"
    path = directory + "/" + name + ".txt"

    def update(self, cl, path):
        self.name = cl.name
        self.directory = path.rsplit("/", 1)[1]
        self


class Error_Popup:
    def __init__(self, message):
        self.frame = Tk()
        self.frame.title("Error")

        self.pane = PanedWindow(self.frame)
        self.pane.pack(padx=5, pady=5)

        self.label = Label(self.pane, text=message)
        self.label.pack()

        self.button = Button(self.frame, text=" OK ", command=self.frame.destroy)
        self.button.pack()

        self.frame.mainloop()


class Save_Popup:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Save")

        self.pane = PanedWindow(self.frame)
        self.pane.grid(row=0)

        self.location_label = Label(self.pane, text="Save Location:")
        self.location_label.grid(row=0, column=0, padx=0, pady=0, sticky='e')

        self.location_entry = Entry(self.pane)
        self.location_entry.grid(row=0, column=1, padx=0, pady=0)
        self.location_entry.insert(0, Info.directory)

        self.button = Button(self.frame, text=" Save ", command=self.save)
        self.button.grid(row=1, pady=5)

        self.frame.mainloop()

    def save(self):
        Info.directory = self.location_entry.get()
        Info.name = hotbar.name_entry.get()
        Info.path = Info.directory + "/" + Info.name + ".txt"
        filing.save(CL(), Info.path)
        self.frame.destroy()


class Load_Popup:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Load")

        self.path_label = Label(self.frame, text="Path:")
        self.path_label.grid(row=0, column=0, padx=0, pady=0, sticky='e')

        self.path_entry = Entry(self.frame)
        self.path_entry.grid(row=0, column=1, padx=0, pady=0)

        self.button = Button(self.frame, text=" Load ", command=self.load)
        self.button.grid(row=2, column=0, columnspan=2, pady=5)

        self.frame.mainloop()

    def load(self):
        try:
            cl = filing.load(self.path_entry.get())
            path = self.path_entry.get()
            # Updating Info
            Info.name = cl.name
            Info.directory = path.rsplit("/", 1)[0]
            Info.path = Info.directory + "/" + Info.name + ".txt"
            # Loading the name
            hotbar.name_entry.delete(0, END)
            hotbar.name_entry.insert(END, Info.name)
            # Loading the weighting buttons
            hotbar.weighting_buttons.set(cl.weighting)
            # Loading the assignments
            for i in reversed(range(len(Info.assignment_panes))):
                Info.assignment_panes[i].pane.destroy()
                Info.assignment_panes.pop()
            update()
            for assignment in cl.assignments:
                create_assignment_pane()
                Info.assignment_panes[-1].name_entry.insert(0, assignment[0])
                Info.assignment_panes[-1].earned_entry.delete(0, END)
                Info.assignment_panes[-1].earned_entry.insert(0, assignment[1])
                Info.assignment_panes[-1].possible_entry.delete(0, END)
                Info.assignment_panes[-1].possible_entry.insert(0, assignment[2])
                Info.assignment_panes[-1].weight_entry.delete(0, END)
                Info.assignment_panes[-1].weight_entry.insert(0, assignment[3])
            self.frame.destroy()
        except FileNotFoundError:
            Error_Popup("No such file or directory.")


class SaveAt_Popup:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Move")

        self.location_label = Label(self.frame, text="Location:")
        self.location_label.grid(row=0, column=0, padx=0, pady=0, sticky='e')

        self.location_entry = Entry(self.frame)
        self.location_entry.grid(row=0, column=1, padx=0, pady=0)

        self.button = Button(self.frame, text=" Move ", command=self.move)
        self.button.grid(row=2, column=0, columnspan=2, pady=5)

        self.frame.mainloop()

    def move(self):
        if not os.path.exists(self.location_entry.get()):
            Error_Popup("This path does not exist.")
        cl = CL()
        path = self.location_entry.get() + "/" + cl.name + ".txt"
        filing.save(cl, path)
        try:
            os.remove(Info.path)
        except:
            pass
        Info.directory = self.location_entry.get()
        Info.name = cl.name
        Info.path = path
        self.frame.destroy()





class Hotbar:
    def __init__(self, frame, update, calculate_grade):
        self.pane = PanedWindow(frame)

        self.name_label = Label(self.pane, text="Class:")
        self.name_label.grid(row=0, column=0, padx=0, pady=0)

        self.name_entry = Entry(self.pane, width=15)
        self.name_entry.insert(END, Info.name)
        self.name_entry.grid(row=0, column=1, padx=0, pady=0)

        self.save_button = Button(self.pane, text="Save", command=self.save)
        self.save_button.grid(row=0, column=2, padx=0, pady=0)

        self.load_button = Button(self.pane, text="Load", command=self.load)
        self.load_button.grid(row=0, column=3, padx=0, pady=0)

        self.move_button = Button(self.pane, text="Move", command=self.move)
        self.move_button.grid(row=0, column=4, padx=0, pady=0)

        self.weighting_buttons = StringVar()
        self.points_button = Radiobutton(self.pane, text="Points", variable=self.weighting_buttons, value="points",
                                         command=update)
        self.weighted_button = Radiobutton(self.pane, text="Weighted", variable=self.weighting_buttons,
                                           value="weighted", command=update)
        self.points_button.grid(row=0, column=5, padx=0, pady=0)
        self.weighted_button.grid(row=0, column=6, padx=0, pady=0)
        self.points_button.select()

        self.calculate_grade_button = Button(self.pane, text="Calculate Grade", command=calculate_grade)
        self.calculate_grade_button.grid(row=0, column=7, padx=0, pady=0)

        self.grade_label = Label(self.pane, text="Grade:")
        self.grade_label.grid(row=0, column=8, padx=0, pady=0)

    def save(self):
        new_name = self.name_entry.get()
        if Info.name == new_name:
            filing.save(CL(), Info.directory + "/" + new_name + ".txt")
        else:
            Save_Popup()

    def load(self):
        Load_Popup()

    def move(self):
        SaveAt_Popup()


class Assignment_Pane:
    def __init__(self, frame):
        self.pane = PanedWindow(frame)

        self.minus_button = Button(self.pane, text=" - ", command=lambda: remove_assignment_pane(self))
        self.minus_button.grid(row=0, column=0, padx=0, pady=0)

        self.down_button = Button(self.pane, text=" v ", command=lambda: move_down(self))
        self.down_button.grid(row=0, column=1, padx=0, pady=0)

        self.name_label = Label(self.pane, text="Assignment:")
        self.name_label.grid(row=0, column=2, padx=0, pady=0)

        self.name_entry = Entry(self.pane, width=20)
        self.name_entry.grid(row=0, column=3, padx=0, pady=0)

        self.grade_label = Label(self.pane, text="Grade:")
        self.grade_label.grid(row=0, column=4, padx=0, pady=0)

        self.earned_entry = Entry(self.pane, width=4)
        self.earned_entry.insert(0, "0")
        self.earned_entry.grid(row=0, column=5, padx=0, pady=0)

        self.divide_label = Label(self.pane, text="/")
        self.divide_label.grid(row=0, column=6, padx=0, pady=0)

        self.possible_entry = Entry(self.pane, width=4)
        self.possible_entry.insert(0, "100")
        self.possible_entry.grid(row=0, column=7, padx=0, pady=0)

        self.weight_label = Label(self.pane, text="Weight:")
        self.weight_label.grid(row=0, column=8, padx=0, pady=0)

        self.weight_entry = Entry(self.pane, width=4)
        self.weight_entry.insert(0, "1")
        self.weight_entry.grid(row=0, column=9, padx=0, pady=0)

    def earned(self):
        return float(self.earned_entry.get())

    def possible(self):
        return float(self.possible_entry.get())

    def weight(self):
        return float(self.weight_entry.get())

    def weighted_percentage(self):
        return float(self.earned_entry.get()) / float(self.possible_entry.get()) * float(self.weight_entry.get())


class Plusbar:
    def __init__(self, frame, create_assignment_pane):
        self.pane = PanedWindow(frame)
        self.plus_button = Button(self.pane, text=" + ", command=create_assignment_pane)
        self.plus_button.grid(row=0, column=0, padx=0, pady=0)


class CL:
    def __init__(self):
        self.name = Info.name
        self.weighting = hotbar.weighting_buttons.get()
        self.assignments = [(assignment_pane.name_entry.get(),
                            assignment_pane.earned_entry.get(),
                            assignment_pane.possible_entry.get(),
                            assignment_pane.weight_entry.get())
                            for assignment_pane in Info.assignment_panes]


def create_assignment_pane():
    Info.assignment_panes.append(Assignment_Pane(frame))
    update()


def remove_assignment_pane(assignment_pane):
    if len(Info.assignment_panes) < 2:
        return
    assignment_pane.pane.destroy()
    Info.assignment_panes.pop(Info.assignment_panes.index(assignment_pane))
    update()


def update():
    update_weighting()
    clear_grade()

    # cycles through all of the panes
    for i in range(len(Info.assignment_panes)):
        Info.assignment_panes[i].pane.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")
    plusbar.pane.grid(row=len(Info.assignment_panes) + 2)


def update_weighting():
    if hotbar.weighting_buttons.get() == "points":
        for assignment in Info.assignment_panes:
            assignment.weight_entry.config(state="disabled")
    if hotbar.weighting_buttons.get() == "weighted":
        for assignment in Info.assignment_panes:
            assignment.weight_entry.config(state="normal")


def calculate_grade():
    try:
        if hotbar.weighting_buttons.get() == "points":
            points_earned = sum([a.earned() for a in Info.assignment_panes])
            points_possible = sum([a.possible() for a in Info.assignment_panes])
            grade_string = "%" + str(round(points_earned / points_possible * 100, 2))
            hotbar.grade_label.config(text=grade_string)
        if hotbar.weighting_buttons.get() == "weighted":
            total_weighted_percentages = sum([a.weighted_percentage() for a in Info.assignment_panes])
            total_weights = sum([a.weight() for a in Info.assignment_panes])
            grade_string = "%" + str(round(total_weighted_percentages / total_weights * 100, 2))
            hotbar.grade_label.config(text=grade_string)
    except Exception:
        Error_Popup("Please make sure all values are positive.")


def clear_grade():
    hotbar.grade_label.config(text="")

def move_down(assignment_pane):
    Info.assignment_panes.remove(assignment_pane)
    Info.assignment_panes.append(assignment_pane)
    update()

# Frame Creation
frame = Tk()
frame.title("Grade Calculator")

# Hotbar Creation
hotbar = Hotbar(frame, update, calculate_grade)
hotbar.pane.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Plusbar Creation
plusbar = Plusbar(frame, create_assignment_pane)
plusbar.pane.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# First Assignment Creation
create_assignment_pane()

# Mainloop
frame.mainloop()
