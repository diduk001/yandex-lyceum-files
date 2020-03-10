import argparse

parser = argparse.ArgumentParser()

parser.add_argument("values", nargs='*')
parser.add_argument("--sort", action="store_true")

args = parser.parse_args()

lst = args.values

d = dict()

for string in lst:
    key, val = string.split('=')
    d[key] = val

keys = list(d.keys())
if args.sort:
    keys.sort()

for key in keys:
    print(f"Key: {key} Value: {d[key]}")
