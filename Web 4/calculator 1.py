import sys

try:
    print(int(sys.argv[1]) + int(sys.argv[2]))
except IndexError:
    print(0)
except ValueError:
    print(0)
