#/usr/bin/python3

# Python-practice: Vigenère-cipher
# A program to encrypt/ decrypt message with the use of the Vigenère-
# cipher.

def create_array():
    # creates the Vigenère-array for en- /decrypting the messages and
    # returns that array in form of a list of strings.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp_string = alphabet
    array = []
    for row in range (0, len(alphabet)):
        array.append(temp_string)
        temp_string = alphabet[row+1:len(alphabet)] + alphabet[0:row+1] 
    return array

# -----------------------------------------------------------------------------

def cleanup_string(string):
    # accepts a string, removes all non-alphabetical characters and turns all
    # letters into uppcase letters. 
    # Returns the string of letters.
    temp_string =""
    for char in string:
        if char.isalpha():
            temp_string += char.upper()
    return temp_string


def create_keyphrase(key, message_length):
    # accept the key-string and the length of the cleartext message
    # removes all non-alphatical characters, turns string into uppercase
    # and multiplies the key until it reaches the length of the cleartext-
    # message. 
    # Returns the multiplied key
    key_phrase = key
    while len(key_phrase) < message_length:
        key_phrase += key
    return key_phrase[0:message_length]


def get_index(char, string):
    # accept a character and a string.
    # returns the index of the character in the string
    for i in range (0, len(string)):
        if char == string[i]:
            index = i
    return index

# -----------------------------------------------------------------------------

def encrypt_message(key, message):
    # accepts the keyphrase and a message, gets the index of a character in
    # message and returns up the encrypted character of said index
    encrypted_char = ""
    encrypted_message = ""
    for i in range (0, len(message)):
        message_index = get_index(message[i], ARRAY[0])
        for j in range(0,26):
            if ARRAY[j][0] == key[i]:
                encrypted_char = ARRAY[j][message_index]
        encrypted_message += encrypted_char
    return encrypted_message
 
def decrypt_message(key, message):
    # accepts the keyphrase and the message, gets the index of the encrypted
    # character and returns the decrypted char of said index
    crypt_index = 0
    decrypted_char=""
    decrypted_message = ""
    for i in range(0, len(message)):
        for j in range (0,26):
            if ARRAY[j][0] == key[i]:
                crypt_index = get_index(message[i], ARRAY[j])
            decrypted_char = ARRAY[0][crypt_index]
        decrypted_message += decrypted_char
    return decrypted_message

# -----------------------------------------------------------------------------

def main():
    choice = ""
    key = ""
    message = ""
    global ARRAY
    ARRAY = create_array()
    print("-----------------------------------------")
    print("             Vigenȩre cipher")
    print("-----------------------------------------\n")

    for i in range(0, len(ARRAY)):
        print(ARRAY[i])
    print("\n")

    while not (choice =="e" or choice =="d"):
        choice = input("Do you want to (e)ncrypt of (d)ecrypt a message? ")
    
    key = input("\nPlease enter the String that should be used as a key: ")
    key = cleanup_string(key)
    
    message = input("Please enter your message now: ")
    message = cleanup_string(message)
    key = create_keyphrase(key, len(message))

    if choice == "e":
        processed_message = encrypt_message(key, message)
    if choice == "d":
        processed_message = decrypt_message(key, message)
    
    print("\n")
    print(f"Cleaned key:       {key}")
    print(f"Cleaned message:   {message}")
    print("===================")
    print(f"Processed message: {processed_message}")


if __name__ == "__main__":
    main()
    
