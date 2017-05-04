def init():
	A=[]
	B=[]
	count1 = int(input("Введите мощность графика A\n"))
	for i in range(count1):
		A.append(tuple(map(int, input("Введите через пробел " + str(i + 1) + "-ую пару множества A\n").split())))

	count2 = int(input("Введите мощность графика B\n"))
	for i in range(count2):
		B.append(tuple(map(int, input("Введите через пробел " + str(i + 1) + "-ую пару множества B\n").split())))

	return set(A), set(B)


def inversion(se):
	se = {(a,b) for b,a in se}
	return se


def composition(A, B):
	J=[]
	for i in A:
		for j in B:
			if i[1] == j[0]:
				J.append((i[0],j[1]))
	return set(J)


def laba():
	A, B = init()
	print("Объединение графиков A и B:", A.union(B))
	print("Пересечение графиков A и B:", A.intersection(B))
	print("Разность графиков A и B:", A.difference(B))
	print("Разность графиков B и A:", B.difference(A))
	print("Симметрическая разность графиков A и B:", A.difference(B).union(B.difference(A)))
	print("Инверсия графика A:", inversion(A))
	print("Инверсия графика B:", inversion(B))
	print("Композиция графиков A и B:", composition(A, B))
	print("Композиция графиков B и A:", composition(B, A))

laba()