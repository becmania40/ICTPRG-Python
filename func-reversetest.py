def reverse_name(first,last):
    print(last,first)

#reverse_name("Fred","Smith")

#reverse_name("Sally","Wong")

def test_reverse_name():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print("Your name reversed: ")
    reverse_name(first_name,last_name)

test_reverse_name()