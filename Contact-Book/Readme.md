COMMAND LINE CONTACT BOOK

A simple Python-based command line contact book application designed to store and manage user contacts efficiently.

Features
-----
    1) Add new contacts.

    2) Search existing contacts by name.

    3)Delete contacts individually.

    4) View all saved contacts.

    5) Persistent storage of contacts on the local system.

    6) Contacts stored internally in dictionary format.

Requirements
------
    Python 3.9 or higher.

    No external libraries required.

Installation and Running
------
    Clone the repository to your local machine.

    Open a terminal and navigate to the project directory.

Run the application using:
------
    bash
    ------
        python main.py
        
    Usage
    ------
        Upon running the script, you will be greeted with a menu:

    text
    ------
        Welcome to the Command Line Contact Book

        Enter the task you want to perform:

        1 - Add Contact  
        2 - Search Contact  
        3 - Delete Contact  
        4 - View All Contacts  
        5 - Exit
        Select an option by entering the corresponding number.

        Example Session
        text
        Welcome to the Command Line Contact Book

        Enter the task you want to perform:

        1 - Add Contact  
        2 - Search Contact  
        3 - Delete Contact  
        4 - View All Contacts  
        5 - Exit

        : 1
        Enter the name: kunal soyal
        Enter the number: 6250139527
        kunal soyal already exists!

        Enter the task you want to perform:

        2
        Enter the name: gorav gumber

        Name: gorav gumber
        Phone: 9799875350

        Enter the task you want to perform:

        2
        Enter the name: jay

        Contact does not exist! Please add.

        Enter the task you want to perform:

        3
        Enter the name: kunal

        Contact does not exist!

        Enter the task you want to perform:

        3
        Enter the name: gorav gumber

        Contact 'gorav gumber' with phone number 9799875350 was deleted successfully!

        Enter the task you want to perform:

        4

        Current Contacts:

        {'abhay kumar singh': '6203191018', 'kunal soyal': '6350424508', 'harshvardhan salvi': '6203191018'}

        Enter the task you want to perform:

        5
        Thank you for using the Contact Book!

Current Limitations
------
    No validation to verify if phone numbers are correct or formatted properly.

    No option to delete all contacts at once.

    Cannot detect or prevent duplicate phone numbers.

License
------
    This project is open source and released under the MIT License.