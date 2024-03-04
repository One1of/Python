for x in range(5,11,2): # (начало,до какого момента, шаг)
    print(x)
print(range(10)) # в виде range
print(list(range(10))) # отображается в виде списка

str1 = 'abcdefg'
for item in enumerate(str1): # произведёт нумерацию символов (1, 'b')
    print(item)

for index, letter in enumerate(str1): # произведёт нумерацию символов (1, 'b')
    print(letter + ' is at index ' + str(index))

print('a' in 'abc') # проверяет если такое элемент как a в abc и возвращает результат True
print('b' in 'cde')

list1 = ['a','b','c',1,'e']
print('c' in list1)
print(1 in list1)

dict1 = {1: 'a', 2:'b', 3:'c'}
print(1 in dict1)
print(1 in dict1.keys())
print('b' in dict1.values())

print(min(100,1,50))
print(max(100,1,50))

from random import shuffle # подключил библиотеку и импортировал команду
list2 = [64,0,15,5]
shuffle(list2) # перетасовывает значения
print(list2)

from random import randint # рандомное целое число
print(randint(1,100))