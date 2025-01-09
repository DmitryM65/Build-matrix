def get_matrix(n, m, value):
	matrix = []
	for i in range(n):
		matrix.append([])           # формируем строки
		for j in range(m):
			matrix[i].append(value) # заполняем i-ю строку значениями
	return matrix                   # возвращаем матрицу

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(0, 0, 4)       # здесь получаем пустой список
result5 = get_matrix(-2, -7, 11)    # и здесь тоже пустой

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)