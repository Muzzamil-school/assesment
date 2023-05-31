#Muzzamil
#This program is for julies party hire

from tkinter import *
import tkinter as tk

#main window
root=Tk()
root.title("Julie's Party Hire")#window title
root.geometry("1000x400")#define window size
root.configure(bg='cadet blue')#window background colour

#title julies party hire
title_label=tk.Label(root, text='Julies Party Hire', font=('Helvetica', 45), fg='black', bg='cadet blue')#displays title on main window
title_label.grid(row=0, column=1, sticky='w')#defines where on main window it should be

#add logo for julies party hire
logo_image=tk.PhotoImage(file='Julies_Party_Hire.png')#imports image
logo=tk.Label(root, image=logo_image, height=70, width=120)#inserts image onto main window
logo.grid(row=0, column=0, sticky='nw')#defines where on main window it should be

#labels for entry boxes 
customer_name_label=tk.Label(root, text='Customer Full Name', font=('Helvetica', 20), fg='black', bg='cadet blue')#shows what info to enter into entry box
customer_name_label.grid(row=1, column=0, pady=5, padx=15, sticky='w')#defines where on main window it should be
receipt_number_label=tk.Label(root, text='Receipt Number', font=('Helvetica', 20), fg='black', bg='cadet blue')#shows what info to enter into entry box
receipt_number_label.grid(row=2, column=0, pady=5, padx=15, sticky='w')#defines where on main window it should be
item_hired_label=tk.Label(root, text='Item Hired', font=('Helvetica', 20), fg='black', bg='cadet blue')#shows what info to enter into entry box
item_hired_label.grid(row=3, column=0, pady=5, padx=15, sticky='w')#defines where on main window it should be
num_item_hired_label=tk.Label(root, text='No. Items Hired', font=('Helvetica', 20), fg='black', bg='cadet blue')#shows what info to enter into entry box
num_item_hired_label.grid(row=4, column=0, pady=5, padx=15, sticky='w')#defines where on main window it should be
delete_row_label=tk.Label(root, text='Delete Row', font=('Helvetica', 20), fg='black', bg='cadet blue')#shows what info to enter into entry box
delete_row_label.grid(row=5, column=0, pady=5, padx=15, sticky='w')#defines where on main window it should be

#entry boxes for people to enter info
customer_name_entry=Entry(root, width=30)#entry box for customer name
customer_name_entry.grid(row=1, column=1, sticky='w')#defines where on main window it should be
receipt_number_entry=Entry(root, width=30)#entry box for receipt number
receipt_number_entry.grid(row=2, column=1, sticky='w')#defines where on main window it should be
item_hired_entry=Entry(root, width=30)#entry box for item hired
item_hired_entry.grid(row=3, column=1, sticky='w')#defines where on main window it should be
num_item_hired_entry=Entry(root, width=30)#entry box for number of items hired
num_item_hired_entry.grid(row=4, column=1, sticky='w')#defines where on main window it should be
delete_row_entry=Entry(root, width=30)#entry box for which row to delete
delete_row_entry.grid(row=5, column=1, sticky='w')#defines where on main window it should be

#update details function
def update_details():
    #these are global variables used 
    global total_entries, customer_name_entry, receipt_number_entry, item_hired_entry, num_item_hired_entry
    #update each item to its own area of the list
    customer_details.append([customer_name_entry.get(), receipt_number_entry.get(), item_hired_entry.get(), num_item_hired_entry.get()])
    #clears entry boxes after details are updated 
    customer_name_entry.delete(0, 'end')
    receipt_number_entry.delete(0, 'end')
    item_hired_entry.delete(0, 'end')
    num_item_hired_entry.delete(0, 'end')
    total_entries+=1

#print details function
def print_details():
    name_count=0
    # Create the column labels
    Label(root, font=("Helvetica", 12),text="Row", bg='cadet blue', fg='black').grid(column=0, row=9)
    Label(root, font=("Helvetica", 12),text="Customer's Full Name", bg='cadet blue', fg='black').grid(column=1, row=9)
    Label(root, font=("Helvetica", 12),text="Reciept number", bg='cadet blue', fg='black').grid(column=2, row=9)
    Label(root, font=("Helvetica", 12),text="Item hired", bg='cadet blue', fg='black').grid(column=3, row=9)
    Label(root, font=("Helvetica", 12),text="No. of Items Hired", bg='cadet blue', fg='black').grid(column=4, row=9)

# add each item in the list into its own row
    while name_count < total_entries:

        Label(root, text=name_count, bg='cadet blue', fg='black').grid(column=0, row=name_count+10)
        Label(root, text=(customer_details[name_count][0]), bg='cadet blue', fg='black').grid(column=1, row=name_count+10)
        Label(root, text=(customer_details[name_count][1]), bg='cadet blue', fg='black').grid(column=2, row=name_count+10)
        Label(root, text=(customer_details[name_count][2]), bg='cadet blue', fg='black').grid(column=3, row=name_count+10)
        Label(root, text=(customer_details[name_count][3]), bg='cadet blue', fg='black').grid(column=4, row=name_count+10)
        name_count+=1
        print(name_count)

