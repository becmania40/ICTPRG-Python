def get_fullname():
    first_name = input("enter first name: ")
    last_name = input("Enter last name: ")

    return first_name, last_name

def get_fullname_test():
    first, last = get_fullname()
    print("first name: " + first)
    print("last name: " + last) 

get_fullname_test()
