# Author: Kieran Ahn

p = 100392089237316158323570985008687907853269981005640569039457584007913129640081
q = 90392089237316158323570985008687907853269981005640569039457584007913129640041
e = 65537
block_size = 60
message = "Scaramouche, Scaramouche, will you do the Fandango? 💃🏽"

N = p * q
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

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
