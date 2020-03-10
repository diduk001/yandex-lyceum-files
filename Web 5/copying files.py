import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--upper", action="store_true")
parser.add_argument("--lines", type=int, default=-1)
parser.add_argument("source", type=str)
parser.add_argument("destination", type=str)

args = parser.parse_args()

src = args.source
dest = args.destination

upper_flag = args.upper
lines_n = args.lines

with open(src) as src_file:
    lines = src_file.readlines()
    if lines_n == -1:
        lines_n = len(lines)

    lines = lines[:lines_n]

    if upper_flag:
        lines = [line.upper() for line in lines]

    with open(dest, mode="w") as dest_file:
        dest_file.writelines(lines)
