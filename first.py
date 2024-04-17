# Define a dictionary to store user credentials
users = {
    "javed": "javed01",
    "nishant": "nishant02",
    "ananta": "ananta03",
    "prince": "prince04"
}

# Define a dictionary to store voting results
votes = {
    "Lok sabha ": 0,
    "Vidhan sabha ": 0,
    "Municipal elections ": 0
}
# Ask the user for their age
age = int(input("Please enter your age: "))

# Check if the user is 18 or older
if age < 18:
    print("You are not old enough to enter. Goodbye!")
    exit()
else:
    print("Welcome! You can enter.")

# Function to handle user login
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in users and users[username] == password:
            print("Login successful!")
            main_menu()
        else:
            print("Invalid username or password. Please try again.")

# Function to display the main menu
def main_menu():
    while True:
        print("******WELCOME TO VOTING PORTAL*****")
        print("\nMain Menu:")
        print("1. ***Lok sabha***")
        print("2. ***Vidhan sabha*** ")
        print("3. ***Municipal elections*** ")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            option1()
        elif choice == 2:
            option2()
        elif choice == 3:
            option3()
    
        elif choice == 4:
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display the sub-menu for Option 1
def option1():
    while True:
        print("\nOption 1 Menu:")
        print("1.Sunil Soren")
        print("2. Rahul Gandhi")
        print("3. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("You have selected Sunil Soren ")
            break
        elif choice == 2:
            print("You have selected Rahul Gandhi ")
            break
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display the sub-menu for Option 2
def option2():
    while True:
        print("\nOption 2 Menu:")
        print("1. Sanjay Singh")
        print("2.Mausam Noor")
        print("3. Back to Main Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("You have selected Sanjay Singh")
            break
        elif choice == 2:
            print("You have selected Mausam Noor")
            break
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display the sub-menu for Option 3
def option3():
    while True:
        print("\nOption 3 Menu:")
        print("1. Sunita Dayal")
        print("2. Umesh Gautam ")
        print("3. Pramila Pandey")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("You have selected Sunita Dayal")
            break
        elif choice == 2:
            print("You have selected Umesh Gautam")
            break
        elif choice == 3:
            print("you have selected Pramila Pandey") 
            break
        else:
            print("Invalid choice. Please try again.")

 #Function to handle voting
def vote():
    while True:
        print("\nVoting Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            votes["option1"] = 1
            print("Thank you for voting!")
            break
        elif choice == 2:
            votes["option2"] = 2
            print("Thank you for voting!")
            break
        elif choice == 3:
            votes["option3"] = 3
            print("Thank you for voting!")
            break
        else:
            print("Invalid choice. Please try again.")

          
# Call the login function to start the system
login()
