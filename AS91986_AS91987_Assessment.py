#Muzzamil
#This program is for julies party hire



from tkinter import *
import tkinter as tk

#main window
root=Tk()
root.title("Julie's Party Hire")
root.geometry("1000x400")
root.configure(bg='cadet blue')

#title julies party hire
title_label=tk.Label(root, text='Julies Party Hire', font=('Helvetica', 45), fg='black', bg='cadet blue')
title_label.grid(row=0, column=1, sticky='w')

#add logo for julies party hire
logo_image=tk.PhotoImage(file='Julies_Party_Hire.png')
logo=tk.Label(root, image=logo_image, height=70, width=120)
logo.grid(row=0, column=0, sticky='nw')


mainloop()