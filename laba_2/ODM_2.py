i = input("1-Задать множества высказыванием\n2-Задать множества перечислением\n")
a = {}
b = {}

if i=="2":
    a = set(map(int, input("Введите первое множество:\n").split()))
    b = set(map(int, input("Введите второе множество:\n").split()))  

if i=="1":
    a = {x+1 for x in range(1,16)}
    b = {x-1 for x in range(3,14)}

c = {x for x in range(1, 101)}

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
    D = []

    for i in a:
        if i in b:
            D.append(i)
    return set(D)

def difference_b_a(a, b):
    F = []

    for i in b:
        if i not in a:
            F.append(i)
    return set(F)

def difference_a_b(a, b):
    E = []

    for i in a:
        if i not in b:
            E.append(i)
    return set(E)

def sim_diff(a, b):
    return difference_a_b(a,b).union(difference_b_a(a, b))

def dopolnenie(a, b):
    J = []
    
    for i in a:
        if i not in b:
            J.append(i)
    return set(J)

def dek(a, b):
    d=[]
    for i in sorted(a):
        for j in sorted(b):
            d.append((int(i),int(j)))

    return set(d)

def union(a,b):
    C = []

    for i in a:
        if i not in b:
            C.append(i)
    return set(C).union(b)

def laba(a, b):
    print('Объединение A и B: C =', union(a, b))
    print('Пересечение A и B: D =', intersection(a, b))
    print('Разность A и B: E =', difference_a_b(a, b))
    print('Разность B и A: F =', difference_b_a(a, b))
    print('Симметричная разность A и B: G =', sim_diff(a, b))
    print('Дополнение множества A: J =', dopolnenie(c, a))
    print('Дополнение множества B: K =', dopolnenie(c, b))
    print('Декартово произведение множеств A и B: Q =', dek(a, b))
    print('Декартово произведение множеств B и A: P =', dek(b, a))

laba(a, b)
