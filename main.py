from tkinter import *



def create_top_pane():
    pane = PanedWindow(frame)
    pane.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    name_label = Label(pane, text="Class:")
    name_label.grid(row=0, column=0, padx=0, pady=0)
    name_entry = Entry(pane, width=10)
    name_entry.grid(row=0, column=1, padx=0, pady=0)
    weighting_buttons = StringVar()
    points_button = Radiobutton(pane, text="Points", variable=weighting_buttons, value="points", command=update)
    weighted_button = Radiobutton(pane, text="Weighted", variable=weighting_buttons, value="weighted", command=update)
    points_button.grid(row=0, column=2, padx=0, pady=0)
    weighted_button.grid(row=0, column=3, padx=0, pady=0)
    points_button.select()
    calculate_grade_button = Button(pane, text="Calculate Grade", command=calculate_grade)
    calculate_grade_button.grid(row=0, column=4, padx=0, pady=0)
    grade_label = Label(pane, text="Grade:")
    grade_label.grid(row=0, column=5, padx=0, pady=0)
    return (pane, name_entry, weighting_buttons, calculate_grade_button, grade_label)

def create_bottom_pane():
    pane = PanedWindow(frame)
    pane.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    plus_button = Button(pane, text=" + ", command=create_assignment_pane)
    plus_button.grid(row=0, column=0, padx=0, pady=0)
    return (pane, plus_button)

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
    score_entry.insert(0, "0")
    score_entry.grid(row=0, column=4, padx=0, pady=0)
    divide_label = Label(pane, text="/")
    divide_label.grid(row=0, column=5, padx=0, pady=0)
    points_entry = Entry(pane, width=4)
    points_entry.insert(0, "100")
    points_entry.grid(row=0, column=6, padx=0, pady=0)
    weight_label = Label(pane, text="Weight:")
    weight_label.grid(row=0, column=7, padx=0, pady=0)
    weight_entry = Entry(pane, width=4)
    weight_entry.insert(0, "1")
    weight_entry.grid(row=0, column=8, padx=0, pady=0)
    assignment_panes.append((pane, minus_button, name_entry, score_entry, points_entry, weight_entry))
    update()

def remove_assignment(minus_button):
    if len(assignment_panes) < 2:
        return

    minus_button.master.destroy()
    minus_button_index = [t[1] for t in assignment_panes].index(minus_button)
    assignment_panes.pop(minus_button_index)
    update()

def update():
    update_weighting()
    clear_grade()

    #cycles through all of the panes
    for i in range(len(assignment_panes)):
        assignment_panes[i][0].grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
    bottom_pane[0].grid(row=len(assignment_panes) + 2)

def update_weighting():
    if top_pane[2].get() == "points":
        for pane_tuple in assignment_panes:
            pane_tuple[5].config(state="disabled")
    if top_pane[2].get() == "weighted":
        for pane_tuple in assignment_panes:
            pane_tuple[5].config(state="normal")

def calculate_grade():
    try:
        if top_pane[2].get() == "points":
            points_earned = sum([int(t[3].get()) for t in assignment_panes])
            points_possible = sum([int(t[4].get()) for t in assignment_panes])
            grade_string = "%" + str(round(points_earned/points_possible*100, 2))
            top_pane[4].config(text=grade_string)
        if top_pane[2].get() == "weighted":
            total_percentages = sum([int(t[3].get()) / int(t[4].get()) * int(t[5].get()) for t in assignment_panes])
            total_weights = sum([int(t[5].get()) for t in assignment_panes])
            grade_string = "%" + str(round(total_percentages/total_weights*100, 2))
            top_pane[4].config(text=grade_string)
    except Exception:
        popup("Error", "Please make sure all values are positive.")

def clear_grade():
    top_pane[4].config(text="")

def popup(title, message):
    popup = Tk()
    popup.title(title)
    popup_label = Label(popup, text=message)
    popup_label.grid(row=0, padx=10, pady=25)
    popup_button = Button(popup, text=" OK ", command=popup.destroy)
    popup_button.grid(row=2, pady=5)
    popup.mainloop()



#Frame Creation
frame = Tk()
frame.title("Grade Calculator")

#Pane Creation
top_pane = create_top_pane()
assignment_panes = []
bottom_pane = create_bottom_pane()

#create the first pane
create_assignment_pane()

#Mainloop
frame.mainloop()