#delete row function
def delete_row():
    #these are global variables used
    global total_entries, delete_row_entry, customer_details
    #finds which row is being deleted and deletes it
    del customer_details[int(delete_row_entry.get())] 
    total_entries-=1
    name_count=0
    delete_row_entry.delete(0,'end')
    #clears row that needs to be deleted
    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+10)
    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+11)
    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+12)
    Label(root, width=100, bg='cadet blue').grid(columnspan=6, row=name_count+13)
    print_details()

#check input function
def check_inputs():
    input_check=0
    #check that customer name is not blank show error if it is
    if len(customer_name_entry.get())==0:
        Label(root, fg="red", text="You Must Fill this Section", bg='cadet blue').grid(column=4, row=1)
        input_check +=1
    if len(customer_name_entry.get())>0:
        Label(root, text="                                                             ", bg='cadet blue').grid(column=4, row=1)
        #chack that customers full name is entered if not show error
        try:
            customer_name_entry.get().split(" ")[1]
            Label(root, text="                                                      ", bg='cadet blue').grid(column=4, row=1)
        except:
            Label(root, fg="red", text="Please Enter Your Full Name", bg='cadet blue').grid(column=4, row=1)
            input_check +=1
    #check that receipt number is not blank show error if it is
    if len(receipt_number_entry.get())==0:
        Label(root, fg="red", text="You Must Fill this Section", bg='cadet blue').grid(column=4, row=2)
        input_check +=1
    if len(receipt_number_entry.get())>0:
        Label(root, text="                                         ", bg='cadet blue').grid(column=4, row=2)
    #check that receipt number is int if not then show error
    if len(receipt_number_entry.get())!=0:
        if receipt_number_entry.get().strip().isdecimal()==False:
            input_check +=1
            Label(root, text="Please Enter a Number", fg="red", bg='cadet blue').grid(row=2, column=4)
        if receipt_number_entry.get().strip().isdecimal()==True:
            Label(root, text="                                                            ", bg='cadet blue').grid(column=4, row=2)
    #check the number of items hired is not empty
    if len(num_item_hired_entry.get())==0:
            Label(root, fg="red", text="You Must Fill this Section", bg='cadet blue').grid(column=4, row=4)
            input_check+=1
     #check the number of items hired is an int
    if len(num_item_hired_entry.get())!=0:
        if num_item_hired_entry.get().strip().isdecimal()==False:
            input_check +=1
            Label(root, text="Please Enter a Number", fg="red", bg='cadet blue').grid(row=4, column=4)
    #check the number of items hired is between 1-500 if not show error
    if (num_item_hired_entry.get().isdigit()):
        if int(num_item_hired_entry.get())<1:
            Label(root, fg="red", text="Please Enter a Number Between 1-500", bg='cadet blue').grid(column=4, row=4)
        if int(num_item_hired_entry.get())>1:
            Label(root, text="                                                                ", bg='cadet blue').grid(column=4, row=4)
        if int(num_item_hired_entry.get())<500:
            Label(root, text="                                                                ", bg='cadet blue').grid(column=4, row=4)
        if int(num_item_hired_entry.get())>500:
            Label(root, fg="red", text="Please Enter a Number Between 1-500", bg='cadet blue').grid(column=4, row=4)
            input_check +=1
    #check the number of items hired is not =0
    if int(num_item_hired_entry.get())==0:
        Label(root, fg="red", text="Please Enter a Number Between 1-500", bg='cadet blue').grid(column=4, row=4)
        input_check +=1
    #check that item hired is not blank show error if it is  
    if len(item_hired_entry.get())==0:
        Label(root, fg="red", text="You Must Fill this Section", bg='cadet blue').grid(column=4, row=3)
        input_check +=1
    if len(item_hired_entry.get())>0:
        Label(root, text="                                                 ", bg='cadet blue').grid(column=4, row=3)
        #check that no numbers have been entered if not show error
        if item_hired_entry.get().isalpha()==False:
            Label(root, fg="red", text="Please Do Not Enter Numbers", bg='cadet blue').grid(column=4, row=3)
            input_check +=1
        if item_hired_entry.get().isalpha()==True:
            Label(root, text="                                ", bg='cadet blue').grid(column=4,row=3)
        #if all requirements are met update details
        if input_check==0:
            update_details()

#buttons
enter_button=Button(root, text='Enter Details', font=('Helvetica', 20), command=check_inputs, width=10)#updates details
enter_button.grid(row=1, column=2, sticky='w')#defines where on main window it should be
print_button=Button(root, text='Print Details', font=('Helvetica', 20), command=print_details, width=10)#prints details
print_button.grid(row=2, column=2, sticky='w')#defines where on main window it should be
delete_button=Button(root, text='Delete Row', font=('Helvetica', 20), command=delete_row, width=10)#deletes row
delete_button.grid(row=3, column=2, sticky='w')#defines where on main window it should be
exit_button=Button(root, text='Exit', font=('Helvetica', 20), command=quit, width=10)#quits program
exit_button.grid(row=4, column=2, sticky='w')#defines where on main window it should be

#defining variables
total_entries=0
customer_details=[]

mainloop()