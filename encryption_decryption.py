def caesar_cipher(text, shift, encrypt=True):
    result = ""

    if not encrypt:
        shift = -shift  # Reverse shift for decryption

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  

    return result

print("Caesar Cipher - Encrypt & Decrypt")

text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(text, shift, encrypt=True)
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, shift, encrypt=False)
print(f"Decrypted: {decrypted_text}")
