#Muzzamil
#This program is so we know what items are hired out
from tkinter import Tk
from tkinter import *
import tkinter as tk
from tkinter import ttk

#Main page
root=tk.Tk()
root.title("Julie's Party Hire")
root.geometry("800x600")
root.configure(bg='cadet blue')

#Logo
logo_image=tk.PhotoImage(file='Julies_Party_Hire.png')
logo_button=tk.Button(root, image=logo_image, height=70, width=120).grid(row=0, column=0)

#Title
title_label=tk.Label(root, text='Julies Party Hire', font=('Helvetica', 45), fg='black', bg='cadet blue')
title_label.grid(row=0, column=1)




mainloop()