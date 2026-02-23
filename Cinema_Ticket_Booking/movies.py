def show_movies():
    print("\nAvailable Movies:")
    print("1. Avengers")
    print("2. Batman")

def select_movie():
    choice = input("Select movie (1 or 2): ")
    
    if choice == "1":
        return "Avengers"
    elif choice == "2":
        return "Batman"
    else:
        print("Invalid choice")
        return None
def show_movies():
    print("\nAvailable Movies:")
    print("1. Avengers")
    print("2. Batman")

def select_movie():
    choice = input("Select movie (1/2): ")

    if choice == "1":
        return "Avengers"
    elif choice == "2":
        return "Batman"
    else:
        print("Invalid choice")
        return None    