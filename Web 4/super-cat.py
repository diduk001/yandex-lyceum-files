import sys

args = sys.argv
del args[0]

try:
    sort_flag = False
    if "--sort" in args:
        sort_flag = True
        args.remove("--sort")

    num_flag = False
    if "--num" in args:
        num_flag = True
        args.remove("--num")

    count_flag = False
    if "--count" in args:
        count_flag = True
        args.remove("--count")

    with open(args[-1]) as f:
        lines = f.readlines()

        if sort_flag:
            lines.sort()

        if num_flag:
            lines = [str(lines.index(lines[i])) + ' ' + lines[i] for i in range(len(lines))]

        if count_flag:
            lines.append("rows count: " + str(len(lines)))

        for line in lines:
            print(line)

except Exception:
    print("ERROR")
