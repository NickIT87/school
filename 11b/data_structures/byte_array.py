text_string = "Hello, World!"
byte_array = bytes(text_string, 'utf-8')


byte_array = b'Hello, World!'
text_string = byte_array.decode('utf-8')


byte_array = bytearray(b'Hello, World!')
byte_array[0] = 72  # Change the first byte
byte_array.extend(b'!')  # Append bytes


text_string = "Hello, World!"
substring = text_string[0:5]  # Extract substring
concatenated_string = text_string + "!"  # Concatenate strings


text_string = "Hello, World!"
length = len(text_string)
uppercase_string = text_string.upper()
lowercase_string = text_string.lower()


byte_data = b'Hello, World!'
hex_representation = hex(int.from_bytes(byte_data, byteorder='big'))
print(hex_representation)


text_string = "Hello, World!"
encoded_bytes = text_string.encode('utf-8')
decoded_string = encoded_bytes.decode('utf-8')
