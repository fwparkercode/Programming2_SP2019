

# Caesar cipher

key = 5

message = "Programming 2!"

print("A", ord("A"))
print("65", chr(65))

encoded_message = ""

for letter in message:
    encoded_letter = chr(ord(letter) + key)
    encoded_message += encoded_letter

print(encoded_message)


decoded_message = ""

for letter in encoded_message:
    decoded_letter = chr(ord(letter) - key)
    decoded_message += decoded_letter

print(decoded_message)


key = "9F17B444C2141DC1EBEDEB96B48F8"

def encode(key, string):
    encoded_message = ""
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c))
        encoded_message += encoded_c
    return encoded_message


def decode(key, string):
    decoded_message = ""
    for i in range(len(string)):
        key_c = key[i % len(key)]
        decoded_c = chr(ord(string[i]) - ord(key_c))
        decoded_message += decoded_c
    return decoded_message

print(encode(key, "Francis W. Parker!"))
print(decode(key, "¸¥¥§T`Q¶®·c"))

