MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }

code = ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"


def morse_decoder(code):
    text = code.split('   ')
    decrypt = ""
    for i in text:
        words = i.split(' ')
        for word in words:
            decrypt += MORSE.get(word)
        decrypt += ' '
    if decrypt[0].isalpha():
        return decrypt.capitalize().strip()
    else:
        return decrypt.strip()

# def morse_decoder(code):
#     words = code.split("   ")
#     result = ""
#     for word in words:
#         symbols = word.split()
#         for symbol in symbols:
#             result += MORSE[symbol]
#         result += " "
#     if result[0].isalpha():
#        result = result[0].upper() + result[1:]
#     return result.strip()

print(morse_decoder(code))
