# Чикида Римма 
numbers = input("Enter numbers: ").split() # Вводим числа через пробел 
list1 = list(map(int,numbers)) # Принимает числа в список 
list2 = [x**2 for x in list1] #  Возводит числа из первого списка в квадрат 
print(f"List of squares: {list2}") # Выводит числа в квадрате 
