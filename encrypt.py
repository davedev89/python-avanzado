def decrypt(func):
    def wrapper(text: str, shift_number: int) -> str:
        shift_number = shift_number * (-1)
        return func(text, shift_number)
    return wrapper

def encrypt(string: str, shift_number: int) -> str:
    alphabet_lower = "abcdefghijklmnñopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numbers = "0123456789"

    encrypted = ""  # Encrypted string

    for charact in string:
        if charact.islower() and (charact in alphabet_lower):
            index = alphabet_lower.find(charact)
            index = (index + shift_number) % 27
            encrypted += alphabet_lower[index]
        elif charact.isupper() and (charact in alphabet_upper):
            index = alphabet_upper.find(charact)
            index = (index + shift_number) % 27
            encrypted += alphabet_upper[index]
        elif charact in numbers:
            index = numbers.find(charact)
            index = (index + shift_number) % 10
            encrypted += numbers[index]
        else:
            encrypted += charact # for special characters
    
    return encrypted

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    shifts_number = int(input("Enter the number of shifts: "))
    encrypted_text = encrypt(text, shifts_number)
    print("\n Encrypted text: " + encrypted_text)

    # Decrypt process
    decrypt_function = decrypt(encrypt)
    decrypt_text = decrypt_function(encrypted_text, shifts_number)
    print("\n Decrypted text: " + decrypt_text)