#================================================
# Brandon Thompson
# Contact List for Software Engineering IV Final
#================================================

class Person():
    def __init__(self, first_name, last_name, number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def __str__(self):
        return f'{self.last_name}, {self.first_name} - {self.number}, {self.email}'

#=========================================================
# display_menu: displays the main menu of the program 
#   and returns the user's answer as a lowercase character
#=========================================================
def display_menu():
    print("\n\t Main Menu\n")
    ans = input("""    A - Add Person
    D - Delete Person
    F - Find and Display Person
    L - List all People
    S - Save List
    E - Exit\n
    Enter Choice: """)

    return ans.lower()

#========================================================
# add_person: prompts the user for first name, last name,
#   number, and email of a person and adds them to the 
#   contact_list dictionary
#========================================================
def add_person(self):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    number = input("Enter phone number: ")
    email = input("Enter email address: ")

    p = Person(first_name, last_name, number, email)
    contact_list[p.last_name] = p

#=========================================================
# delete_person: prompts the user for the last name of 
#   the person they want to delete and deletes that person
#   from the contact_list dictionary
# Also gives error if the person the user enters is not
#   in the contact_list dictionary
#=========================================================
def delete_person(self):
    last_name = input("Enter last name: ")
    try:
        del contact_list[last_name]
    except:
        print("Person not in list")

#============================================================
# find_person: prompts the user for the last name of
#   the person they want to find and displays all information
#   about that person
# Also gives error if the person the user enters is not
#   in the contact_list dictionary
#============================================================
def find_person(self):
    last_name = input("Enter last name: ")
    try:
        print(contact_list[last_name])
    except:
        print("Person not in list")

#========================================================
# list_all_people: sorts the contact_list dictionary by
#   last name keys and displays all information about all 
#   people in the contact list
#========================================================
def list_all_people(self):
    for key in sorted(contact_list):
        print(contact_list[key])

#===================================================
# save_list: writes the contents of the contact_list
#   dictionary to a file name 'contacts.txt'
#===================================================
def save_list(self):
    f = open("contacts.txt", "w")
    for key in contact_list:
        p = contact_list[key]
        f.write(p.last_name + ',' + p.first_name + ',' + p.number + ',' + p.email + '\n')
    f.close()


if __name__ == "__main__":
    # dictionary to store contact information
    contact_list = {
            
    }

    # tries to open file and populate the contact_list dictionary
    # with the contents of the file using the last names as the key
    try:
        f = open("contacts.txt", "r")
        for line in f:
            currentline = line.strip().split(",")
            p = Person(currentline[1], currentline[0], currentline[2], currentline[3])
            contact_list[p.last_name] = p
        f.close()
    except:
        contact_list = {

        }

    # dictionary to use the user input from the main menuu to 
    # call the function the user wants
    switcher = {
        'a': add_person,
        'd': delete_person,
        'f': find_person,
        'l': list_all_people,
        's': save_list,
        'e': "",
    }

    while True:
        ans = display_menu()
        if ans == 'e':
            break
        else:
            try:
                func = switcher.get(ans, 'invalid')
                func(contact_list)
            except:
                print("Invalid Input!!")

