import tkinter
import tkinter.messagebox


# Function to clear all tasks in the TODO-LIST
def clear_listbox():
    Tasks.delete(0, "end")

# Function to update the TODO-LIST with the remaining tasks
def update_remaining_tasks():
    clear_listbox()
    for task in data:
        Tasks.insert('end', task)
    numtask = len(data)
    display_count_remaining['text'] = f'REMAINING TASK: {numtask}'

# Function to add a task to the TODO-LIST
def add():
    task = Type.get()
    if task != '':
        data.append(task)
        update_remaining_tasks()

    else:
        tkinter.messagebox.showwarning(
            title="Warning!", message="A task must be entered")

    Type.delete(0, tkinter.END)

# Function to delete a selected task from the TODO-LIST
def delete():
    try:
        task_index = Tasks.curselection()[0]
        de = Tasks.get('active')

        if de in data:
            data.remove(de)
            Tasks.delete(task_index)
        update_remaining_tasks()

    except:
        tkinter.messagebox.showwarning(
            title="Warning!", message="A task must be selected")

# Function to delete all tasks from the TODO-LIST
def delete_all():
    del_all = Tasks.get('active')
    if del_all != '':
        conf = tkinter.messagebox.askquestion(
            'Delete all??', 'Are you sure to delete all task?')
        if conf.upper() == "YES":
            Complete.delete(0, 'end')
            global data
            data = []
            update_remaining_tasks()

    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Empty List")

# Function to mark a selected task as done
def mark():
    try:
        task_index = Tasks.curselection()[0]
        mark1 = Tasks.get('active')
        if mark1 in data:
            Complete.insert('end', mark1)
            data.remove(mark1)
        update_remaining_tasks()

    except:
        tkinter.messagebox.showwarning(
            title="Warning!", message="A task must be selected")

# Function to unmark a selected task as done
def unmark():
    try:
        task_index = Complete.curselection()[0]
        unmark1 = Complete.get('active')
        if unmark1 not in data:
            data.append(unmark1)
            Complete.delete(task_index)
        update_remaining_tasks()

    except:
        tkinter.messagebox.showwarning(
            title="Warning!", message="A task must be selected")

# Function to save the tasks to a file
def save():
    if data==[]:
        tkinter.messagebox.showwarning(title="Warning!", message="Empty List")
    else:
        with open('file.txt', 'w') as f:
            for listitem in data:
                f.write(f'{listitem}') 
                if  listitem not in data[-1]:
                        f.write('\n')  
        tkinter.messagebox.showinfo(
            'Task save confirmation', 'Your task saved successfully')
    update_remaining_tasks()

# Function to load tasks from a file
def load():
    if data==[]:
        with open('file.txt', 'r') as filereader:
            for currentask in filereader:
                currentask=currentask.strip()
                data.append(currentask)
            
    else:
        loadcon= tkinter.messagebox.askquestion(
    'Loading  Confirmation', 'Are you sure you want to delete your current adding tasks from the list?')
        if loadcon.upper() == "YES":
            data.clear()
            with open('file.txt', 'r') as filereader:
                for currentask in filereader:
                   currentask=currentask.strip()
                   data.append(currentask)
                
    update_remaining_tasks()

# Function to sort the tasks in ascending order
def ascending():
    if data == []:
        tkinter.messagebox.showwarning('Warning!', 'Empty List')
    else:
        data.sort()
        update_remaining_tasks()

# Function to sort the tasks in descending order
def descending():
    if data == []:
        tkinter.messagebox.showwarning('Warning!', 'Empty List')
    else:
        data.sort(reverse=True)
        update_remaining_tasks()

# Function to show information about the app
def info():
    tkinter.messagebox.showinfo(
        "info", "THIS IS TODO-LIST APP\n\nCREATED BY GOURAB ROY\n\nPYTHON PROJECT")

