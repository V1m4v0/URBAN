def get_matrix(n, m, value):  # Создаем функцию с тремя параметрами
    matrix = []  # Создаем пустой список
    for i in range(n):  # Создаем цикл для количества строк матрицы
        list_ = list()  # Создаем пустой список
        matrix.append(list_)  # Добавляем в список пустой список
        for j in range(m):  # Создаем цикл для количества столбцов матрицы
            list_.append(value)  # Добавляем значение в матрицу

    return matrix  # Возвращаем значение переменной


result1 = get_matrix(2, 2, 10)  # В переменную записываем функцию
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
