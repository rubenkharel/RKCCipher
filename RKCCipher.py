from termcolor import colored
def encryption_rotation(non_rotated_message):
    if not len(non_rotated_message)%2 == 0:
        non_rotated_message += " "
    linewidth=2
    rotation=""
    i = 0
    l=[]
    for i, x in enumerate(non_rotated_message):
        if i%linewidth ==0:
            l.append([])
        l[-1].append(x)
    for i in reversed(range(linewidth)):
        for x in reversed(l):
            rotation += x[i]
    return rotation
def decryption_rotation(message_encrypted):
    message_encrypted = ''.join(reversed(message_encrypted))
    length = len(message_encrypted)
    half = length/2
    if length%2 == 0:
        f_half = message_encrypted[:int(half)]
        l_half = message_encrypted[int(half):]
    else:
        f_half = message_encrypted[:int(half)+1]
        l_half = message_encrypted[int(half)+1:]
    decrypted_message = ""
    if length%2 == 0:
        for x in range(int(half)):
            for i in range(2):
                if i == 0:
                    decrypted_message += f_half[x]
                else:
                    decrypted_message += l_half[x]
    else:
        for x in range(int(half)-1):
            for i in range(2):
                if i == 0:
                    decrypted_message += f_half[x]
                elif len(l_half)%2 != 0 and i == 1 :
                    decrypted_message += l_half[x+1]
                else:
                    decrypted_message += l_half[x]
    return decrypted_message

def Encrypt():
    key = input("Enter your key: ")
    message = input("Enter your message: ")
    abc = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    abcy = ""
    abcx = abc
    for i in range(len(abcx)):
        abcy = abcx
        for x in key:
            if x == abc[i]:
                abcx = abcx.replace(x,"")
    key = ''.join([j for i, j in enumerate(key) if j not in key[:i]])
    key_final = key.replace(" ","")
    swapped = key_final+abcy
    print(colored("This is the original alphabets not altered:","red"))
    print(">> ",colored(abc, "green"))
    print(colored("These alphabets are altered by keys provided:","red"))
    print(">> ",colored(key_final,"red")+colored(abcy,"green"))
    encrypted_message = ""

    for i in message:
        index = abc.find(i)
        if i == " ":
            encrypted_message += i
        else:
            next_char = swapped[int(index)]
            encrypted_message += next_char
    print(colored("This is cyphered text without rotation:","red"))
    print(">> ",colored(encrypted_message,"green"))
    print(colored("This is cyphered text after rotation:", "red"))
    print(">> ", colored(encryption_rotation(encrypted_message), "green"))


def Decrypt():
    key = input("Enter your key: ")
    message = input("Enter your message: ")
    message = decryption_rotation(message)
    print(colored("This is cyphered text after rotation:", "red"))
    print(">> ", colored(message, "green"))
    abc = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    abcy = ""
    abcx = abc
    for i in range(len(abcx)):
        abcy = abcx
        for x in key:
            if x == abc[i]:
                abcx = abcx.replace(x, "")
    key = ''.join([j for i, j in enumerate(key) if j not in key[:i]])
    key_final = key.replace(" ", "")
    swapped = key_final + abcy
    print(colored("This is the original alphabets not altered:", "red"))
    print(">> ", colored(abc, "green"))
    print(colored("These alphabets are altered by keys provided:", "red"))
    print(">> ", colored(key_final, "red") + colored(abcy, "green"))
    decrypted_message = ""
    for i in message:
        index = swapped.find(i)
        if i == " ":
            decrypted_message += i
        else:
            next_char = abc[int(index)]
            decrypted_message += next_char
    print(colored("This is cyphered text:","red"))
    print(">> ",colored(decrypted_message,"green"))
print("___________________ENCRYPTION___________________")
Encrypt()
print("___________________DECRYPTION___________________")
Decrypt()
