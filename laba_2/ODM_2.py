a = set(input("Введите первое множество:\n").split())

b = set(input("Введите второе множество:\n").split())

c = set(input("Введите универсум:\n").split())
while a.difference(c):
    print("Введите верный универсум")
    c = set(input("Введите универсум:\n").split())


def view(a, b):
    print('Объединение:', set(map(int, a.union(b))))
    print('Пересечение:', set(map(int,a.intersection(b))))
    print('Разность a и b: ', set(map(int,a.difference(b))))
    print('Разность b и a: ', set(map(int,b.difference(a))))
    print('Симметричная разность a и b: ', set(map(int,b.difference(a))).union(set(map(int,a.difference(b)))))
    print('Дополнение множества a: ', set(map(int,c.difference(a))))
    d=[]
    for i in sorted(a):
        for j in sorted(b):
            d.append((int(i),int(j)))
    print('Декартово произведение множеств a и b: ', set(d))



def intersection(a, b):
    g = []

    for i in a:
        if i in b:
            g.append(i)
    print(set(g))


def union(a,b):
    g = []

    for i in a:
        if i not in b:
            g.append(i)
    print(set(g).union(b))
view(a, b)
