from panes import *



def create_assignment():
    assignments.append(Assignment(frame, remove_assignment))
    update()

def remove_assignment(assignment):
    if len(assignments) < 2:
        return
    assignment.pane.destroy()
    assignments.pop(assignments.index(assignment))
    update()

def update():
    update_weighting()
    clear_grade()

    #cycles through all of the panes
    for i in range(len(assignments)):
        assignments[i].pane.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
    plusbar.pane.grid(row=len(assignments) + 2)

def update_weighting():
    if hotbar.weighting_buttons.get() == "points":
        for assignment in assignments:
            assignment.weight_entry.config(state="disabled")
    if hotbar.weighting_buttons.get() == "weighted":
        for assignment in assignments:
            assignment.weight_entry.config(state="normal")

def calculate_grade():
    try:
        if hotbar.weighting_buttons.get() == "points":
            points_earned = sum([a.earned() for a in assignments])
            points_possible = sum([a.possible() for a in assignments])
            grade_string = "%" + str(round(points_earned/points_possible*100, 2))
            hotbar.grade_label.config(text=grade_string)
        if hotbar.weighting_buttons.get() == "weighted":
            total_weighted_percentages = sum([a.weighted_percentage() for a in assignments])
            total_weights = sum([a.weight() for a in assignments])
            grade_string = "%" + str(round(total_weighted_percentages/total_weights*100, 2))
            hotbar.grade_label.config(text=grade_string)
    except Exception:
        popup("Error", "Please make sure all values are positive.")

def clear_grade():
    hotbar.grade_label.config(text="")

def popup(title, message):
    popup = Tk()
    popup.title(title)
    popup_label = Label(popup, text=message)
    popup_label.grid(row=0, padx=10, pady=25)
    popup_button = Button(popup, text=" OK ", command=popup.destroy)
    popup_button.grid(row=2, pady=5)
    popup.mainloop()



#Assignments List
assignments = []

#Frame Creation
frame = Tk()
frame.title("Grade Calculator")

#Hotbar Creation
hotbar = Hotbar(frame, update, calculate_grade)
hotbar.pane.grid(row=0, column=0, padx=10, pady=5, sticky="w")

#Plusbar Creation
plusbar = Plusbar(frame, create_assignment)
plusbar.pane.grid(row=2, column=0, padx=10, pady=5, sticky="w")

#First Assignment Creation
create_assignment()

#Mainloop
frame.mainloop()