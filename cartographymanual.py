encryption_dict = {
    'a': '3', 'b': '#', 'c': 'w', 'd': 'r', 'e': '9',
    'f': '!', 'g': 'e', 'h': 'j', 'i': 'y', 'j': 'x',
    'k': 'b', 'l': 'k', 'm': '4', 'n': '%', 'o': 'l',
    'p': '2', 'q': '&', 'r': 'n', 's': 'a', 't': 'v',
    'u': '5', 'v': 'p', 'w': 'u', 'x': '*', 'y': '7',
    'z': 'f'
}
#____________________________________________________________________________________________________________________________________________
while True:
    print("\nSelect an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

#----------------------------------------------- ENCRYPTION ------------------------------------------
    if choice == '1':
        user1 = input(str('Enter your message to encrypt: '))
        translate1 = ""

        for letter1 in user1:
            for key,value in encryption_dict.items():
                if letter1 == key:
                    translate1 = translate1+str(value)
                    break
            else:
                translate1 = translate1+letter1

        print("Encrypted message is: ",translate1)

#---------------------------------------------- DECRYPTION --------------------------------------------
    elif choice == '2':
        user2 = input(str('Enter your message to descrypt: '))
        translate2 = ""

        for letter2 in user2:
            for key,value in encryption_dict.items():
                if letter2 == value:
                    translate2 = translate2+str(key)
                    break
            else:
                translate2 = translate2+letter2

        print("Decrypted message is: ",translate2)
#-------------------------------------------------------------------------------------------------------        

    elif choice == '3':
        print("Exiting the program")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
#_________________________________________________________________________________________________________________________________________________