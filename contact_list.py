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
    print("\n Main Menu\n")
    print("A - Add Person\n"
        "D - Delete Person\n"
	    "F - Find and Display Person\n"
	    "L - List all People\n"
		"S - Save List\n"
		"E - Exit\n\n"
		"Enter Choice:")

if __name__ == "__main__":
    display_menu()

    bt = Person("Brandon", "Thompson", "2146688475", "bthomp24@gmail.com")
    myDict = {
        bt.last_name : bt,
    }

    print(myDict.get(bt.last_name))