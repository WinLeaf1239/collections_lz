import statistics #Вводим библиотеку 

N = int(input('Введите до какого элемента будет ряд фибоначи: ')) 
a = 0 #Для числа фибоначи
b = 1 #Для числа фибоначи
elem = 0 #Для количества чисел больших медианного значения
list = [] #Задаем пустой список
for i in range (0 , N) : #Цикл от 0 до N
    list.append(a)
    a, b = b, a + b
print("Наш ряд фибоначи:" , list)
for i in range(0,len(list),2) :
    list[i] = list[i] *2
for i in range(1,len(list),2) :
    list[i] = list[i] **2
print("Наш измененный ряд фибоначи:" , list)
print("Минимальный элемент нашего измененного ряда:" , min(list))
print("Максимальный элемент нашего измененного ряда:" , max(list))
print("Длина нашего измененного ряда:" , len(list))

med = statistics.median(list)
print("Медианное значание нашего ряда:" , med)
for i in range(0,len(list)) :
    if list[i] > med :
        elem += 1
print("Кол-во элементов больше медианного значения:" , elem)