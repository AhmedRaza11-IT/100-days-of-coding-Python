# Exercise 3

def encrypt_message(message, shift):
    """Encrypt a message using Caesar cipher."""
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if it's a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase or lowercase
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # Keep non-letters as is
    return encrypted_message


def decrypt_message(encrypted_message, shift):
    """Decrypt a message using Caesar cipher."""
    return encrypt_message(encrypted_message, -shift)


# Main program
if __name__ == "__main__":
    print("Secret Messaging System")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().lower()

    if choice in ['e', 'encrypt']:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        encrypted = encrypt_message(message, shift)
        print(f"Encrypted Message: {encrypted}")
    elif choice in ['d', 'decrypt']:
        encrypted_message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        decrypted = decrypt_message(encrypted_message, shift)
        print(f"Decrypted Message: {decrypted}")
    else:
        print("Invalid choice. Please select either Encrypt or Decrypt.")

