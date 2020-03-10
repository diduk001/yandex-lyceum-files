def count_lines(path):
    try:
        with open(path) as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", nargs=1, required=True, help="file to count lines")

    args = parser.parse_args()
    file_path = args.file[0]

    print(count_lines(file_path))
