def caesar_encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    # Decrypt by shifting backwards
    return caesar_encrypt(ciphertext, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Type 'E' to encrypt or 'D' to decrypt: ").strip().upper()
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for the shift value.")

    if choice == 'E':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'D':
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please select 'E' or 'D'.")

if __name__ == "__main__":
    main()
