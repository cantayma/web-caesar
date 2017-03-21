import string

def alphabet_position(letter):
    """
    receives a letter, returns 0-based numerical position in the alphabet;
    case-sensitive; assumes letters only input
    """

    if letter in string.ascii_uppercase:
        position = string.ascii_uppercase.find(letter)

    elif letter in string.ascii_lowercase:
        position = string.ascii_lowercase.find(letter)

    return position

def rotate_character(char, rot):
    """
    recieves a string, char, and an integer, rot, and returns a new string
    that is the character after it is rotated through the alphabet by rot
    """

    if char in string.ascii_uppercase:
        newChar = string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    elif char in string.ascii_lowercase:
        newChar = string.ascii_lowercase[(alphabet_position(char) + rot) % 26]
    else:
        newChar = char

    return newChar

def encrypt(text, rot):
    """
    receives a string, text and an int, rot, and returns the encrypted text by
    rotating each character in text by rot positions
    """

    encryptedText = ""

    for aLetter in text:
        encryptedText += rotate_character(aLetter, rot)

    return encryptedText
