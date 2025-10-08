#Чикида Римма 
numbers = input("Enter numbers: ").split() # Вводим список чисел  
list1 = list(map(int,numbers)) # Принимает числа всписок 
# Инициализируем переменные 
n = 0  
max = list1[0] # Предполагаем, что первый элемент - максимальный
# Цикл while для прохода по списку
while n < len(list1) : 
    if list1[n] > max: 
        max = list1[n]
    n += 1
print(f"Maximum number in the list: {max}") # Выводим максимальноие число в списке 
