#!/usr/bin/python3
"""Run an interactive shell, users can view and edit a phone book and then save it to file."""
class Person:
    """Entry in phonebook able to store and display information"""
    def __init__(self, name, home_number, mobile_number):
        self.name = name
        self.home_number = home_number
        self.mobile_number = mobile_number

    def display(self):
        """Print stored information to screen."""
        print("Name: %s" % (self.name))
        print("Home Number: %s" % (self.home_number))
        print("Mobile Number: %s" % (self.mobile_number))

    def edit(self, new_name):
        """Request user input and use it to edit entry details"""
        if new_name:
            self.name = new_name
        else:
            print("No changes will be made to the entry name")
        self.edit_number("mobile")
        self.edit_number("home")
        print("Revised entry:")
        self.display()

    def edit_number(self, numtype):
        """Take input from user and edit the appropriate number."""
        print("Current entry %s number:" % (numtype))
        if numtype == "mobile":
            print(self.mobile_number)
        else:
            print(self.home_number)
        new_number = input("Enter new %s number: (leave blank to remain same)\n" % (numtype))
        if new_number:
            if numtype == "mobile":
                self.mobile_number = new_number
            else:
                self.home_number = new_number
        else:
            print("No changes will be made to %s phone number" % (numtype))

class Book:
    """Stores list of Person objects, contains methods to manipulate and view that list."""
    def __init__(self):
        self.name = "phonebook"
        self.people = []

    def display_self(self):
        """Iterate through all entries in book and display details."""
        print("")
        print("---Fonbuk 5000 User List---")
        print("")
        for i in self.people:
            i.display()
            print("")
        print("---End of Fonbuk---\n")

    def search(self):
        """Request criteria from user, iterate through all entries and display matching results."""
        search = input("Enter part or whole of entry name:\n")
        count = 0
        for i in self.people:
            if search in i.name:
                i.display()
                count = 1
        if count == 0:
            print("Could not find any entries matching that description")

    def man_add_person(self):
        """Request input from user, create new entry based on that then add to phonebook."""
        new_name = input("Enter new entry's name:\n")
        if self.check_duplicate(new_name) == 0:
            print("An entry with that name already exists,")
            print("please try again with a different name")
        else:
            new_home_number = input("Enter new entry's home number:\n")
            new_mobile_number = input("Enter new entry's mobile number:\n")
            self.people.append(Person(new_name, new_home_number, new_mobile_number))

    def delete_person(self):
        """Request input from user, identify then delete appropriate entry."""
        delrow = input("Enter exact name of entry to be deleted\n")
        index = self.identify_by_name(delrow)
        if index == "None":
            print("Delete failed! Returning to main menu")
        else:
            print("Deleting %s" % (self.people[index].name))
            del self.people[index]

    def edit_person(self):
        """Request input from user, identify entry and then edit it based on further input."""
        edited = input("Enter exact name of entry to be edited\n")
        index = self.identify_by_name(edited)
        if index == "None":
            print("Edit failed! Returning to main menu")
        else:
            print("Current entry Name: %s" % (self.people[index].name))
            new_name = input("Enter new name: (leave blank to remain the same)\n")
            dupe = self.check_duplicate(new_name)
            if (dupe == 0) & (new_name != self.people[index].name):
                print("An entry with that name already exists,")
                print("please try again with a different name")
            else:
                self.people[index].edit(new_name)

    def identify_by_name(self, name):
        """Identify entry then return entry's position in book."""
        for idx, person in enumerate(self.people):
            if name == person.name:
                return idx
        print("No entry found with that name")
        return "None"

    def check_duplicate(self, name):
        """Check for entrys with the provided name, returns 0 if already exists or 1 otherwise."""
        for i in self.people:
            if name == i.name:
                return 0
        return 1

    def order_entries(self):
        """Sort phonebook alphabetically(ish)."""
        sortlist = []
        for i in self.people:
            if not sortlist:
                sortlist.append(i)
            else:
                counter = len(sortlist)-1
                while counter >= 0:
                    if i.name > sortlist[counter].name:
                        sortlist.insert(counter+1, i)
                        counter = -1
                    elif counter == 0:
                        sortlist.insert(0, i)
                        counter = -1
                    else:
                        counter -= 1
        self.people = sortlist

    def auto_pop(self):
        """Fill in phonebook with dummy entries, to be used for testing or demonstration."""
        print("autopopulating phone book")
        self.people.append(Person("john", "01245348070", "07800571191"))
        self.people.append(Person("jonas", "01245348071", "07800571192"))
        self.people.append(Person("jim", "01245348072", "07800571193"))
        self.people.append(Person("jerome", "01245348073", "07800571194"))
        self.people.append(Person("jeremey", "01245348074", "07800571195"))
        self.people.append(Person("jil", "01245348075", "07800571196"))
        self.people.append(Person("jeff", "01245348076", "07800571197"))
        self.people.append(Person("jerry", "01245348077", "07800571198"))
        self.people.append(Person("josh", "01245348078", "07800571199"))
        self.people.append(Person("joe", "01245348079", "07800571200"))
        self.people.append(Person("julia", "01245348080", "07800571201"))

    def save_file(self):
        """Save current phonebook entries to a file with name input by user."""
        filename = input("Please enter name of fonbuk to be saved\n")
        if filename == "":
            filename = "DEFAULTSAVE"
            print("Blank filename has been interpreted as DEFAULTSAVE")
        with open(("savefiles/%s" % (filename)), "w") as file:
            for i in self.people:
                file = open(("savefiles/%s" % (filename)), "a")
                file.write("%s,%s,%s\n" % (i.name, i.home_number, i.mobile_number))
        print("Successfully saved to file")

    def load_file(self):
        """Replace current phonebook entries with those in a file with name specified by user."""
        print("WARNING! This will overwrite currently active fonbuk data.")
        check = "y"
        while check == "y" or check == "yes":
            self.clear_buk()
            print("Please enter name of fonbuk to be loaded")
            filename = input("")
            if filename == "":
                filename = "DEFAULTSAVE"
                print("Blank filename has been interpreted as DEFAULTSAVE")
            try:
                file = open(("savefiles/%s" % (filename)), "r")
            except FileNotFoundError:
                print("File not found, cancelling load")
                break
            for line in file:
                name, home_number, mobile_number = line.split(",", 2)
                if self.check_duplicate(name) == 0:
                    self.clear_buk()
                    print("File contains duplicate names, cancelling load")
                else:
                    name = name.rstrip()
                    home_number = home_number.rstrip()
                    mobile_number = mobile_number.rstrip()
                    self.auto_add_person(name, home_number, mobile_number)
            file.close()
            print("File sucessfully loaded")
            self.display_self()
            check = "n"

    def auto_add_person(self, new_name, new_home_number, new_mobile_number):
        """Generate and add user based on provided details."""
        print(new_name)
        print(new_mobile_number)
        print(new_home_number)
        self.people.append(Person(new_name, new_home_number, new_mobile_number))

    def clear_buk(self):
        """Empty current phone book."""
        self.people = []


