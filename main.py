def encript(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def decript(chipertext, key):
    return encript(chipertext, key)

def main():
    # fungsi enkripsi
    plaintext = str(input("Masukkan plaintext: "))
    key = 'ABC'

    print("Plaintext: ", plaintext)
    print("Enkripsi: ", encript(plaintext, key))

    # fungsi dekripsi
    chipertext = str(input("Masukkan chippertest: "))
    key = "ABC"

    print("Chipertext: ", chipertext)
    print("Dekripsi: ", decript(chipertext, key))

main()