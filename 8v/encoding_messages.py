from cryptography.fernet import Fernet


# key = Fernet.generate_key()
# print(type(key))
# print(key)
# print(key[0])

# file = open('key.key', 'wb')
# file.write(key)
# file.close()

file = open('key.key', 'rb')
f_key = file.read()
file.close()
print(f_key)

fernet = Fernet(f_key)
#print(type(fernet))

message = "secret message"

encMessage = fernet.encrypt(message.encode('utf-8'))
print(encMessage)

decMessage = fernet.decrypt(encMessage).decode('utf-8')
print(decMessage)
print(type(decMessage))