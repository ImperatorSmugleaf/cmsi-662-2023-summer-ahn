# Author: Kieran Ahn
# A small demonstration of an Auto-Key Vigenère cipher using the ciphertext as
# the key

cipher = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}

plaintext = "TAKEACOPYOFYOURPOLICYTONORMAWILCOXONTHETHIRDFLOOR"
key = "QUARK"
ciphertext = ""
for i in range(len(plaintext)):
    encodedLetter = list(cipher.keys())[
        (cipher[plaintext[i]] + cipher[key[i]]) % 26]
    if len(key) < len(plaintext):
        key += encodedLetter
    ciphertext += encodedLetter
print(f'KEY: {key}')
print(f'CIPHERTEXT: {ciphertext}')
