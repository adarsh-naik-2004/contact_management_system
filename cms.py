import csv
import tkinter as tk
from tkinter import messagebox

class Admin:
    
    __usernames = ['arpit', 'adarsh']
    __passwords = ['221010211', '221010202']

    def check_credentials(self, username, password):
        if username in self.__usernames:
            index = self.__usernames.index(username)
            if password == self.__passwords[index]:
                messagebox.showinfo("Admin Verified", "Admin verified!!")
                return True
            else:
                messagebox.showerror("Incorrect Password", "Incorrect password!!")
                return False
        else:
            messagebox.showerror("Incorrect Username", "Incorrect username!!")
            return False
        
class ContactSystem: 

    def write_file(self,list_data):
            f = open("contacts.csv", "w")
            all_data = str()
            for data in list_data:
                    all_data += data+'\n'
            f.write(all_data)
            f.close()
            return True
        
    def show_contact(self):
        f=open("contacts.csv",'r')
        main_data=f.read()
        main_data=main_data.split('\n')
        main_data=(list(filter(None,main_data)))
        show.delete(1.0, tk.END)
        show.insert(tk.END,"List of Contacts :\n")
        show.insert(tk.END,"---------------------------------------------------------------------------\n")

        if main_data:
            for data in main_data:
                        if data!=[]:
                            split_data=data.split(',')                            
                            show.insert(tk.END,f"User ID : {split_data[0]}\n")
                            show.insert(tk.END,f"Name : {split_data[1]}\n")
                            show.insert(tk.END,f"Email : {split_data[2]}\n")
                            show.insert(tk.END,f"Mobile No. : {split_data[3]}\n")
                            show.insert(tk.END,f"Address : {split_data[4]}\n")
                            show.insert(tk.END,f"Group : {split_data[5]}\n")
                            show.insert(tk.END,f"Note : {split_data[6]}\n")
                            show.insert(tk.END,"---------------------------------------------------------------------------\n")
                           
        else:
            messagebox.showwarning("No Records", "No records found.")

    def add_contact(self, user_id, name, email, mobile_no, address, group, note):
        data = user_id+','+name+','+email+','+mobile_no+','+address+','+group+','+note+'\n'
        f = open("contacts.csv", "a")
        f.write(data)
        f.close()
        messagebox.showinfo("Contact Added", "Contact added successfully.")

    def edit_contact(self, user_id, name, email, mobile_no, address, group, note):
        new_value=user_id+','+name+','+email+','+mobile_no+','+address+','+group+','+note
        f=open("contacts.csv",'r')
        main_data=f.read()
        main_data=main_data.split('\n')
        main_data=(list(filter(None,main_data)))
        for data in main_data:
                split_data=data.split(',')
                if user_id == split_data[0]:
                    main_data[main_data.index(data)] = new_value
                    
        if (self.write_file(main_data)):                    
            messagebox.showinfo("Contact Updated", "Contact updated successfully.")                    
        else:    
            messagebox.showerror("Contact Not Found", "Contact not found.")

    def remove_contact(self, user_id):
        f=open("contacts.csv",'r')
        main_data=f.read()
        main_data=main_data.split('\n')
        main_data=(list(filter(None,main_data)))
        for data in main_data:
            if user_id == data[0]:
                main_data.remove(data)
                break
        if (self.write_file(main_data)):
            messagebox.showinfo("Contact Deleted", "Contact deleted successfully.")
        else:
            messagebox.showerror("Contact Not Found", "Contact not found.")

    def search_by_id(self, user_id):
        f=open("contacts.csv",'r')
        main_data=f.read()
        main_data=main_data.split('\n')
        main_data=(list(filter(None,main_data)))
        search.delete(1.0, tk.END)
        search.insert(tk.END,"Search Results :\n")
        search.insert(tk.END,"---------------------------------------------------------------------------\n")
        found=False
        for data in main_data:
            split_data=data.split(',')
            if user_id==split_data[0]:
                search.insert(tk.END,f"User ID : {split_data[0]}\n")
                search.insert(tk.END,f"Name : {split_data[1]}\n")
                search.insert(tk.END,f"Email : {split_data[2]}\n")
                search.insert(tk.END,f"Mobile No. : {split_data[3]}\n")
                search.insert(tk.END,f"Address : {split_data[4]}\n")
                search.insert(tk.END,f"Group : {split_data[5]}\n")
                search.insert(tk.END,f"Note : {split_data[6]}\n")
                search.insert(tk.END,"---------------------------------------------------------------------------\n")
                found = True
        if not found:
            messagebox.showinfo("Contact Not Found", "Contact not found.")    

    def search_by_name(self, name):
        f=open("contacts.csv",'r')
        main_data=f.read()
        main_data=main_data.split('\n')
        main_data=(list(filter(None,main_data)))
        search.delete(1.0, tk.END)
        search.insert(tk.END,"Search Results :\n")
        search.insert(tk.END,"---------------------------------------------------------------------------\n")
        found = False
        for data in main_data:
            split_data=data.split(',')
            if name == split_data[1]:
                search.insert(tk.END,f"User ID : {split_data[0]}\n")
                search.insert(tk.END,f"Name : {split_data[1]}\n")
                search.insert(tk.END,f"Email : {split_data[2]}\n")
                search.insert(tk.END,f"Mobile No. : {split_data[3]}\n")
                search.insert(tk.END,f"Address : {split_data[4]}\n")
                search.insert(tk.END,f"Group : {split_data[5]}\n")
                search.insert(tk.END,f"Note : {split_data[6]}\n")
                search.insert(tk.END,"---------------------------------------------------------------------------\n")
                found = True
        if not found:
            messagebox.showinfo("Contact Not Found", "Contact not found.")

    def search_by_group(self, group):
        f=open("contacts.csv",'r')
        main_data=f.read()
        main_data=main_data.split('\n')
        main_data=(list(filter(None,main_data)))
        search.delete(1.0, tk.END)
        search.insert(tk.END,"Search Results :\n")
        search.insert(tk.END,"---------------------------------------------------------------------------\n")
        found = False
        for data in main_data:
            split_data=data.split(',')
            if group == split_data[5]:
                search.insert(tk.END,f"User ID : {split_data[0]}\n")
                search.insert(tk.END,f"Name : {split_data[1]}\n")
                search.insert(tk.END,f"Email : {split_data[2]}\n")
                search.insert(tk.END,f"Mobile No. : {split_data[3]}\n")
                search.insert(tk.END,f"Address : {split_data[4]}\n")
                search.insert(tk.END,f"Group : {split_data[5]}\n")
                search.insert(tk.END,f"Note : {split_data[6]}\n")
                search.insert(tk.END,"---------------------------------------------------------------------------\n")
                found = True
        if not found:
            messagebox.showinfo("Group Not Found", "Group not found.")
   
