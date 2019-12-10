# Brandon Thompson
# Contact List for Software Engineering IV Final

class Person():
    def __init__(self, first_name, last_name, number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.number}, {self.email}'

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

# def menu_choice(ans):
#     print('this is the answer - ' + ans)

#     switcher[ans]

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

    switcher = {
        'a': add_person,
        'e': "",
    }

    while True:
        ans = display_menu()
        if ans == 'e':
            break
        else:
            switcher[ans](contact_list)

    for x in contact_list:
        print(contact_list[x])
