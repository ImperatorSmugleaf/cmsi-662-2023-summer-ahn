# Author: Kieran Ahn

p = 100392089237316158323570985008687907853269981005640569039457584007913129640081
q = 90392089237316158323570985008687907853269981005640569039457584007913129640041
e = 65537
block_size = 60
message = "Scaramouche, Scaramouche, will you do the Fandango? 💃🏽"

N = p * q
phi = (p - 1) * (q - 1)

# Code from GeeksforGeeks
def extendedEuclideanAlgorithm(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extendedEuclideanAlgorithm(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

# thanks to help from https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
d = extendedEuclideanAlgorithm(e, phi)[1]

# Encrypting
utf8message = message.encode('utf-8').hex()

messageBlocks = [utf8message[i:i+block_size*2] for i in range(0, len(utf8message), block_size*2)]

numericMessageBlocks = [int(block, 16) for block in messageBlocks]
ciphertexts = [pow(block, e, N) for block in numericMessageBlocks]
hexCiphertexts = [hex(ciphertext) for ciphertext in ciphertexts]
finalCipherText = "".join(hexCiphertexts)

# Decrypting
cipherTextInteger = int(finalCipherText, 16)
decryptedCipherTextInteger = pow(cipherTextInteger, d, N)

print(f'Original Message: {message}\n')
print(f'N = {N}\n')
print(f'd = {d}\n')
print(f'Cipher text: {finalCipherText}\n')
print(f'Decrypted message: {decryptedCipherTextInteger.to_bytes(block_size, "big").decode("utf-8")}')
