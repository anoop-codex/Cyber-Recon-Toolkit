import string
import secrets


def generate_password():

    print("\n========== PASSWORD GENERATOR ==========\n")

    while True:

        try:
            length = int(input("Enter password length (8-64): "))

            if 8 <= length <= 64:
                break

            print("Password length must be between 8 and 64.")

        except ValueError:
            print("Please enter a valid number.")

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    print("\nGenerated Password\n")
    print(password)