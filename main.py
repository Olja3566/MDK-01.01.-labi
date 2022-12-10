def schitat(c):
    c = str(c)
    b = list(c)
    b.reverse()
    a = 0
    for u in b:
        if u == '0':
            a = a + 1
        else:
            print('Подсчёт окончен')
            break
    return print(a)

schitat(5670000)
