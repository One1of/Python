# Lists(списки(массивы))
some_list = [23, "world", 965.45]
print(some_list)
print(len(some_list)) # так же можно функции len выводить кол-во значений в массиве
another_list = some_list[:2] # как и со строками вырезали нужное кол-во элементов
print(another_list)
some_list[0] = 23500
print(some_list)
new_list = some_list + another_list # со списками работает конкатенация
print(new_list)

# add items(добавление элементов)
new_list.append("item") # этот метод добавляет новый элемент в конец списка
print(new_list)
new_list.insert(3, "middle")
print(new_list)

# removing items(удаление элементов)
new_list.pop() # по умолчанию удаляет первый элемент с конца(-1) но это можно изменить
new_list.pop(0)
print(new_list)

deleted_item = new_list.pop(2) # удалили элемент и вернули его в эту переменную
print(deleted_item)
# deleted_item = new_list.remove()  удаляет первое названное значение
# print(deleted_item) тут находится значение None потому что remove ничего не возвращает

number_list = [3, 2, 1]
letter_list = ["c", "b", "a"]
number_list.sort() # сортирует по возрастанию и так же не возвращает значения reverse(сортирует в обратном порядке)
letter_list.sort() # по убыванию
print(new_list)
print(letter_list)

number_list.append(letter_list) # добавляет список внутрь другого списка
print(number_list)

# dictionaries(словари - тобиж объекты)
car = {
    'model': 'opel',
    'year': 2003,
    'price': 500
}
print(car['model'])
car['wheels'] = 4 # добавили в словарь ключ wheels со значением 4
del car['wheels'] # удалили ключ значение(если не указать их то удалится сам словарь)
print(car)
car.clear() # удалит все ключи и элементы находящиеся в нём
man = {
    'name': "Same",
    'age': 19,
    'hobbies': ['programming', 'photo', 'music'],
    'children': {
         'girl': 'Mart',
    }
}
print(man['hobbies'][0]) # вызвали значение находящееся в листе hobbies(по индексу) который внутри объекта

children = man['children']
# print(children['girl']
print(man['children']['girl'])
man['children']['son'] = 'Jon' # добавил во вложенный объект(словарь) ключ значение
print(man)

print(man.keys()) # выводит все ключи словаря
print(man.values()) # выводит все значения
print(man.items()) # выводит все элементы(получаем структуру в скобках которая называется tuple(кортеж))

# у Python есть множественное присваивание:
x = y = z = 7
print(x, y, z)
x, y, z = 4, 8, 12
print(x, y, z)
# это может использоваться для распаковки tuple

# Tuple(кортеж) является не изменяемым(так что, если захочется изменить tuple вместо этого придётся создать новый)
tuple1 = 1, 2, 3 # можно не указывать скобки так как они нужны чтобы было понятно tuple это или нет
tuple2 = ('a', 'b', 'c')
tuple3 = (12, 'middle', 43.5)
tuple4 = tuple1 + tuple2
print(tuple4)

one, two, tree = tuple3
print(one,two,tree)
t = (1,2,3,4,5)
print(t.count(3)) # покажет сколько раз встречается 3(тоже самое работает и со строками)

print(t.index(3)) # покажет под каким индексом находится это значение(либо индекс самого первого такого же значения)

# Sets(множества(не упорядоченная коллекция уникальных элементов))
colors = {'red', 'green', 'blue'} # такие же скобки как и у словаря
print(colors)
print(type(colors))

colors2 = set() # создали пустое множество
print(type(colors2))

number_list = [54, 25, 62, 62]
text_tuple = ('hohoho', 'hahaha', 'hehehe')
set_from_list = set(number_list) # создали множество и хоть в number_list есть 2 одинаковых значения при создании sets будет только одно
set_from_tuple = set(text_tuple)
print(set_from_list, set_from_tuple)

set_from_list.add(55)
set_from_tuple.add('hihihi')
print(set_from_list,set_from_tuple)

set_from_list.pop() # удалили рандомный элемент и возвращает его
set_from_tuple.remove('hihihi') # не возвращает(есть метод discard который делает тоже самое но при отсутствии удаляемого элемента не будет ошибки)
print(set_from_list,set_from_tuple) # и конечно же можно можно использовать clear для очистки всего множества