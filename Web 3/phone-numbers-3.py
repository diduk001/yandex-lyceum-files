class NumberError(Exception):
    pass


class FormatError(NumberError):
    pass


class LengthError(NumberError):
    pass


number = input()
try:

    number.strip()

    if '(' in number and ')' not in number or '(' not in number and ')' in number:
        raise FormatError

    number = number.replace('(', ' ', 1)
    number = number.replace(')', ' ', 1)

    if '--' in number:
        raise FormatError

    if number[0] == '-' or number[-1] == '-':
        raise FormatError

    number = number.replace('-', ' ')

    number = number.split()
    number = ''.join(number)

    if number[0] == "8":
        number = "+7" + number[1:]
    elif number[:2] == "+7":
        pass
    else:
        raise FormatError

    if not number[1:].isdigit():
        raise FormatError

    if len(number) != 12:
        raise LengthError


except FormatError:
    print("неверный формат")

except LengthError:
    print("неверное количество цифр")

else:
    print(number)