class AddContactWindow:
    
    def _init_(self, parent, contact_system):
        self.contact_system = contact_system
        self.window = tk.Toplevel(parent)
        self.window.title("Add Contact")

        self.create_widgets()

    def create_widgets(self):
        self.label_user_id = tk.Label(self.window, text="User ID:")
        self.label_user_id.grid(row=0, column=0, sticky=tk.E)

        self.entry_user_id = tk.Entry(self.window)
        self.entry_user_id.grid(row=0, column=1)

        self.label_name = tk.Label(self.window, text="Name:")
        self.label_name.grid(row=1, column=0, sticky=tk.E)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.grid(row=1, column=1)

        self.label_email = tk.Label(self.window, text="Email:")
        self.label_email.grid(row=2, column=0, sticky=tk.E)

        self.entry_email = tk.Entry(self.window)
        self.entry_email.grid(row=2, column=1)

        self.label_mobile_no = tk.Label(self.window, text="Mobile No:")
        self.label_mobile_no.grid(row=3, column=0, sticky=tk.E)

        self.entry_mobile_no = tk.Entry(self.window)
        self.entry_mobile_no.grid(row=3, column=1)

        self.label_address = tk.Label(self.window, text="Address:")
        self.label_address.grid(row=4, column=0, sticky=tk.E)

        self.entry_address = tk.Entry(self.window)
        self.entry_address.grid(row=4, column=1)

        self.label_group = tk.Label(self.window, text="Group:")
        self.label_group.grid(row=5, column=0, sticky=tk.E)

        self.entry_group = tk.Entry(self.window)
        self.entry_group.grid(row=5, column=1)

        self.label_note = tk.Label(self.window, text="Note:")
        self.label_note.grid(row=6, column=0, sticky=tk.E)

        self.entry_note = tk.Entry(self.window)
        self.entry_note.grid(row=6, column=1)

        self.button_add = tk.Button(self.window, text="Add", command=self.add)
        self.button_add.grid(row=7, column=0)

    def add(self):
        user_id = self.entry_user_id.get()
        name = self.entry_name.get()
        email = self.entry_email.get()
        mobile_no = self.entry_mobile_no.get()
        address = self.entry_address.get()
        group = self.entry_group.get()
        note = self.entry_note.get()
        self.contact_system.add_contact(user_id, name, email, mobile_no, address, group, note)
        self.window.destroy()

