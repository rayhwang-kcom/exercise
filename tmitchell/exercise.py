#!/usr/bin/python3
"""Run an interactive shell, users can view and edit a phone book and then save it to file."""
class Person:
    """Entry in phonebook able tyo store and display information"""
    def __init__(self, name, hnumber, mnumber):
        self.name = name
        self.hnumber = hnumber
        self.mnumber = mnumber

    def display(self):
        """Print stored information to screen."""
        print("Name: %s" % (self.name))
        print("Home Number: %s" % (self.hnumber))
        print("Mobile Number: %s" % (self.mnumber))

    def edit(self, new_name):
        """Request user input and use it to edit entry details"""
        if new_name != "":
            self.name = new_name
        else:
            print("No changes will be made to the entry name")
        print("Current entry home number:")
        print(self.hnumber)
        print("Enter new home number: (leave blank to remain same)")
        new_hnumber = input("")
        if new_hnumber != "":
            self.hnumber = new_hnumber
        else:
            print("No changes will be made to home phone number")
        print("Current entry mobile number:")
        print(self.mnumber)
        print("Enter new mobile number: (leave blank to remain same)")
        new_mnumber = input("")
        if new_mnumber != "":
            self.mnumber = new_mnumber
        else:
            print("No changes will be made to mobile phone number")
        print("Revised entry:")
        self.display()

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
        print("---End of Fonbuk---")
        print("")

    def search(self):
        """Request criteria from user, iterate through all entries and display matching results."""
        print("Enter part or whole of entry name:")
        search = input("")
        count = 0
        for i in self.people:
            if search in i.name:
                i.display()
                count = 1
        if count == 0:
            print("Could not find any entries matching that description")

    def man_add_person(self):
        """Request input from user, create new entry based on that then add to phonebook."""
        print("Enter new entry's name:")
        new_name = input("")
        if self.check_duplicate(new_name) == 0:
            print("An entry with that name already exists,")
            print("please try again with a different name")
        else:
            print("Enter new entry's home number:")
            new_hnumber = input("")
            print("Enter new entry's mobile number:")
            new_mnumber = input("")
            new_person = Person(new_name, new_hnumber, new_mnumber)
            self.people.append(new_person)

    def delete_person(self):
        """Request input from user, identify then delete appropriate entry."""
        print("Enter exact name of entry to be deleted")
        delrow = input("")
        index = self.identify_by_name(delrow)
        if index == "null":
            print("Delete failed! Returning to main menu")
        else:
            print("Deleting %s" % (self.people[index].name))
            del self.people[index]

    def edit_person(self):
        """Request input from user, identify entry and then edit it based on further input."""
        print("Enter exact name of entry to be edited")
        edited = input("")
        index = self.identify_by_name(edited)
        if index == "null":
            print("Edit failed! Returning to main menu")
        else:
            print("Current entry Name: %s" % (self.people[index].name))
            print("Enter new name: (leave blank to remain the same)")
            new_name = input("")
            dupe = self.check_duplicate(new_name)
            if (dupe == 0) & (new_name != self.people[index].name):
                print("An entry with that name already exists,")
                print("please try again with a different name")
            else:
                self.people[index].edit(new_name)

    def identify_by_name(self, name):
        """Identify entry then return entry's position in book."""
        count = 0
        for i in self.people:
            if name == i.name:
                return count
            count += 1
        print("No entry found with that name")
        return "null"

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
        print("Please enter name of fonbuk to be saved")
        filename = input("")
        if filename == "":
            filename = "DEFAULTSAVE"
            print("Blank filename has been interpreted as DEFAULTSAVE")
        file = open(("savefiles/%s" % (filename)), "w")
        for i in self.people:
            file = open(("savefiles/%s" % (filename)), "a")
            file.write("%s,%s,%s\n" % (i.name, i.hnumber, i.mnumber))
            file.close()
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
                name, hnumber, mnumber = line.split(",", 2)
                if self.check_duplicate(name) == 0:
                    self.clear_buk()
                    print("File contains duplicate names, cancelling load")
                else:
                    name = name.rstrip()
                    hnumber = hnumber.rstrip()
                    mnumber = mnumber.rstrip()
                    self.auto_add_person(name, hnumber, mnumber)
            file.close()
            print("File sucessfully loaded")
            self.display_self()
            check = "n"

    def auto_add_person(self, new_name, new_hnumber, new_mnumber):
        """Generate and add user based on provided details."""
        print(new_name)
        print(new_mnumber)
        print(new_hnumber)
        new_person = Person(new_name, new_hnumber, new_mnumber)
        self.people.append(new_person)

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
        print("Before you leave do you want to save the phone book? (y or n)")
        save = input("")
        if save == "y" or save == "yes":
            self.book.save_file()
        print("Thank you for using Fonbuk 5000, have a great day!")
        self.checkcontinue = "n"


EXECUTOR = Execute()
EXECUTOR.main()
