class NumberError(Exception):
    pass


number = input()
try:

    number.strip()

    if '(' in number and ')' not in number or '(' not in number and ')' in number:
        raise NumberError

    number = number.replace('(', ' ', 1)
    number = number.replace(')', ' ', 1)

    if '--' in number:
        raise NumberError

    if number[0] == '-' or number[-1] == '-':
        raise NumberError

    number = number.replace('-', ' ')

    number = number.split()
    number = ''.join(number)

    if number[0] == "8":
        number = "+7" + number[1:]
    elif number[:2] == "+7":
        pass
    else:
        raise NumberError

    if not number[1:].isdigit():
        raise NumberError

    if len(number) != 12:
        raise NumberError


except NumberError:
    print("error")

else:
    print(number)
