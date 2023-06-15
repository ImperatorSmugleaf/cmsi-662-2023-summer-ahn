/**
 * Author: Kieran Ahn
 * A small node.js application that implements the AES-256-CBC encryption algorithm.
 */

import { createCipheriv, createDecipheriv } from "crypto"

const argv = process.argv.slice(2)
const encryptionSwitch = argv[0]
const message = argv[1]
const key = argv[2]
const initializationVector = argv[3]

const AES_256_CBC = "aes-256-cbc"

const makeCipher = (encryptionSwitch) => {
    const makeBuffers = (key, initializationVector) => {
        let keyBuffer
        let initializationVectorBuffer

        try {
            keyBuffer = Buffer.from(key.normalize(), "utf-8")
        } catch (error) {
            throw new Error(
                `Error encoding ${key}. Please ensure all input is valid utf-8 strings.`
            )
        }

        try {
            initializationVectorBuffer = Buffer.from(
                initializationVector.normalize(),
                "utf-8"
            )
        } catch (error) {
            throw new Error(
                `Error encoding ${initializationVector}. Please ensure all input is valid utf-8 strings.`
            )
        }
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
validate(key.length == 32, "Encryption keys must be 32 bytes long.")
validate(
    initializationVector.length == 16,
    "Initialization vectors must be 16 bytes long."
)

const { cipher, isEncoding } = makeCipher(encryptionSwitch)({
    algorithm: AES_256_CBC,
    key: key,
    initializationVector: initializationVector,
})

const encodedMessage = isEncoding
    ? () => {
          let encoding = cipher.update(
              Buffer.from(message.normalize()),
              "utf-8",
              "hex"
          )
          encoding += cipher.final("hex")
          return encoding
      }
    : () => {
          let decoding = cipher.update(message, "hex", "utf-8")
          decoding += cipher.final("utf-8")
          return decoding
      }

console.log(encodedMessage())
