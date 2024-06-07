grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # Присваиваем переменной заданный список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # Присваиваем переменной заданное множество

a1 = (sum(grades[0]) / len(grades[0])) # Находим среднюю оценку
a2 = (sum(grades[1]) / len(grades[1]))
a3 = (sum(grades[2]) / len(grades[2]))
a4 = (sum(grades[3]) / len(grades[3]))
a5 = (sum(grades[4]) / len(grades[4]))

students = list(students) # Преобразуем множество в список

b1 = students[0] # Присваиваем переменным преобразованные элементы списка
b2 = students[1]
b3 = students[2]
b4 = students[3]
b5 = students[4]

set = dict ([[b1,a1], [b2,a2], [b3,a3], [b4,a4], [b5,a5]]) #Объединяем списки для составления словаря
print("['Имя' : ср. балл]", set) # Выводим получившийся словарь
