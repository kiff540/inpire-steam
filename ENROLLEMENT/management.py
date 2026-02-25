import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Functions ---
def enroll_student():
    """Fetches data from entry fields and adds it to the display table."""
    s_num = entry_num.get()
    s_name = entry_name.get()
    c_id = entry_course.get()
    
    # Basic validation to ensure fields aren't empty
    if not s_num or not s_name or not c_id:
        messagebox.showwarning("Input Error", "Please fill in all fields before enrolling.")
        return
        
    # Insert the data into the Treeview (Table)
    table.insert("", tk.END, values=(s_num, s_name, c_id))
    
    # Clear the entry fields after successful enrollment
    entry_num.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    
    # Optional success message
    messagebox.showinfo("Success", f"Student {s_name} enrolled successfully!")

# --- Main Window Setup ---
root = tk.Tk()
root.title("School Management System - Enrollment")
root.geometry("550x450")
root.configure(padx=20, pady=20)

# ==========================================
# FRAME 1: Data Entry Form
# ==========================================
frame_input = tk.Frame(root, relief=tk.GROOVE, borderwidth=2, padx=15, pady=15)
frame_input.pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

# Title for the input frame
tk.Label(frame_input, text="Enroll a New Student", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Student Number
tk.Label(frame_input, text="Student Number:").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_num = tk.Entry(frame_input, width=30)
entry_num.grid(row=1, column=1, pady=5, padx=10)

# Student Name
tk.Label(frame_input, text="Student Name:").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_name = tk.Entry(frame_input, width=30)
entry_name.grid(row=2, column=1, pady=5, padx=10)

# Course ID
tk.Label(frame_input, text="Course ID:").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_course = tk.Entry(frame_input, width=30)
entry_course.grid(row=3, column=1, pady=5, padx=10)

# Enroll Button
btn_enroll = tk.Button(frame_input, text="Enroll Student", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=enroll_student)
btn_enroll.grid(row=4, column=0, columnspan=2, pady=(15, 0), ipadx=10, ipady=5)


# ==========================================
# FRAME 2: Display Table
# ==========================================
frame_display = tk.Frame(root)
frame_display.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Define columns for the Treeview
columns = ("Student Number", "Student Name", "Course ID")
table = ttk.Treeview(frame_display, columns=columns, show="headings")

# Define column headings
for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor=tk.CENTER, width=150)

# Add a scrollbar to the table
scrollbar = ttk.Scrollbar(frame_display, orient=tk.VERTICAL, command=table.yview)
table.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()