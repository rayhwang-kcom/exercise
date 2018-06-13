# Create empty book
address_book = [] 
# Show menu
print (40 * '-')
print ("             Address Book")
print (40 * '-')
print ("1. Enter Name, Phone Number and Address")
print ("2. Read current stored data")
print ("3. Exit")
print (40 * '-')
 
# Get input
choice = input('Enter your choice [1-3] : ')

# String to int
choice = int(choice)
 
# Take action
if choice == 1:
        print("Hi please enter your Name, Phone Number and Address")
        name = input('Name ')
        phone = input('Phone ')
        address = input('Address ')
        print("So your name is -", name)
        print("your phone number is -", phone)
        print("and your address is -", address)
        address_book.append(name)
        address_book.append(phone)
        address_book.append(address)
        #print(address_book) # me testing output format

# Lets open the file and apend data        
        with open("address.txt", "a") as f:
            for s in address_book:
                f.write(str(s) +"\n")
elif choice == 2:
        print ("Reading in currently stored data")
        with open("address.txt", "r") as f:
            data = f.readlines()    

        for line in data:
            address = line.split()
            print(address)
elif choice == 3:
        print ("Exiting...")
else:    # default choice
        print ("Invalid number. Try again...")
