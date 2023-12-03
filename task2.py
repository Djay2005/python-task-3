import random
import string

def generate_password(length=12):
    """
    Generate a random password with a specified length.

    :param length: Length of the password (default is 12)
    :return: Random password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords=5, length=12):
    """
    Generate multiple random passwords.

    :param num_passwords: Number of passwords to generate (default is 5)
    :param length: Length of each password (default is 12)
    :return: List of random passwords
    """
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Welcome to the Password Generator!")

    try:
        password_length = int(input("Enter the desired length for the password(s): "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
        return

    passwords = generate_multiple_passwords(num_passwords, password_length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
