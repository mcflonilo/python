import tkinter as tk
import subprocess
import os
import volatility3
def volatility(file):
    os.popen('python3 vol.py -f '+file+' windows.info')

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
    create_button(root, "Button 2", "python3 vol.py -f '+file+' windows.info")
    create_button(root, "Button 3", "python script3.py")

    root.mainloop()