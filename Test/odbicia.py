import tkinter as tk;
from tkinter import ttk;
from tkinter.messagebox import showinfo;
import socket;


root = tk.Tk()

def quit():
    root.quit()

def do_something():
    print("Hello World")

def download():
    showinfo(title = "Download", message = "Downloading...")


def the_funny():
    hostname = socket.gethostname()
    number = socket.gethostbyname(hostname)
    showinfo(title = "The funny", message = "To ty? " + number)


download_icon = tk.PhotoImage(file = "print.png", width = 55, height = 55)




root.geometry("500x500")
root.title("Hello World")

label = ttk.Label(root, text="Hello World", font=("Arial", 20, "bold"))  
label.pack(padx=20, pady=20)

button = ttk.Button(root, text="Uga buga", command=quit)
button.pack(padx=15, pady=10)

button2 = ttk.Button(root, text="Buga uga", command=do_something)
button2.pack(padx=15, pady=10)

button3 = ttk.Button(root, image=download_icon , command=download)
button3.pack(ipadx=10, ipady=10, expand=True)

button3 = ttk.Button(root,text="Download" ,compound=tk.LEFT , image=download_icon , command=download)
button3.pack(ipadx=10, ipady=10, expand=True)

button4 = ttk.Button(root, text="The funny", command=the_funny)
button4.pack(ipadx=10, ipady=10, expand=True)




root.mainloop()
