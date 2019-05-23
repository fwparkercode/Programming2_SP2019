import key

def decode(key, string):
    '''
    Decode a message using encryption key
    :param key: encryption key
    :param string: encrypted message
    :return: decoded_message
    '''
    decoded_chars = ""
    for i in range(len(string)):
        key_c = key[i % len(key)]
        decoded_c = chr(ord(string[i]) - ord(key_c) % 256)
        decoded_chars += decoded_c
    return decoded_chars


