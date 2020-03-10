import zipfile
import json
import io

ans = 0
with zipfile.ZipFile("input.zip") as archive:
    for file_path in archive.infolist():
        file_name = file_path.filename
        file = archive.open(file_name)
        data = ''
        for line in io.TextIOWrapper(file, encoding='utf-8'):
            data += line.strip()
        if data == '':
            continue
        resp = json.loads(data)
        if 'city' in resp.keys() and resp['city'] == "Москва":
            ans += 1
print(ans)