# Function to exit the application
def Exit():
    conf = tkinter.messagebox.askquestion(
        'Quit Confirmation', 'Are you sue you want to quit?')
    if conf.upper() == "YES":
        root.destroy()

# Main application window
root = tkinter.Tk()
root.title("To-Do List")
root.geometry("1280x700")
root.resizable(False, False)
img = tkinter.PhotoImage(file="Background.png")
label = tkinter.Label(root, image=img)
label.place(x=0, y=0)
root.wm_iconbitmap("favicon.ico")

# database
data = []

# Frames
SPACE = tkinter.Frame(root)
SPACE.place(x=475, y=300)
Buttons = tkinter.Frame(root)
Buttons.place(x=50, y=200)
Tabs = tkinter.Frame(root)
Tabs.place(x=730, y=10)

# Entry
Type = tkinter.Entry(Buttons, width=52, bg='black',fg='white', font="sans-serif 11 bold")
Type.pack(fill=tkinter.Y, ipady=10)

# Listbox
Tasks = tkinter.Listbox(Tabs, height=20, width=65,bg="#FFD700", fg="black", font="sans-serif 11 bold")
Tasks.pack()
Complete = tkinter.Listbox(Tabs, height=15, width=65, bg="#3f000f", fg="white", font="sans-serif 11 bold")
Complete.pack()


# counter
display_count_remaining = tkinter.Label(SPACE, text='REMAINING TASK', width=31, bg="#DC143C", fg="white", relief=tkinter.RIDGE, font='sans-serif 10 bold')
display_count_remaining.pack()


# buttons
add_task_button = tkinter.Button(Buttons, text='ADD TASK', width=45, command=add, bg="#E91E63", fg="white", font="sans-serif 11 bold")
add_task_button.pack()

delete_task_button = tkinter.Button(Buttons, text='DELETE TASK', width=45, command=delete, bg="#E91E63", fg="white", font="sans-serif 11 bold")
delete_task_button.pack()

delete_all_task_button = tkinter.Button(Buttons, text='DELETE ALL TASK', width=45, command=delete_all, bg="#E91E63", fg="white", font="sans-serif 11 bold")
delete_all_task_button.pack()

Save_task_button = tkinter.Button(Buttons, text='SAVE TASK', width=45, command=save, bg="#E91E63", fg="white", font="sans-serif 11 bold")
Save_task_button.pack()

Load_task_button = tkinter.Button(Buttons, text='LOAD ALL TASK', width=45,  command=load, bg="#E91E63", fg="white", font="sans-serif 11 bold")
Load_task_button.pack()

Mark_as_done_button = tkinter.Button(Buttons, text='MARK THE TASK AS DONE', width=45, command=mark, bg="#E91E63", fg="white", font="sans-serif 11 bold")
Mark_as_done_button.pack()

Mark_as_undone_button = tkinter.Button(Buttons, text='MARK THE TASK AS UNDONE', width=45, command=unmark, bg="#E91E63", fg="white", font="sans-serif 11 bold")
Mark_as_undone_button.pack()


Exit_button = tkinter.Button(Buttons, text='EXIT', width=45, command=Exit, bg="#E91E63", fg="white", font="sans-serif 11 bold")
Exit_button.pack()

Aorder_button = tkinter.Button(SPACE, text='ARRANGE IN ASCENDING ORDER', width=30, command=ascending, bg="#4CAF50", fg="white", font='sans-serif 10 bold')
Aorder_button.pack()

Dorder_button = tkinter.Button(SPACE, text='ARRANGE IN DESCENDING ORDER', width=30, command=descending, bg="#4CAF50", fg="white", font='sans-serif 10 bold')
Dorder_button.pack()

info_button = tkinter.Button(SPACE, text='INFO', width=30, command=info, bg="#4CAF50", fg="white", font='sans-serif 10 bold')
info_button.pack()

# Run the TODO-LIST application  
root.mainloop()
