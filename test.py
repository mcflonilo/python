import tkinter as tk
import subprocess
import os
def ping():
    os.popen('ping -n 1 ' + 'www.google.com')

def run_command(command):
    subprocess.run(command, shell=True)

def create_button(root, text, command):
    button = tk.Button(root, text=text, command=lambda: run_command(command))
    button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Command Runner")

    # Create buttons
    create_button(root, "Button 1", "ping www.google.com")
    create_button(root, "Button 2", "python script2.py")
    create_button(root, "Button 3", "python script3.py")

    root.mainloop()