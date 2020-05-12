from tkinter import *



def create_top_pane():
    pane = PanedWindow(frame)
    pane.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    name_label = Label(pane, text="Class:")
    name_label.grid(row=0, column=0, padx=0, pady=0)
    name_entry = Entry(pane, width=10)
    name_entry.grid(row=0, column=1, padx=0, pady=0)
    calculate_grade_button = Button(pane, text="Calculate Grade")
    calculate_grade_button.grid(row=0, column=3, padx=0, pady=0)
    grade_label = Label(pane, text="Grade:")
    grade_label.grid(row=0, column=4, padx=0, pady=0)
    return (pane, name_label, name_entry, calculate_grade_button, grade_label)

def create_bottom_pane():
    pane = PanedWindow(frame)
    pane.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    plus_button = Button(pane, text=" + ", command=create_assignment_pane)
    plus_button.grid(row=0, column=0, padx=0, pady=0)
    return(pane, plus_button)

def create_assignment_pane():
    pane = PanedWindow(frame)
    minus_button = Button(pane, text=" - ", command=lambda: remove_assignment(minus_button))
    minus_button.grid(row=0, column=0, padx=0, pady=0)
    name_label = Label(pane, text="Assignment:")
    name_label.grid(row=0, column=1, padx=0, pady=0)
    name_entry = Entry(pane, width=20)
    name_entry.grid(row=0, column=2, padx=0, pady=0)
    grade_label = Label(pane, text="Grade:")
    grade_label.grid(row=0, column=3, padx=0, pady=0)
    score_entry = Entry(pane, width=4)
    score_entry.grid(row=0, column=4, padx=0, pady=0)
    divide_label = Label(pane, text="/")
    divide_label.grid(row=0, column=5, padx=0, pady=0)
    points_entry = Entry(pane, width=4)
    points_entry.grid(row=0, column=6, padx=0, pady=0)
    weight_label = Label(pane, text="Weight:")
    weight_label.grid(row=0, column=7, padx=0, pady=0)
    weight_entry = Entry(pane, width=4)
    weight_entry.grid(row=0, column=8, padx=0, pady=0)
    assignment_panes.append((pane, minus_button, name_label, name_entry, grade_label, score_entry, divide_label, points_entry, weight_label, weight_entry))
    update()

def remove_assignment(minus_button):
    minus_button.master.destroy()
    minus_button_index = [t[1] for t in assignment_panes].index(minus_button)
    assignment_panes.pop(minus_button_index)
    update()

def update():
    #cycles through all of the panes
    for i in range(len(assignment_panes)):
        assignment_panes[i][0].grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
    bottom_pane[0].grid(row=len(assignment_panes) + 2)



#Frame Creation
frame = Tk()
frame.title("Grade Calculator")

#Pane Creation
top_pane = create_top_pane()
assignment_panes = []
bottom_pane = create_bottom_pane()

#Mainloop
frame.mainloop()