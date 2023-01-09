# pylint:disable=missing-class-docstring
# pylint:disable=missing-function-docstring

from typing import Dict, Optional

MORSE_CODES = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}

MORSE_CODES_REVERSED = {v: k for k, v in MORSE_CODES.items()}


class MorseEncoder:
    def __init__(self, encryption_table: Dict[str, str], delimiter: Optional[str] = None):
        self.encryption_table = encryption_table
        self.delimiter = delimiter or " "

    def encode(self, sentence: str) -> str:
        result = []

        for letter in sentence:
            if letter != self.delimiter:
                result.append(self.encryption_table[letter.upper()])
            result.append(self.delimiter)

        return "".join(result).strip()


class MorseDecoder:
    def __init__(self, decryption_table: Dict[str, str], delimiter: Optional[str] = None):
        self.decryption_table = decryption_table
        self.delimiter = delimiter or " "

    def decode(self, sentence: str) -> str:
        result = []
        codes = sentence.split(self.delimiter)

        for letter in codes:
            if letter and letter != self.delimiter:
                result.append(self.decryption_table[letter])
            result.append(self.delimiter)

        return "".join(result).strip()
