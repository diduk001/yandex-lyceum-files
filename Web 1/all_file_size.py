import os


def human_read_format(size):
    arr = [(pow(pow(2, 10), 3), "ГБ"), (pow(pow(2, 10), 2), "МБ"), (pow(pow(2, 10), 1), "КБ"), (1,
                                                                                                "Б")]
    if size == 0:
        return "0Б"

    for elem in arr:
        if elem[0] <= size:
            return str(round(size / elem[0])) + elem[1]


def get_files_sizes():
    res = ""
    for path in os.listdir(os.getcwd()):
        if os.path.isfile(path):
            res += f"{path} {human_read_format(os.path.getsize(path))}\n"
    return res.strip()

