import struct


# Varicode class for GoodPSK.
class Varicode:
    """This class implements the PSK31 varicode alphabet."""

    def encode(self, text):
        """Encodes a string to a string of varicoded bits."""
        return self.delim.join([self.characters[ch] for ch in text]) + self.delim

    def decode(self, bits):
        """Decodes a string of bits to a string of letters."""
        varicode = {value: key for key, value in self.characters.iteritems()}
        return ''.join([varicode[bit] for bit in bits.split(self.delim) if bit])

    def repeat(self, text, count):
        """returns string with 'text' repeated 'count' times"""
        return ''.join([text] * count)

    def write(self, text, filename):
        size = 8  # define size of varicode chunks, 8 for byte

        # convert text to varicode, add 8-bit 0 preamble and 1 postamble
        varicode = self.repeat('0', size) + self.encode(text) + self.repeat('1', size)
        varicode += self.repeat('1', len(varicode) % size)  # pad varicode text to whole no. of bytes

        with open(filename, 'wb') as fp:
            for index in xrange(0, len(varicode), size):            # index for traversal by chunk
                u8 = ~int(varicode[index:index+size], 2) % 2**size  # convert to unsigned byte and invert
                fp.write(struct.pack('@B', u8))                     # pack as sytem-endian binary and write to file

    delim = "00"
    characters = {
        "\n": "11101",
        " ":  "1",

        # Numbers
        "0":  "10110111",
        "1":  "10111101",
        "2":  "11101101",
        "3":  "11111111",
        "4":  "101110111",
        "5":  "101011011",
        "6":  "101101011",
        "7":  "110101101",
        "8":  "110101011",
        "9":  "110110111",

        # Symbols
        "'":  "101111111",
        "?":  "1010101111",
        "!":  "111111111",
        ";":  "110111101",
        ":":  "11110101",
        "!":  "111111111",
        "\"": "101011111",
        "#":  "111110101",
        "$":  "111011011",
        "%":  "1011010101",
        "&":  "1010111011",
        "(":  "11111011",
        ")":  "11110111",
        "*":  "101101111",
        "+":  "111011111",
        ".":  "1010111",
        ",":  "1110101",
        "-":  "110101",
        "|":  "110111011",
        "_":  "1010111111",
        "\\": "111110111",
        "/":  "110101111",
        "=":  "1010101",
        "<":  "111101101",
        ">":  "111010111",
        "[":  "1010101101",
        "]":  "111101111",

        # Lowercase
        "a": "1011",
        "b": "1011111",
        "c": "101111",
        "d": "101101",
        "e": "11",
        "f": "111101",
        "g": "1011011",
        "h": "101011",
        "i": "1101",
        "j": "111101011",
        "k": "10111111",
        "l": "11011",
        "m": "111011",
        "n": "1111",
        "o": "111",
        "p": "111111",
        "q": "110111111",
        "r": "10101",
        "s": "10111",
        "t": "101",
        "u": "110111",
        "v": "1111011",
        "w": "1101011",
        "x": "11011111",
        "y": "1011101",
        "z": "111010101",

        # Uppercase
        "A": "1111101",
        "B": "11101011",
        "C": "10101101",
        "D": "10110101",
        "E": "1110111",
        "F": "11011011",
        "G": "11111101",
        "H": "101010101",
        "I": "1111111",
        "J": "111111101",
        "K": "101111101",
        "L": "11010111",
        "M": "10111011",
        "N": "11011101",
        "O": "10101011",
        "P": "11010101",
        "Q": "111011101",
        "R": "10101111",
        "S": "1101111",
        "T": "1101101",
        "U": "101010111",
        "V": "110110101",
        "W": "101011101",
        "X": "101110101",
        "Y": "101111011",
        "Z": "1010101101",
    }
