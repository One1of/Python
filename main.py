# For
num_list = [1,2,3,4,5]
for num in num_list: # for переменная в цикле в num_list
    print(num) # выведет все цифры по порядку

for num in num_list:
    print('Hello') # выведет Hello столько раз сколько элементов этом списке

for num in num_list:
    print(str(num_list) + 'Hello') # выводится цифра и заданное слово

for num in num_list:
    if num % 2 == 1: # вот так пишутся условия для цикла for
        print(num)
    else:
        print('Hi') # а если цифра чётная то выводится эта строка

list_num_sum = 0
for num in num_list:
    list_num_sum = list_num_sum + num
    print(list_num_sum) # а тут выводятся все результаты после их получения
# print(list_num_sum) если написать в начале строки то это будет обозначать выход из цикла и вывидется последний результат

say = 'Looking my ass'
for message in say:
    print(message) # выводится каждая буква из строки

for message in say:
    if say == 'ass': # выводится ass)) так же можно написать != ass
        print(message)

tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)
for let1, let2 in tuple_list:
#    print(let1, let2) let1 вывод 1 значения let2 вывод 2 (тут вывод одновременоо 1,2 1,2 1,)
    print(let1)
    print(let2)

dictionary = {'key1': 'num1', 'key2': 'num2', 'key3': 'num3'}
for item in dictionary.items(): # вывожим ключ значение(.key ключи .values значения)
    print(item)

for x in range(3): # вывод последовательности чисел до 3 (используется когда переменная не важна а важна итерация)
    print(x)

# While
y = 1
while y <= 5:
    print(y)
    y += 1 # y = y + 1

x = 0
while x < 10:
    print('x < 10, x = ' + str(x))
    x += 1
else:
    print('x >= 10, x = ' + str(x))

for x in range(10): # тоже самое что и цикл сверху
    print('x < 10, x = ' + str(x))
    x += 1
else:
    print('x >= 10, x = ' + str(x))

# Break, continue, pass
list1 = [1, 2, 3]
for x in list1:
    pass # является заглушкой которую можно использовать для временного отключения ненужного цикла(метода, функции)

for x in list1:
    if x == 3:
        break # выход из цикла
    print(x)

for x in list1:
    if x == 2:
        continue # переход в начало цикла
    print(x)