class EditContactWindow:
    
    def _init_(self, parent, contact_system):
        self.contact_system = contact_system
        self.window = tk.Toplevel(parent)
        self.window.title("Edit Contact")

        self.create_widgets()

    def create_widgets(self):
        self.label_user_id = tk.Label(self.window, text="User ID:")
        self.label_user_id.grid(row=0, column=0, sticky=tk.E)

        self.entry_user_id = tk.Entry(self.window)
        self.entry_user_id.grid(row=0, column=1)

        self.button_search = tk.Button(self.window, text="Search", command=self.search)
        self.button_search.grid(row=1, column=0)

        self.label_name = tk.Label(self.window, text="Name:")
        self.label_name.grid(row=2, column=0, sticky=tk.E)

        self.entry_name = tk.Entry(self.window)
        self.entry_name.grid(row=2, column=1)

        self.label_email = tk.Label(self.window, text="Email:")
        self.label_email.grid(row=3, column=0, sticky=tk.E)

        self.entry_email = tk.Entry(self.window)
        self.entry_email.grid(row=3, column=1)

        self.label_mobile_no = tk.Label(self.window, text="Mobile No:")
        self.label_mobile_no.grid(row=4, column=0, sticky=tk.E)

        self.entry_mobile_no = tk.Entry(self.window)
        self.entry_mobile_no.grid(row=4, column=1)

        self.label_address = tk.Label(self.window, text="Address:")
        self.label_address.grid(row=5, column=0, sticky=tk.E)

        self.entry_address = tk.Entry(self.window)
        self.entry_address.grid(row=5, column=1)

        self.label_group = tk.Label(self.window, text="Group:")
        self.label_group.grid(row=6, column=0, sticky=tk.E)

        self.entry_group = tk.Entry(self.window)
        self.entry_group.grid(row=6, column=1)

        self.label_note = tk.Label(self.window, text="Note:")
        self.label_note.grid(row=7, column=0, sticky=tk.E)

        self.entry_note = tk.Entry(self.window)
        self.entry_note.grid(row=7, column=1)

        self.button_update = tk.Button(self.window, text="Update", command=self.update)
        self.button_update.grid(row=8, column=0)

    def search(self):
        user_id = self.entry_user_id.get()
        self.contact_system.search_by_id(user_id)

    def update(self):
        user_id = self.entry_user_id.get()
        name = self.entry_name.get()
        email = self.entry_email.get()
        mobile_no = self.entry_mobile_no.get()
        address = self.entry_address.get()
        group = self.entry_group.get()
        note = self.entry_note.get()
        self.contact_system.edit_contact(user_id, name, email, mobile_no, address, group, note)
        self.window.destroy()

class RemoveContactWindow:
    def _init_(self, parent, contact_system):
        self.contact_system = contact_system
        self.window = tk.Toplevel(parent)
        self.window.title("Remove Contact")

        self.create_widgets()

    def create_widgets(self):
        self.label_user_id = tk.Label(self.window, text="User ID:")
        self.label_user_id.grid(row=0, column=0, sticky=tk.E)

        self.entry_user_id = tk.Entry(self.window)
        self.entry_user_id.grid(row=0, column=1)

        self.button_remove = tk.Button(self.window, text="Remove", command=self.remove)
        self.button_remove.grid(row=1, column=0)

    def remove(self):
        user_id = self.entry_user_id.get()
        self.contact_system.remove_contact(user_id)
        self.window.destroy()

