def error():
    print('error')
    exit(0)


def split_join(symbol, string):
    s = string[:]
    if symbol is None:
        s = s.split()
    else:
        s = s.split(symbol)
    s = ''.join(s)
    return s


number = input()
number.strip()
number = split_join(None, number)

if number[0] == '-' or number[-1] == '-':
    error()

if '--' in number:
    error()

number = split_join('-', number)

brackets_balance = 0
for symb in number:
    if symb == '(':
        brackets_balance += 1
    elif symb == ')':
        brackets_balance -= 1

    if brackets_balance < 0:
        error()

if brackets_balance != 0:
    error()

if number.count('(') > 1:
    error()

number = split_join('(', number)
number = split_join(')', number)

if not((len(number) == 11 and number[0] == '8') or (len(number) == 12 and number[:2] == '+7')):
    error()
elif number[0] == '8':
    number = "+7" + number[1:]

print(number)
