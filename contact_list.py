# Brandon Thompson
# Contact List for Software Engineering IV Final

class Person():
    def __init__(self, first_name, last_name, number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def __str__(self):
        return f'{self.last_name}, {self.first_name} - {self.number}, {self.email}'

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

def add_person(self):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    number = input("Enter phone number: ")
    email = input("Enter email address: ")

    p = Person(first_name, last_name, number, email)
    contact_list[p.last_name] = p

def delete_person(self):
    last_name = input("Enter last name: ")
    del contact_list[last_name]

def find_person(self):
    print("in find")

def list_all_people(self):
    for key in sorted(contact_list):
        print(contact_list[key])

def save_list(self):
    print("in save")


if __name__ == "__main__":
    bt = Person("Brandon", "Thompson", "2146688475", "bthomp24@gmail.com")
    contact_list = {
        bt.last_name : bt,
    }

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

