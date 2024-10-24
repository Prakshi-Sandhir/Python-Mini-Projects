import tkinter as tk

window = tk.Tk()
window.title("TO DO LIST!📝")
window.geometry("1000x900") 

window.configure(bg="#FCF7FF")

label = tk.Label(window, text="TO DO LIST!📝", font=("Britannic Bold", 25), bg="#FCF7FF")
label.pack(padx=20, pady=20)

frame = tk.Frame(window, padx=10, pady=10, bg="#FCF7FF")
frame.pack(padx=10, pady=10) 

tk.Label(frame, text="Enter Your Tasks: ", font=("Britannic Bold", 20), bg="#FCF7FF").grid(row=0, column=0, padx=10, pady=10, sticky="w")

name_entry = tk.Text(frame, width=35, height=2)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

tasks_frame = tk.Frame(window, bg="#C4CAD0", width=500, height=500)
tasks_frame.pack(padx=10, pady=10) 
tasks_frame.pack_propagate(False)  

task_number = 0

def add_task():
    global task_number

    task = name_entry.get("1.0", tk.END).strip()  
    
    if not task:
        return
    
    task_frame = tk.Frame(tasks_frame, bg="#C4CAD0")
    task_frame.pack(fill="x", pady=5)  

    task_label = tk.Label(task_frame, text=task, font=("Britannic Bold", 15), bg="#C4CAD0")
    task_label.pack(side="right", padx=5)

    delete_button = tk.Button(task_frame, text="Remove", command=lambda: task_frame.destroy())
    delete_button.pack(side="left", padx=5)  

    task_number += 1
    name_entry.delete("1.0", tk.END)


add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()