class SearchContactWindow:
    def _init_(self, parent, contact_system):
        self.contact_system = contact_system
        self.window = tk.Toplevel(parent)
        self.window.title("Search Contact")

        self.create_widgets()

    def create_widgets(self):
        self.label_search_by = tk.Label(self.window, text="Search By:")
        self.label_search_by.grid(row=0, column=0, sticky=tk.E)

        self.search_by_var = tk.StringVar()
        self.search_by_var.set("ID")

        self.radio_button_id = tk.Radiobutton(self.window, text="ID", variable=self.search_by_var, value="ID")
        self.radio_button_id.grid(row=0, column=1, sticky=tk.W)

        self.radio_button_name = tk.Radiobutton(self.window, text="Name", variable=self.search_by_var, value="Name")
        self.radio_button_name.grid(row=0, column=2, sticky=tk.W)

        self.radio_button_group = tk.Radiobutton(self.window, text="Group", variable=self.search_by_var, value="Group")
        self.radio_button_group.grid(row=0, column=3, sticky=tk.W)

        self.label_value = tk.Label(self.window, text="Value:")
        self.label_value.grid(row=1, column=0, sticky=tk.E)

        self.entry_value = tk.Entry(self.window)
        self.entry_value.grid(row=1, column=1)

        self.button_search = tk.Button(self.window, text="Search", command=self.search)
        self.button_search.grid(row=2, columnspan=4)

    def search(self):
        search_by = self.search_by_var.get()
        value = self.entry_value.get()
        if search_by == "ID":
            self.contact_system.search_by_id(value)
        elif search_by == "Name":
            self.contact_system.search_by_name(value)
        elif search_by == "Group":

            self.contact_system.search_by_group(value)
            

def login():
    username = entry_username.get()
    password = entry_password.get()
    if admin.check_credentials(username, password)==True:
            
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        button_login.config(state=tk.DISABLED)
        button_show_contact.config(state=tk.NORMAL)
        button_add_contact.config(state=tk.NORMAL)
        button_edit_contact.config(state=tk.NORMAL)
        button_remove_contact.config(state=tk.NORMAL)
        button_search_contact.config(state=tk.NORMAL)

def show_contact():
        contact_system.show_contact()

def add_contact():        
        AddContactWindow(window,contact_system)
def edit_contact():
        EditContactWindow(window,contact_system)

def remove_contact():
        RemoveContactWindow(window,contact_system)

def search_contact():
        f=open("contacts.csv",'r')
        main_data=f.read()
        main_data=main_data.split('\n')
        main_data=(list(filter(None,main_data)))
        group.delete(1.0, tk.END)
        group.insert(tk.END,"Groups :\n")
        group.insert(tk.END,"-------------------------\n")
        grps=set()
        for data in main_data:
            split_data=data.split(',')
            grps.add(split_data[5])
        for i in grps:
            group.insert(tk.END,f"{i}\n")
        SearchContactWindow(window,contact_system)

window = tk.Tk()
window.title("Contact Management System")
window.geometry("800x600")
admin = Admin()
contact_system=ContactSystem()

label_username = tk.Label(window, text="Username:")
label_username.grid(row=0, column=0, pady=10, sticky=tk.E)

entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1,pady=10)

label_password = tk.Label(window, text="Password:")
label_password.grid(row=1, column=0, sticky=tk.E)

entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1, pady=10)

button_login = tk.Button(window, text="Login", command=login)
button_login.grid(row=2, column=1, pady=10)

button_show_contact = tk.Button(window, text="Show Contacts", command=show_contact)
button_show_contact.grid(row=3, column=1, pady=10)

button_add_contact = tk.Button(window, text="Add Contact", command=add_contact)
button_add_contact.grid(row=4, column=1, pady=10)

button_edit_contact = tk.Button(window, text="Edit Contact", command=edit_contact)
button_edit_contact.grid(row=5, column=1,pady=10)

button_remove_contact = tk.Button(window, text="Remove Contact", command=remove_contact)
button_remove_contact.grid(row=6, column=1, pady=10)

button_search_contact = tk.Button(window, text="Search Contact", command=search_contact)
button_search_contact.grid(row=7, column=1, pady=10)

button_add_contact.config(state=tk.DISABLED)
button_edit_contact.config(state=tk.DISABLED)
button_remove_contact.config(state=tk.DISABLED)

show = tk.Text(window, width=75, height=25)
show.grid(row=9, column=0, padx=20, pady=20)
group = tk.Text(window, width=25, height=25)
group.grid(row=9, column=1, padx=20, pady=20)
search = tk.Text(window, width=75, height=25)
search.grid(row=9, column=2, padx=20, pady=20)

f=open("contacts.csv",'r')
main_data=f.read()
main_data=main_data.split('\n')
main_data=(list(filter(None,main_data)))
group.delete(1.0, tk.END)
group.insert(tk.END,"Groups :\n")
group.insert(tk.END,"-------------------------\n")
grps=set()
for data in main_data:
    split_data=data.split(',')
    grps.add(split_data[5])
for i in grps:
    group.insert(tk.END,f"{i}\n")

window.mainloop()
