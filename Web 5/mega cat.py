import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file", nargs=1, type=str)
parser.add_argument("--count", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")

try:
    args = parser.parse_args()

    file = args.file[0]
    count_flag = args.count
    num_flag = args.num
    sort_flag = args.sort

    with open(file) as f:
        lines = f.readlines()

        if sort_flag:
            lines.sort()

        if num_flag:
            lines = [str(lines.index(lines[i])) + ' ' + lines[i] for i in range(len(lines))]

        if count_flag:
            lines.append("rows count: " + str(len(lines)))

        for line in lines:
            print(line.rstrip())

except Exception as e:
    print("ERROR")
