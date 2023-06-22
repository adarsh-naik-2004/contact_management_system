# contact_management_system

The script begins with the necessary imports: csv for working with CSV files and tkinter for creating the GUI. The messagebox module from tkinter is also imported for displaying messages.

The Admin class defines a simple username-password authentication system. The usernames and passwords are stored in private lists (__usernames and __passwords). The check_credentials method takes a username and password as input and checks if they match the stored credentials. If the credentials are valid, a message is displayed indicating successful verification.

The ContactSystem class is the main class that handles contact management operations. It provides methods for adding, editing, removing, and searching contacts in the system. Contacts are stored in a CSV file named "contacts.csv".

The write_file method is responsible for writing a list of contact data to the CSV file. It takes a list of contact data as input, converts it to a string, and writes it to the file.

The show_contact method reads the contact data from the CSV file, displays it in the GUI, and inserts it into a text widget (show). The contact data is displayed in a formatted manner, showing each contact's details.

The add_contact method takes contact information as input and adds a new contact to the CSV file. It then displays a message indicating successful addition.

The edit_contact method allows editing an existing contact based on the provided user ID. It updates the contact information in the CSV file and displays a message indicating successful update.

The remove_contact method removes a contact from the CSV file based on the provided user ID. It displays a message indicating successful deletion.

The search_by_id, search_by_name, and search_by_group methods search for contacts based on the provided user ID, name, or group, respectively. They display the search results in the GUI's text widget (search) if any matching contacts are found.

The AddContactWindow, EditContactWindow, RemoveContactWindow, and SearchContactWindow classes define separate windows for adding, editing, removing, and searching contacts, respectively. They inherit from the Toplevel class of tkinter and create the necessary widgets (labels, entry fields, buttons) for user interaction.

![image](https://github.com/adarsh-naik-2004/contact_management_system/assets/130145440/8265b293-4a13-4e0d-a1ae-0214e0d55334)


