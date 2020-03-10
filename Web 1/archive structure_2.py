import zipfile


def human_read_format(size):
    arr = [(pow(pow(2, 10), 3), "ГБ"), (pow(pow(2, 10), 2), "МБ"), (pow(pow(2, 10), 1), "КБ"), (1,
                                                                                                "Б")]
    if size == 0:
        return "0Б"

    for elem in arr:
        if elem[0] <= size:
            return str(round(size / elem[0])) + elem[1]


with zipfile.ZipFile('input.zip') as archive:
    for file in archive.infolist():
        fname = file.filename
        if fname[-1] == '/':
            print('  ' * (fname.count('/') - 1) + fname.split('/')[-2])
        else:
            print('  ' * fname.count('/') + fname.split('/')[-1],
                  str(human_read_format(file.file_size)))
