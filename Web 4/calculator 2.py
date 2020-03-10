import sys


class EmptySequenceError(ValueError):
    pass


try:
    a = sys.argv
    del a[0]

    if not a:
        raise EmptySequenceError

    ans = 0
    for i in range(len(a)):
        temp = int(a[i])
        if i % 2 == 0:
            ans += temp
        else:
            ans -= temp

    print(ans)

except EmptySequenceError:
    print("NO PARAMS")
except Exception as e:
    name = e.__repr__()
    print(name[:name.find("(")])