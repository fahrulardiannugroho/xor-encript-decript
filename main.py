def encript(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def decript(chipertext, key):
    return encript(chipertext, key)

def main():
    plaintext = 'matakuliahkripto'
    key = 'ACD'

    print("Plaintext: ", plaintext)
    print("Enkripsi: ", encript(plaintext, key))

    chipertext = ',"0 (1-*%)(6(30.'
    key = "ACD"

    print("Chipertext: ", chipertext)
    print("Dekripsi: ", decript(chipertext, key))

main()