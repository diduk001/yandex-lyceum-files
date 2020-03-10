import os.path
import shutil
import time


def os_slash():
    if os.name == 'posix':
        return '/'
    elif os.name == "nt":
        return '\\' * 2


SLASH = os_slash()


def make_reserve_arc(source, dest, name_=None):
    source_path = str(os.path.abspath(source))
    dest_path = str(os.path.abspath(dest))
    if name_ is None:
        cur_time_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        name = f'{source_path.split(SLASH)[-1]} {cur_time_string} Copy'
    else:
        name = name_
    shutil.make_archive(name, 'zip', root_dir=source_path)
    shutil.move(name + '.zip', dest_path)


while True:
    source = input("Введите, пожалуйста, путь к копируемой директории:\t")
    if os.path.exists(source) and os.path.isdir(source):
        print('OK!')
        break
    else:
        print("Вы где-то ошиблись. Попробуйте ещё раз")

while True:
    dest = input("Введите, пожалуйста, путь к директории, куда надо поместить копию:\t")
    if os.path.exists(dest) and os.path.isdir(dest):
        print('OK!')
        break
    else:
        print("Вы где-то ошиблись. Попробуйте ещё раз")

name = input("Нажмите Enter чтобы оставить имя копии по умолчанию или введите имя копии\t")
print("OK!")
if name == '':
    name = None

print("Начало копирования")
make_reserve_arc(source, dest, name)
print("Копирование завершено")
