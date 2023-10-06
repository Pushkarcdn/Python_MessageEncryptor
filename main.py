import random
import string

while True:

    def encryption():
        ran1 = random.choices(string.ascii_lowercase, k=3)
        ran1 = ran1[0] + ran1[1] + ran1[2]
        ran2 = random.choices(string.ascii_lowercase, k=3)
        ran2 = ran2[0] + ran2[1] + ran2[2]

        message = input("\n\t Enter Your Message: ")
        message = message.split()
        emsg = []

        password = input("\n\t Create a password: ")
        password = password[::-1]
        password = ran2 + ran1 + password + ran1

        for i in message:
            length = len(i)
            if length < 3:
                a = i[::-1]
                emsg.append(a)
            if length > 2:
                a = i
                a = a[1:] + a[0]
                a = ran1 + a + ran2
                emsg.append(a)

        emsg = " ".join(emsg)
        emsg = password + " " + emsg
        return emsg

    def decryption():
        message = input("\n\tPaste the encrypted message here: ")
        password1 = input("\n\tEnter the password to decrypt the message: ")
        message = message.split()
        dmsg = []

        password = message[0]
        message = message[1:]

        password = password[6:-3]
        password = password[::-1]

        if password1 == password:
            for i in message:
                length = len(i)
                if length < 3:
                    a = i
                    a = a[::-1]
                    dmsg.append(a)
                if length > 2:
                    a = i
                    a = a[3:-3]
                    a = a[-1] + a[:-1]
                    dmsg.append(a)

            dmsg = " ".join(dmsg)
            return dmsg
        else:
            print("Incorect Password")

    print("\n\n\t !!! WELCOME TO PUSHKAR's ENCRYPTIONS !!!")
    print("\n")

    print("  What's on your mind ? \n\n \t 1. Encrypt Message \n\t 2. Decrypt Message")

    answer = int(input("\n  Choose one (1/2) : "))

    if answer == 1:
        emsg = encryption()
        print(f"\n\tYour message in encrypted form is: {emsg} \n")

    if answer == 2:
        dmsg = decryption()
        print(f"\n\tYour message is: {dmsg} \n")

    choise = input(
        "\n\t Do you want to encrypt or decrypt any other message ? (y/n) : "
    )
    if choise == "n" or choise == "N":
        input("\n\t Thanks for using. \n")
        break
exit()
