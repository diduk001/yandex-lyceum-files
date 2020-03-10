import zipfile

with zipfile.ZipFile('input.zip') as archive:
    for file in archive.infolist():
        fname = file.filename
        if fname[-1] == '/':
            print('  ' * (fname.count('/') - 1) + fname.split('/')[-2])
        else:
            print('  ' * fname.count('/') + fname.split('/')[-1])