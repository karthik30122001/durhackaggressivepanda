import tkinter as tk
from tkinter import ttk


from tkinter import filedialog
log_lines= []
log_data =[]
# def open_file_dialog():
#     file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
#     if file_path:
#         open_file(file_path)

def open_file():
    global log_data
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.log")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                log_data = file.readlines()
                ref_loglines(log_data)
                
        except Exception as e:
            
            print(f"Error opening file: {e}")


def filter_logs():
    # Implement log filtering logic here
    pass

# Create the main window
root = tk.Tk()
root.title("Log Viewer")

# Create a frame for the scrollable log display
log_frame = tk.Frame(root)
log_frame.pack(side="left", padx=10, pady=10)

# Create a canvas to make the log frame scrollable
canvas = tk.Canvas(log_frame)
canvas.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to hold the log content
log_content = tk.Frame(canvas)
canvas.create_window((0, 0), window=log_content, anchor="nw")

# Create buttons for opening files
open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack()

# Create radio buttons for log type filtering
log_type_var = tk.StringVar()
log_type_var.set("All")  # Default selection
filter_label = tk.Label(root, text="Filter by Log Type:")
filter_label.pack()
all_radio = tk.Radiobutton(root, text="All", variable=log_type_var, value="All", command=filter_logs)
all_radio.pack()
info_radio = tk.Radiobutton(root, text="Info", variable=log_type_var, value="Info", command=filter_logs)
info_radio.pack()
error_radio = tk.Radiobutton(root, text="Error", variable=log_type_var, value="Error", command=filter_logs)
error_radio.pack()
warning_radio = tk.Radiobutton(root, text="Warning", variable=log_type_var, value="Warning", command=filter_logs)
warning_radio.pack()

# Create text fields
text_field1 = tk.Entry(root, width=50)
text_field1.pack()
text_field2 = tk.Entry(root, width=50)
text_field2.pack()

# Example log data
log_data = [
    "Info: This is an informational log entry",
    "Error: Something went wrong",
    "Info: Another informational log",
    "Warning: Be cautious",
    "Error: Critical error occurred",
]

# Display example log data in the scrollable frame
def ref_loglines(log_data):
    for log_entry in log_data:
        log_label = tk.Label(log_content, text=log_entry, wraplength=400)
        log_label.pack(anchor="w")

# Update the canvas scroll region
    log_content.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()