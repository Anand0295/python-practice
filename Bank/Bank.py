database = {"user1": ["User@123", "1234", 1000], "user2": ["Python#123", "5678", 0]}


def validate_password(password):
    upper = 0
    lower = 0
    special = 0
    digit = 0

    for i in password:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
        elif not i.isalnum():
            special += 1

    if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
        return True
    return False


def validate_pin(pin):
    if pin.isdigit() and len(pin) == 4:
        return True
    return False


def signup():
    username = input("enter your new username: ")
    if username in database:
        print("Sorry, Username already Exists!!")
    else:
        password = input("enter your new password: ")
        if not validate_password(password):
            print("Enter a valid password.")
            return
        confirm_password = input("Confirm you Password: ")
        if password != confirm_password:
            print("passwords do not match!!")
            return
        pin = input("enter your new pin: ")
        if not validate_pin(pin):
            print("Enter a valid pin.")
            return
        confirm_pin = input("Confirm your pin: ")
        if pin != confirm_pin:
            print("pins do not match!!")
            return
        amount = int(input("enter the opening amount: "))
        if amount >= 500:
            database[username] = [password, pin, amount]
        else:
            print("minimum deposit is Rs.500")


def login():
    username = input("Enter your username: ")
    if username not in database:
        print("Username does not Exist!!")
    else:
        password = input("Enter your password: ")
        if password != database[username][0]:
            print("Wrong Password!!")
        else:
            while True:
                print("1. Deposit\n2. Withdraw\n3. Balance Check\n4. Exit")
                op = int(input("Choose your option: "))
                if op == 1:
                    deposit(username)
                elif op == 2:
                    withdraw(username)
                elif op == 3:
                    balance(username)
                elif op == 4:
                    print("Good Bye!")
                    break
                else:
                    print("Invalid Option.")


def deposit(username):
    print("\n           DEPOSIT           ")
    pin = input("\nenter your pin: ")
    if pin != database[username][1]:
        print("Pin not matching!!")
    else:
        amount = int(input("Enter amount you are depositing: "))
        if amount > 0:
            database[username][2] = database[username][2] + amount
            print(
                f"Amount deposited successfully!!\n New Balance: Rs.{database[username][2]}"
            )


def withdraw(username):
    print("\n           WITHDRAW            ")
    pin = input("\nenter your pin: ")
    if pin != database[username][1]:
        print("Pin not matching!!")
    else:
        amount = int(input("Enter amount you are withdrawing: "))
        if amount > 0 and amount <= database[username][2]:
            database[username][2] = database[username][2] - amount
            print(
                f"Amount withdrawn successfully!!\n New Balance: Rs.{database[username][2]}"
            )
        else:
            print("Insufficient Balance!!")


def balance(username):
    print("\n           BALANCE           ")
    pin = input("\nenter your pin: ")
    if pin != database[username][1]:
        print("Pin not matching!!")
    else:
        print(f"Current Balance: Rs.{database[username][2]}")


print("Welcome to the Bank")
print("1. Login \n2. Signup")
op = input("Choose: ")
if op == "1":
    login()
elif op == "2":
    signup()
else:
    print("Invalid option")
