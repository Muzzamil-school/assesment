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

#update details function
def update_details():
    global total_entries, customer_name_entry, receipt_number_entry, item_hired_entry, num_item_hired_entry
    # append each item to its own area of the list
    customer_details.append([customer_name_entry.get(), receipt_number_entry.get(), item_hired_entry.get(), num_item_hired_entry.get()])
    #clear the boxes
    customer_name_entry.delete(0, 'end')
    receipt_number_entry.delete(0, 'end')
    item_hired_entry.delete(0, 'end')
    num_item_hired_entry.delete(0, 'end')
    total_entries += 1

#print details function
def print_details():
    name_count = 0
    # Create the column headings
    Label(root, font=("Helvetica", 12),text="Row", bg='cadet blue', fg='black').grid(column=0, row=9)
    Label(root, font=("Helvetica", 12),text="Customer's Full Name", bg='cadet blue', fg='black').grid(column=1, row=9)
    Label(root, font=("Helvetica", 12),text="Reciept number", bg='cadet blue', fg='black').grid(column=2, row=9)
    Label(root, font=("Helvetica", 12),text="Item hired", bg='cadet blue', fg='black').grid(column=3, row=9)
    Label(root, font=("Helvetica", 12),text="No. of Itemss Hired", bg='cadet blue', fg='black').grid(column=4, row=9)

# add each item in the list into its own row
    while name_count < total_entries:

        Label(root, text=name_count, bg='cadet blue', fg='black').grid(column=0, row=name_count+10)
        Label(root, text=(customer_details[name_count][0]), bg='cadet blue', fg='black').grid(column=1, row=name_count+10)
        Label(root, text=(customer_details[name_count][1]), bg='cadet blue', fg='black').grid(column=2, row=name_count+10)
        Label(root, text=(customer_details[name_count][2]), bg='cadet blue', fg='black').grid(column=3, row=name_count+10)
        Label(root, text=(customer_details[name_count][3]), bg='cadet blue', fg='black').grid(column=4, row=name_count+10)
        name_count += 1
        print(name_count)

#delete row function
def delete_row():
    global total_entries, delete_row_entry, customer_details
    del customer_details[int(delete_row_entry.get())] 
    total_entries -= 1
    name_count = 0
    delete_row_entry.delete(0,'end')
    
    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+10) 

    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+11)

    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+13)
    
    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+14)
    
    print_details()


mainloop()