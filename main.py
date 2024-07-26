def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65) #ord() used to convert into ascii values 
            #here apply caeser cipher algo and this is formula for encypting and decrypting 
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  

def main():
    choice = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message: ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'encrypt':
        print(f"Encrypted message: {encrypt(text, shift)}")
    elif choice == 'decrypt':
        print(f"Decrypted message: {decrypt(text, shift)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
