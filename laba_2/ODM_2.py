i = input("1-Задать множества высказыванием\n2-Задать множества перечислением\n")
a = {}
b = {}

# Если пользователь выбирает вариант задания множеств – высказыванием
if i == "1":
	a = {x + 1 for x in range(1, 16)}
	b = {x - 1 for x in range(3, 14)}
	# Выводим на экран элементы множества А.
	print(a)
	# Выводим на экран элементы множества В.
	print(b)

if i == "2":
	# Вводим элементы множества А;
	a = set(map(int, input("Введите первое множество:\n").split()))
	# Вводим элементы множества B
	b = set(map(int, input("Введите второе множество:\n").split()))

# Универсальное множество  состоит из натуральных чисел от 1 до 100.
U = {x for x in range(1, 101)}


def view(a, b):
	print('Объединение:', set(map(int, a.union(b))))
	print('Пересечение:', set(map(int, a.intersection(b))))
	print('Разность a и b: ', set(map(int, a.difference(b))))
	print('Разность b и a: ', set(map(int, b.difference(a))))
	print('Симметричная разность a и b: ', set(map(int, b.difference(a))).union(set(map(int, a.difference(b)))))
	print('Дополнение множества a: ', set(map(int, c.difference(a))))
	d = []
	for i in sorted(a):
		for j in sorted(b):
			d.append((int(i), int(j)))
	
	print('Декартово произведение множеств a и b: ', set(d))


def intersection(a, b):
	# Создается пустое множество D.
	D = []
	
	for i in a:
		# Если выбранный элемент множества A равен выбранному элементу множества B,
		if i in b:
			# Записываем выбранный элемент множества A во множество D
			D.append(i)
	# Выводим на экран результат операции пересечения множеств А и (множество D).
	return set(D)


def difference_b_a():
	# Создается пустое множество F
	F = list(b)
	# Выбираем первый элемент множества B
	for i in b:
		# Если выбранный элемент множества B равен выбранному элементу множества A
		if i in a:
			## Удаляем выбранный элемент множества A из множества E
			F.remove(i)
	# Выводим на экран результат операции математической разности множеств B и A (множество F).
	return set(F)


def difference_a_b():
	# Создается пустое множество E
	E = list(a)
	# Выбираем первый элемент множества A
	for i in a:
		# Если выбранный элемент множества A равен выбранному элементу множества B
		if i in b:
			# Удаляем выбранный элемент множества A из множества E
			E.remove(i)
	# Выводим на экран результат операции математической разности множеств А и В (множество E).
	return set(E)


def sim_diff(a, b):
	# Копируем каждый элемент множества E в множество G.
	G = list(difference_a_b())
	F = list(difference_b_a())
	
	for i in F:
		# Если выбранный элемент множества F не равен выбранному элементу множества G
		if i not in G:
			# Записываем выбранный элемент множества F во множество G
			G.append(i)
	
	# Выводим на экран результат операции симметрической разности множеств E и F (множество G).
	return set(G)


def dopolnenie_a():
	# Создаём пустое множество J.
	J = list(U)
	
	for i in a:
		# Если выбранный элемент универсального множества U равен выбранному
		# элементу множества A
		if i in J:
			# Удаляем выбранный элемент универсального множества U из множества J
			J.remove(i)
	# Выводим на экран результат операции дополнения множества А (множество J)
	return set(J)


def dopolnenie_b():
	# Создаём пустое множество J.
	K = list(U)
	
	for i in b:
		# Если выбранный элемент универсального множества U равен выбранному
		# элементу множества B
		if i in K:
			# Удаляем выбранный элемент универсального множества U из множества J
			K.remove(i)
	# Выводим на экран результат операции дополнения множества B (множество J)
	return set(K)


def dek(a, b):
	# Создаём пустое множество Q.
	Q = []
	# Если выбранный элемент множества А не является последним, то:
	# Выбираем следующий элемент множества А
	for i in a:
		# Если выбранный элемент множества В не является последним, то:
		#  Выбираем следующий элемент множества В
		for j in b:
			# Записываем кортеж, состоящий из выбранного элемента множества А и выбранного элемен  множества В, во множеств Q
			Q.append((i, j))
	# Выводим на экран результат декартового произведения множеств А и В (множество Q)
	return set(Q)


def union(a, b):
	# Во множество C копируется каждый элемент множества А
	C = list(a)
	
	for i in b:
		# Если выбранный элемент множества В не равен выбранному элементу множества А
		if i not in C:
			# Записываем выбранный элемент множества B во множество С
			C.append(i)
	# Выводим на экран результат операции объединения множеств А и В (множество C)
	return set(C)



print('Объединение A и B: C =', union(a, b))
print('Пересечение A и B: D =', intersection(a, b))
print('Разность A и B: E =', difference_a_b())
print('Разность B и A: F =', difference_b_a())
print('Симметричная разность A и B: G =', sim_diff(a, b))
print('Дополнение множества A: J =', dopolnenie_a())
print('Дополнение множества B: K =', dopolnenie_b())
print('Декартово произведение множеств A и B: Q =', dek(a, b))
print('Декартово произведение множеств B и A: P =', dek(b, a))

