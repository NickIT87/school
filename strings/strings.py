greeting = 'hello'
greeting_b = b'hello'
greeting_ba = bytearray(greeting_b)

print(type(greeting))
print(type(greeting_b))
print(type(greeting_ba))
print(len(greeting_ba))
print(greeting_ba[0])
print(bytes(greeting_ba[0]))
print(bin(greeting_ba[0]))