import socket

message = input("enter your message: ")


key = "asdfghjklqwertyuiopzxcvbnm1234567890!@#$%^&*()_+ .,"
val = key[:: -1]

encrypter = dict(zip(key,val))

encryptedMessage = "".join(encrypter[letter] for letter in message)
print(encryptedMessage)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),3041))

s.listen(5)

while True:
    clt, adr = s.accept()
    clt.send(bytes(encryptedMessage,"utf-8"))


