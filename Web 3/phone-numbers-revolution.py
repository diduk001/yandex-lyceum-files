class NumberError(Exception):
    pass


class FormatError(NumberError):
    pass


class LengthError(NumberError):
    pass


class OperatorCodeError(NumberError):
    pass


CODES = [str(i) for i in range(910, 920)] + \
        [str(i) for i in range(980, 990)] + \
        [str(i) for i in range(920, 940)] + \
        [str(i) for i in range(902, 907)] + \
        [str(i) for i in range(960, 970)]

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
    elif number[:2] in ("+7", "+359", "+55", "+1"):
        pass
    else:
        raise FormatError

    if not number[1:].isdigit():
        raise FormatError

    if len(number) != 12:
        raise LengthError

    if number[2:5] not in CODES:
        raise OperatorCodeError

except FormatError:
    print("неверный формат")

except LengthError:
    print("неверное количество цифр")

except OperatorCodeError:
    print("не определяется оператор сотовой связи")

else:
    print(number)
