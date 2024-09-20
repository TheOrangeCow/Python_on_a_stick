import tkinter as tk
from tkinter import filedialog
import os
import subprocess

# Function to run a file
def runfile(file):
    root.destroy()
    os.system(file)


def run_script(filename):
    command = f'call %cd%\\venv\\Scripts\\activate && python {filename}'
    subprocess.run(command, shell=True)

def browse():
    filename = filedialog.askopenfilename()
    if filename:
        if not ' ' in filename:
            root.destroy()
            run_script(filename)
        else:
            error.config(text="Please remove the spaces in the name")
    else:
        error.config(text="Error finding the file")


root = tk.Tk()
root.title("Python on a Stick")
root.config(bg = "black")


title_font = ("Helvetica", 24, "bold")
button_font = ("Helvetica", 14, "bold")


title = tk.Label(root, text="Python on a Stick", font=title_font, fg="white", bg ="black")
title.pack(pady=20)


error = tk.Label(root, text="", font=("Helvetica", 12), fg="red", bg = "black")
error.pack(pady=10)


cmd = tk.Button(root, text="Open Command Prompt", font=button_font, command=lambda: runfile("cmd_venv.bat"), bg="green", fg="white")
cmd.pack(pady=10)


idle = tk.Button(root, text="Open IDLE", font=button_font, command=lambda: runfile("idle_run.bat"), bg="orange", fg="white")
idle.pack(pady=10)


browse_btn = tk.Button(root, text="Run a File", font=button_font, command=browse, bg="purple", fg="white")
browse_btn.pack(pady=10)


example = tk.Button(root, text="Run an Example", font=button_font, command=lambda: runfile("tetrers.py"), bg="brown", fg="white")
example.pack(pady=10)

root.mainloop()