class Execute:
    """Handle The currently active user session"""
    def __init__(self):
        self.book = Book()
        self.checkcontinue = "y"

    def main(self):
        """Introduce session and maintain loop in which user takes actions."""
        print("Hello and welcome to Fonbuk 5000")
        print("There are currently %s entries" % (len(self.book.people)))
        while self.checkcontinue == "y":
            self.take_action()

    def take_action(self):
        """Display menu to user, request and then interpret input from user"""
        self.book.order_entries()
        print("What do you want to do?")
        print("[a]dd entry")
        print("[d]elete entry")
        print("[e]dit entry")
        print("[s]how all entries")
        print("sea[r]ch entries")
        print("sa[v]e to file")
        print("[l]oad from file")
        print("e[x]it program")
        action = input("")
        if action == "a" or action == "add":
            self.book.man_add_person()
        elif action == "d" or action == "delete":
            self.book.delete_person()
        elif action == "e" or action == "edit":
            self.book.edit_person()
        elif action == "s" or action == "show":
            self.book.display_self()
        elif action == "x" or action == "exit":
            self.exit()
        elif action == "v" or action == "save":
            self.book.save_file()
        elif action == "l" or action == "load":
            self.book.load_file()
        elif action == "r" or action == "search":
            self.book.search()
        elif action == "ap":
            self.book.auto_pop()
        else:
            print("Invalid selection!")

    def exit(self):
        """Request input from user to check saving of book, then break Loop ending session"""
        save = input("Before you leave do you want to save the phone book? (y or n)\n")
        if save == "y" or save == "yes":
            self.book.save_file()
        print("Thank you for using Fonbuk 5000, have a great day!")
        self.checkcontinue = "n"


EXECUTOR = Execute()
EXECUTOR.main()
