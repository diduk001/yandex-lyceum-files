import os
import os.path


def os_slash():
    if os.name == 'posix':
        return '/'
    elif os.name == "nt":
        return '\\' * 2


SLASH = os_slash()


def human_read_format(size):
    arr = [(pow(pow(2, 10), 3), "ГБ"), (pow(pow(2, 10), 2), "МБ"), (pow(pow(2, 10), 1), "КБ"), (1,
                                                                                                "Б")]
    if size == 0:
        return "0Б"

    for elem in arr:
        if elem[0] <= size:
            return str(round(size / elem[0])) + elem[1]


def count_files(abs_path):
    res = 0
    for file in os.listdir(abs_path):
        son_file_path = f'{abs_path}{SLASH}{file}'
        if os.path.isfile(son_file_path):
            res += 1
        elif os.path.isdir(son_file_path):
            res += count_files(son_file_path)
    return res


while True:
    root_dir = input("Введите, пожалуйста, путь к директории, куда надо поместить копию:\t")
    if os.path.exists(root_dir) and os.path.isdir(root_dir):
        print('OK!')
        break
    else:
        print("Вы где-то ошиблись. Попробуйте ещё раз")

directories_sorted = os.listdir(root_dir)
directories_sorted = list(filter(lambda file: os.path.isdir(root_dir + SLASH + file),
                                 directories_sorted))
directories_sorted.sort(key=lambda file: count_files(root_dir + SLASH + file), reverse=True)
directories_sorted = directories_sorted[:10]
directories_sorted.sort(key=lambda file: os.path.getsize(root_dir + SLASH + file), reverse=True)
directories_sorted = list(map(lambda file: (file, human_read_format(os.path.getsize(root_dir + SLASH
                                                                                    + file)),
                                            ), directories_sorted))
for file, size in directories_sorted:
    print(f'{file}{(max(1, 75 - (len(file) + len(size)))) * " "}{size}')
