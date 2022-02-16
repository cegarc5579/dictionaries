# Problem 2 ENCRYPTION QUESTION


def main():
    codes = {
        "A": "9",
        "a": "$",
        "B": "3",
        "b": "!",
        "C": "W",
        "c": "#",
        "D": "*",
        "d": "[",
        "E": "@",
        "e": "s",
        "F": "6",
        "f": "?",
        "G": "<",
        "g": ">",
        "H": "^",
        "h": "0",
        "I": "|",
        "i": "~",
        "J": "u",
        "j": "5",
        "K": "w",
        "k": "%",
        "L": "Y",
        "l": "-",
        "M": "=",
        "m": "1",
        "N": "2",
        "n": "7",
        "O": "4",
        "o": "T",
        "P": "x",
        "p": "A",
        "Q": "u",
        "q": "E",
        "R": "p",
        "r": ".",
        "S": "K",
        "s": "B",
        "T": "F",
        "t": "f",
        "U": "Q",
        "u": "d",
        "V": "N",
        "v": "y",
        "W": "o",
        "w": "O",
        "X": "P",
        "x": "&",
        "Y": "`",
        "y": ":",
        "Z": "z",
        "z": "Z",
    }
    encryption(codes)


def encryption(codes):

    message = open("info_security.txt", "r")
    message_read = message.read()

    encrypted = open("encryptedtext.txt", "w")

    for i in message_read:
        if i in codes:
            encrypted.write(codes[i])
        else:
            encrypted.write(i)

    encrypted.close()


main()
