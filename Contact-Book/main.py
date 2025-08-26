class contactBook:
    def __init__(self, filename="contact_book.txt"):
        self.filename = filename
        self.contact = self.load_contacts()


    def load_contacts(self):
        contact: dict = {}
        with open(self.filename,'r',encoding='utf-8') as f:
            for line in f:
                if ',' in line:
                    name, phone = line.strip().split(',', 1)
                    contact[name] = phone

        return contact
    

    def contact_save(self):
        with open(self.filename,'+w',encoding='utf-8') as f:
            for name, phone in self.contact.items():
                f.write(f"{name},{phone}\n")


    def add(self,name,phone):
        if name in self.contact:
            return f"\n{name} already exist!"   
        else: 
            self.contact[name] = phone

        self.contact_save()
        return f"\n\n{name} added sucesfully."


    def search(self, name):
        if name in self.contact:
            print(f"\nname:- {name}\nphone:- {self.contact[name]}") 
        else:
            print(f"\nContact Does not exist!\n\tPlease Add!")

    def delete(self, name):
        if name in self.contact:
            print(f"\ncontact\n\nname:- {name}\n phone number:- {self.contact[name]}\n\nis delete successfully!")
            del self.contact[name] 
        else:
            print(f"\nContact already does not exist!")
    
    def list(self):
        print(f"\nThe Contact Book\n\n{self.contact}")


def main():

    contact_book = contactBook()
    print("welcome to the command line Contact Book\n")
    while True:    
        print("\nEnter the task you want to do\n")
        task=int(input(f"Enter 1 to Add Contact\nEnter 2 to search a Contact\nEnter 3 to delete a Contact\nEnter 4 to see all the contact\nOr enter 5 to exit\n:- "))
        if task == 1:
            name = input("Enter the name : ")
            phone = int(input("Enter the number : "))
            print(contact_book.add(name,phone))
        elif task == 2:
            name = input("Enter the name : ")
            contact_book.search(name)
        elif task == 3:
            name = input("Enter the name : ")
            contact_book.delete(name)
        elif task == 4:
            contact_book.list()
        elif task == 5:
            print(f"Thank You!")
            break
        else:
            print(f"Invalid Input, Try Again\n")


if __name__ == "__main__":
    main()