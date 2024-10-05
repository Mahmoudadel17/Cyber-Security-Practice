import socket


decryptedKey = input("enter the encryption key: ")


if len(decryptedKey) == 51:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((socket.gethostname(),3041))

    message = s.recv(1000)
    message = message.decode("utf-8")

    val = decryptedKey[:: -1]

    decrypter = dict(zip(val,decryptedKey))

    message = "".join(decrypter[letter] for letter in message)
    print(message)
else:
    print("you are not autherized to show this content ^_^.")

