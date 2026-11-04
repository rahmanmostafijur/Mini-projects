import secrets
import string

length = int(input("Enter the length of the password: "))


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


if length <= 0:
    print("Password length must be greater than 0.")
else:
    password = generate_password(length)
    print("Generated password:", password)
