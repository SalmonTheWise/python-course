__author__ = 'salmon-the-wise'
obj = str(input())
number = int(input())
if obj == 'утюг':
    form = ['утюг', 'утюга', 'утюгов']
elif obj == 'ложка':
    form = ['ложка', 'ложки', 'ложек']
elif obj == 'гармошка':
    form = ['гармошка', 'гармошки', 'гармошек']
elif obj == 'чайник':
    form = ['чайник', 'чайника', 'чайников']


def plural(n, words):
    x = n // 10
    if ((x % 10) != 1) and n % 10 == 1:
        return words[0]
    elif ((x % 10) != 1) and (2 <= n % 10 <= 4):
        return words[1]
    else:
        return words[2]


print(number, plural(number, form))
