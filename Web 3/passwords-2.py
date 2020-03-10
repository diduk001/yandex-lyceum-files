class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


DIGITS = "0123456789"

PC_SYMBOLS_LATIN = "QWERTYUIOP%%ASDFGHJKL%%ZXCVBNM"
PC_SYMBOLS_CYRILLIC = "ЙЦУКЕНГШЩЗХЪ%%ФЫВАПРОЛДЖЭ%%ЯЧСМИТЬБЮ"

MAC_SYMBOLS_LATIN = "QWERTYUIOP%%ASDFGHJKL%%ZXCVBNM"
MAC_SYMBOLS_CYRILLIC = "ЙЦУКЕНГШЩЗХЪ%%ФЫВАПРОЛДЖЭЁ%%ЯЧСМИТЬБЮ"


def check_password(password):
    if len(password) <= 8:
        raise LengthError

    if password.lower() == password or password.upper() == password:
        raise LetterError

    for digit in DIGITS:
        if digit in password:
            break
    else:
        raise DigitError

    password = password.upper()

    for index in range(len(password) - 2):
        substr = password[index:index + 3]
        if (substr in PC_SYMBOLS_LATIN
                or substr in PC_SYMBOLS_CYRILLIC
                or substr in MAC_SYMBOLS_LATIN
                or substr in MAC_SYMBOLS_CYRILLIC):
            raise SequenceError

    return "ok"
