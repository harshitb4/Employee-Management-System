import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
from customtkinter import CTkButton
import re


conn = sqlite3.connect("employee.db")
cursor = conn.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS employee (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT,
                    contact INTEGER
                )
                ''' )

conn.commit()

# to insert a record
def insert_record():
    insert_window = tk.Toplevel(window)
    insert_window.title('Insert Record')
    insert_window.geometry("500x500")
    
    id_label = tk.Label(insert_window, text="id:")
    id_label.pack()
    id_entry = tk.Entry(insert_window,width=30)
    id_entry.pack()

    gap_label = tk.Label(insert_window, text="", height=1)  # Adjust the height to control the size of the gap
    gap_label.pack()

    first_name_label = tk.Label(insert_window, text="first_name:")
    first_name_label.pack()
    first_name_entry = tk.Entry(insert_window,width=30)
    first_name_entry.pack()

    gap_label = tk.Label(insert_window, text="", height=1)  # Adjust the height to control the size of the gap
    gap_label.pack()

    last_name_label = tk.Label(insert_window, text="last_name:")
    last_name_label.pack()
    last_name_entry = tk.Entry(insert_window,width=30)
    last_name_entry.pack()

    gap_label = tk.Label(insert_window, text="", height=1)  # Adjust the height to control the size of the gap
    gap_label.pack()

    email_label = tk.Label(insert_window, text="email:")
    email_label.pack()
    email_entry = tk.Entry(insert_window,width=30)
    email_entry.pack()

    gap_label = tk.Label(insert_window, text="", height=1)  # Adjust the height to control the size of the gap
    gap_label.pack()

    contact_label = tk.Label(insert_window, text="contact:")
    contact_label.pack()
    contact_entry = tk.Entry(insert_window,width=30)
    contact_entry.pack()

    gap_label = tk.Label(insert_window, text="", height=1)  # Adjust the height to control the size of the gap
    gap_label.pack()
    
    def insert_data():
        id = id_entry.get()
        if not id.isdigit():
            messagebox.showinfo("Failed", "id should be numeric only")
            return
        first_name = first_name_entry.get()
        if not (re.match(r'^[a-zA-Z.]+$',first_name)):
            messagebox.showinfo("Failed", "Invalid first_name")
            return
        last_name = last_name_entry.get()
        if not (re.match(r'^[a-zA-Z.]+$',last_name)):
            messagebox.showinfo("Failed", "Invalid last_name")
            return
        email = email_entry.get()
        if not (email.__contains__('@') and email[-4:].__contains__('.com')):
            messagebox.showinfo("Failed", "Invalid e-mail")
            return
        contact = contact_entry.get()
        if not (id.isdigit() and len(contact)==10):
            messagebox.showinfo("Failed", "Invalid contact number")
            return
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employee (id, first_name, last_name, email, contact) VALUES (?,?,?,?,?)", (id,first_name,last_name,email,contact))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Success", "Records inserted successfully")
        
    insert_button = tk.Button(insert_window, text = "Insert", command = insert_data,padx=25,pady=6,bg="black",fg="white",borderwidth=0, highlightthickness=0)
    insert_button.pack()
            
# to delete record
def delete_record():
    
    delete_window = tk.Toplevel(window)
    delete_window.title('Delete Record')
    delete_window.geometry("500x500")
    
    id_label = tk.Label(delete_window, text= "Employee ID:")
    id_label.pack()
    id_entry = tk.Entry(delete_window)
    id_entry.pack()
    
    def delete_data():
        record_id = id_entry.get()
        if not record_id:
            messagebox.showerror("Error", "please enter employee id")
            return
        
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employee WHERE id=?", (record_id,))
        print("Record does not exists")
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Records deleted successfully")

    gap_label = tk.Label(delete_window, text="", height=1)  # Adjust the height to control the size of the gap
    gap_label.pack()    
    delete_button = tk.Button(delete_window, text="Delete", command=delete_data,bg="black",fg="white",borderwidth=0, highlightthickness=0)
    delete_button.pack()
    
# to show records    
def show_records():
    records_window = tk.Toplevel(window)
    records_window.title("Records")
    records_window.geometry("1500x500")
    
    text_widget = tk.Text(records_window, height=100, width=100)
    text_widget.pack()
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    records = cursor.fetchall()
    conn.commit()
    conn.close()
    for record in records:
        text_widget.insert(tk.END, f"ID: {record[0]}, Fisrt_name: {record[1]}, Last_name: {record[2]}, Email: {record[3]}, Contact: {record[4]}" + "\n")
    
    
window=tk.Tk()
window.title("employee data")
window.geometry("500x500")


#insert button
gap_label = tk.Label(window, text="", height=4)  # Adjust the height to control the size of the gap
gap_label.pack()
custom_font = ("Helvetica", 22)
insert_button = tk.Button(window, text = "Insert Record", command = insert_record,font=custom_font,padx=6,pady=6,bg="black", fg="white",borderwidth=0, highlightthickness=0)
initial_width = insert_button.winfo_width()
new_width = initial_width + 20
insert_button.config(width=new_width)
insert_button.pack()

#delete button
gap_label = tk.Label(window, text="", height=4)  # Adjust the height to control the size of the gap
gap_label.pack()
custom_font = ("Helvetica", 22)
delete_button = tk.Button(window, text = "Delete Record", command = delete_record,font=custom_font,padx=6,pady=6,bg="black", fg="white",borderwidth=0, highlightthickness=0)
initial_width = delete_button.winfo_width()
new_width = initial_width + 20
delete_button.config(width=new_width)
delete_button.pack()

#submit button
gap_label = tk.Label(window, text="", height=4)  # Adjust the height to control the size of the gap
gap_label.pack()
custom_font = ("Helvetica", 22)
show_button = tk.Button(window, text = "Show Records", command = show_records,font=custom_font,padx=6,pady=6,bg="black", fg="white",borderwidth=0, highlightthickness=0)
initial_width = show_button.winfo_width()
new_width = initial_width + 20
show_button.config(width=new_width)
show_button.pack()

window.mainloop()
conn.close()



