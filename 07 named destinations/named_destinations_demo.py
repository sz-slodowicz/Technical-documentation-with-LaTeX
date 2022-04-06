import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import subprocess

#define the root
window = tk.Tk()
window.title("Named destinations demo")
window.resizable(False, False)

#define the function for opening pdf at a named destination
def open_pdf_at_nameddest(file, nameddest):
    subprocess.Popen([r"C:\\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe", "/A", "nameddest="+nameddest, file],shell=True)

#define the close window
close_button = tk.Button(master=window, text="Close", font=("Arial", 12) , command=lambda: window.quit())
close_button.grid(row=1,column=1, sticky=tk.N+tk.S+tk.W+tk.E)

#define the help button
help_button = tk.Button(master=window, text="Help", font=("Arial", 12),command= lambda: open_pdf_at_nameddest(r"C:\Users\z00425de\Dropbox\Python\TkInter\named_destinations_latex.pdf", "key_and_token"))
help_button.grid(row=1, column=0, sticky=tk.N+tk.S+tk.W+tk.E)


#define the left frame with a label and entry field
left_frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1, padx=5, pady=20)
left_frame.grid(row=0, column=0, padx=5, pady=5)
enter_key_label = tk.Label(master=left_frame, text="Enter key:", font=("Arial", 12))
key = tk.StringVar()
enter_key_entry = tk.Entry(master=left_frame, textvariable=key, width=20)
enter_key_entry.grid(row=0, column=1, sticky=tk.N+tk.S+tk.W+tk.E)
enter_key_label.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)

#define the left frame with a label, entry field
right_frame = tk.Frame(master=window,relief=tk.RAISED, borderwidth=1, padx=5, pady=20)
right_frame.grid(row=0, column=1, padx=5, pady=5)
token = tk.StringVar()
token_label = tk.Label(master=right_frame, text="Enter token:", font=("Arial", 12))
enter_token_entry = tk.Entry(master=right_frame, textvariable=token, width=20)
enter_token_entry.grid(row=0, column=1, sticky=tk.N+tk.S+tk.W+tk.E)
token_label.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)


window.mainloop()

#print(password.get())