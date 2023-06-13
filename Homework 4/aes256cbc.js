/**
 * Author: Kieran Ahn
 * A small node.js application that implements the AES-256-CBC encryption algorithm.
 */

import { createCipheriv, createDecipheriv } from "crypto"

const argv = process.argv.slice(2)
const AES_256_CBC = "aes-256-cbc"

const makeCipher = (encryptionSwitch) => {
    const makeBuffers = (key, initializationVector) => {
        const keyBuffer = Buffer.from(key.normalize(), "utf-8")
        const initializationVectorBuffer = Buffer.from(
            initializationVector.normalize(),
            "utf-8"
        )
        return [keyBuffer, initializationVectorBuffer]
    }

    switch (encryptionSwitch) {
        case "-d":
            return ({ algorithm, key, initializationVector }) => {
                return {
                    cipher: createDecipheriv(
                        algorithm,
                        ...makeBuffers(key, initializationVector)
                    ),
                    isEncoding: false,
                }
            }
        case "-e":
            return ({ algorithm, key, initializationVector }) => {
                return {
                    cipher: createCipheriv(
                        algorithm,
                        ...makeBuffers(key, initializationVector)
                    ),
                    isEncoding: true,
                }
            }
        default:
            throw new Error("Encryption/decryption switch must be either -e or -d.")
    }
}
const validate = (condition, message) => {
    if (!condition) {
        throw new Error(message)
    }
}

if (argv.length !== 4) {
    console.log(
        "Usage: node aes256cbc.js [-e/-d] [message] [key] [initialization vector]"
    )
    process.exit()
}
validate(argv[2].length == 32, "Encryption keys must be 32 bytes long.")
validate(argv[3].length == 16, "Initialization vectors must be 16 bytes long.")

const { cipher, isEncoding } = makeCipher(argv[0])({
    algorithm: AES_256_CBC,
    key: argv[2],
    initializationVector: argv[3],
})

const message = isEncoding
    ? () => {
          let encoding = cipher.update(
              Buffer.from(argv[1].normalize()),
              "utf-8",
              "hex"
          )
          encoding += cipher.final("hex")
          return encoding
      }
    : () => {
          let decoding = cipher.update(argv[1], "hex", "utf-8")
          decoding += cipher.final("utf-8")
          return decoding
      }

console.log(message())
