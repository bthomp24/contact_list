# Brandon Thompson
# Contact List for Software Engineering IV Final

class Person():
    def __init__(name, number, email):
        self.name = name
        self.number = number
        self.email = email


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
