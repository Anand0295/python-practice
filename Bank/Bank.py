database = {"user1": ["user@123", 1234, 1000], "user2": ["python#123", 5678, 0]}


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
        elif i.isspecial():
            special += 1
        elif i.isdigit():
            digit += 1

    if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
        return True
    return False

def validate_pin(pin):
    if pin.isdigit() and len(pin)==4:
        