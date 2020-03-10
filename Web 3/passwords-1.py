DIGITS = "0123456789"

PC_SYMBOLS_LATIN = "QWERTYUIOP%%ASDFGHJKL%%ZXCVBNM"
PC_SYMBOLS_CYRILLIC = "ЙЦУКЕНГШЩЗХЪ%%ФЫВАПРОЛДЖЭ%%ЯЧСМИТЬБЮ"

MAC_SYMBOLS_LATIN = "QWERTYUIOP%%ASDFGHJKL%%ZXCVBNM"
MAC_SYMBOLS_CYRILLIC = "ЙЦУКЕНГШЩЗХЪ%%ФЫВАПРОЛДЖЭЁ%%ЯЧСМИТЬБЮ"


def error():
    print('error')
    exit(0)


password = input()

for digit in DIGITS:
    if digit in password:
        break
else:
    error()

if password.isalpha():
    error()

if password.isdigit():
    error()

if len(password) <= 8:
    error()

if password.lower() == password or password.upper() == password:
    error()


password = password.upper()

for index in range(len(password) - 2):
    substr = password[index:index + 3]
    if (substr in PC_SYMBOLS_LATIN
            or substr in PC_SYMBOLS_CYRILLIC
            or substr in MAC_SYMBOLS_LATIN
            or substr in MAC_SYMBOLS_CYRILLIC):
        error()

print('ok')
