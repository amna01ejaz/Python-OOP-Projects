def login():
    name = input("Enter your name: ")
    
    if name:
        print("Welcome", name)
        return True
    else:
        print("Invalid name")
        return False
def get_user():
    name = input("Your full name: ")
    return name