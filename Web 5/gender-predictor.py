import argparse
from collections import defaultdict


def interval(val, min, max, default):
    if val < min or val > max:
        return default
    return val


DEFAULT_DICT = defaultdict(lambda: 50)
DEFAULT_DICT["melodrama"] = 0
DEFAULT_DICT["football"] = 100
DEFAULT_DICT["other"] = 50

parser = argparse.ArgumentParser()
parser.add_argument("--barbie", type=int, nargs=1, default=[50], required=False)
parser.add_argument("--cars", type=int, nargs=1, default=[50], required=False)
parser.add_argument("--movie", type=str, nargs=1, default=["other"], required=False)

args = parser.parse_args()

barbie = interval(args.barbie[0], 0, 100, 50)
cars = interval(args.cars[0], 0, 100, 50)
movie = DEFAULT_DICT[args.movie[0]]

boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - boy

print(f'boy: {boy}')
print(f'girl: {girl}')
