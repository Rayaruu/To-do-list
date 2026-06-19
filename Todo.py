import tkinter as tk
import json
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry("400x500")
root.title("To-Do List")
task_list = []

img = Image.open("gingham.jpg")
img = img.resize((400, 500))   
header_image = ImageTk.PhotoImage(img)

background_label = tk.Label(root, image=header_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


Entry=tk.Entry(root, width=40,)
Entry.pack(pady=10)

def add_task(event=None):
    task=Entry.get()
    task_list.append({"text": task, "done": False})
    for task in task_list:
        row=tk.Checkbutton(tasks_frame, text=task["text"],command=lambda t=task: mark_done(t))
        row.pack()
    Entry.delete(0, tk.END)
    print(task_list)
    refresh_display()
    save_tasks()  # Save tasks whenever a new task is added

 
Entry.bind("<Return>", add_task)  # Bind the Enter key to the add_task function

my_button=tk.Button(root, text="Add Task", command=add_task)
my_button.pack(pady=10)

tasks_frame=tk.Frame(root)
tasks_frame.pack(pady=10)

def refresh_display():
    for widget in tasks_frame.winfo_children():
        widget.destroy()
    for task in task_list:
        var=tk.BooleanVar(value=task["done"])
        task["var"] = var
        row= tk.Checkbutton(tasks_frame, text=task["text"], variable=var, command=lambda t=task: mark_done(t))
        row.pack()
        delete_button = tk.Button(tasks_frame, text="Delete", command=lambda t=task: delete_task(t))
        delete_button.pack()

def mark_done(task):
    task["done"] = not task["done"]
    refresh_display()
    save_tasks()  
def delete_task(task):
    task_list.remove(task)
    refresh_display()
    save_tasks() 

def save_tasks():
    data_to_save = [] 

    for task in task_list:
        
        data_to_save.append({"text": task["text"], "done": task["done"]})

    # write that list to a file as JSON
    with open("tasks.json", "w") as f:
        json.dump(data_to_save, f)
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            loaded_data = json.load(f)
            for task in loaded_data:
                task_list.append(task)
    except FileNotFoundError:
        pass  

load_tasks()  
refresh_display()  
root.mainloop()