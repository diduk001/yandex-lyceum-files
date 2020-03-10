import sys

args = sys.argv[1:]

sort_flag = False
if '--sort' in args:
    args.remove("--sort")
    sort_flag = True
dictionary = dict()

for arg in args:
    key, val = arg.split('=')
    dictionary[key] = val

keys = list(dictionary.keys())
if sort_flag:
    keys.sort()

for key in keys:
    print(f"Key: {key} Value: {dictionary[key]}")
