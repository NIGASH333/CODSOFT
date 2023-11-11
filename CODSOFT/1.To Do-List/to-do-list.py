import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if not task_string:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    confirm_delete = messagebox.askyesno('Delete All', 'Are you sure?')
    if confirm_delete:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager - NIGASH")
    guiWindow.geometry("800x600+500+150")  # Changed the size to 800x600
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="yellow")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="yellow")
    functions_frame = tk.Frame(guiWindow, bg="yellow")
    listbox_frame = tk.Frame(guiWindow, bg="yellow")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Algerian", "30"),
        background="yellow",
        foreground="blue"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Castellar", "11", "bold"),
        background="yellow",
        foreground="#000000"
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Consolas", "12"),
        width=30,  # Adjusted width
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=30,  # Adjusted width
        command=add_task,
        style="TButton"
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=30,  # Adjusted width
        command=delete_task,
        style="TButton"
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=30,  # Adjusted width
        command=delete_all_tasks,
        style="TButton"
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=30,  # Adjusted width
        command=close,
        style="TButton"
    )
    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=50,  # Adjusted width
        height=20,  # Adjusted height
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
