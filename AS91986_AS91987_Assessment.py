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

#labels for entry boxes 
customer_name_label=tk.Label(root, text='Customer Full Name', font=('Helvetica', 20), fg='black', bg='cadet blue')
customer_name_label.grid(row=1, column=0, pady=5, padx=15, sticky='w')
receipt_number_label=tk.Label(root, text='Receipt Number', font=('Helvetica', 20), fg='black', bg='cadet blue')
receipt_number_label.grid(row=2, column=0, pady=5, padx=15, sticky='w')
item_hired_label=tk.Label(root, text='Item Hired', font=('Helvetica', 20), fg='black', bg='cadet blue')
item_hired_label.grid(row=3, column=0, pady=5, padx=15, sticky='w')
num_item_hired_label=tk.Label(root, text='No. Items Hired', font=('Helvetica', 20), fg='black', bg='cadet blue')
num_item_hired_label.grid(row=4, column=0, pady=5, padx=15, sticky='w')
delete_row_label=tk.Label(root, text='Delete Row', font=('Helvetica', 20), fg='black', bg='cadet blue')
delete_row_label.grid(row=5, column=0, pady=5, padx=15, sticky='w')






#entry boxes for people to enter info
customer_name_entry=Entry(root, width=30)
customer_name_entry.grid(row=1, column=1, sticky='w')
receipt_number_entry=Entry(root, width=30)
receipt_number_entry.grid(row=2, column=1, sticky='w')
item_hired_entry=Entry(root, width=30)
item_hired_entry.grid(row=3, column=1, sticky='w')
num_item_hired_entry=Entry(root, width=30)
num_item_hired_entry.grid(row=4, column=1, sticky='w')
delete_row_entry=Entry(root, width=30)
delete_row_entry.grid(row=5, column=1, sticky='w')









mainloop()