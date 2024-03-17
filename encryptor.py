from string import ascii_letters, punctuation, digits


def get_message_input():
    message = input("Please type the message you want to encrypt:")
    return message


def get_shift_factor_input():
    shift_factor = input("Please enter the desired shift factor:")
    while not shift_factor.isdigit():
        shift_factor = input("Please enter a number to represent the desired shift factor:")
    shift_factor = int(shift_factor)
    # Ensure that any shift factor will not overwhelm
    while shift_factor > 95:
        shift_factor -= 95
    return shift_factor


def encrypt(message, shift_factor):
    abc = (ascii_letters + punctuation + digits + " ") * 2
    encrypted_message = "".join([abc[abc.find(char) + shift_factor] for idx, char in enumerate(message)])
    return encrypted_message


def main():
    message = get_message_input()
    encrypted_message = encrypt(message, get_shift_factor_input())
    print(f"Your original message is {message}.\nYour encrypted message is: {encrypted_message}.")


if __name__ == "__main__":
    main()
