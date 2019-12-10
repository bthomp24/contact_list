# Brandon Thompson
# Contact List for Software Engineering IV Final

class Person():
    def __init__(self, first_name, last_name, number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

def display_menu():
    print("\n\t Main Menu\n")
    ans = input("""    A - Add Person
    D - Delete Person
    F - Find and Display Person
    L - List all People
    S - Save List
    E - Exit\n
    Enter Choice:""")

    return ans

def menu_choice(ans):

    switcher = {
        'a': add_person(contact_list)
    }
    switcher.get(ans, "Invalid Input!!")

def add_person(self):
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    number = input("Enter phone number:")
    email = input("Enter email address:")

    p = Person(first_name, last_name, number, email)
    contact_list[p.last_name] = p

if __name__ == "__main__":
    bt = Person("Brandon", "Thompson", "2146688475", "bthomp24@gmail.com")
    contact_list = {
        bt.last_name : bt,
    }

    ans = display_menu()
    menu_choice(ans)

    for x, y in contact_list.items():
        print(x, y)
