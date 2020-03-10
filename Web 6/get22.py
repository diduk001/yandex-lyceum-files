import requests

address = input()
port = input()
a = input()
b = input()

params = {
    "a": a,
    "b": b
}

r = requests.get(address + ':' + port, params=params)
json_response = r.json()

check = json_response['check']
result = list(json_response['result'])
result = list(map(int, result))
result.sort()

print(*result)
print(check)
