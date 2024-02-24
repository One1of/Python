str = "Hello"
str1 = len(str) # считает длину строки
print(str1)
print(len(str))

# indexing
print(str[0])
print(str[-1]) # узнаём какой символ находится в конце строки

# slicing
print(str[0:3]) # выбрали область которая будет вырезана
print(str[-3:-1])
print(str[:2]) # вырезали сначала до 2 символа
print(str[::3]) # вырезали символы с интервалом 3
print(str[::-1]) # вывод перевёрнутой строки

# свойства и методы строк

# immutable (неизменное)
str = "Word"
print(str[3])
# str[3] = "k" строки являются неизменными
# print(str)
str1 = str[:3]

# concatenable
str2 = str1 + "k" # вот как можно заменять строки
print(str2)

# multiplication (умножение)    строки в этом яп являются объектами по этому и есть методы работы со строками
cookies = "cookie "
print(cookies * 3) # выведет строку с 3 словами cookie

print(cookies.upper()) # этот метод делает все буквы заглавными
print(cookies.lower())
print(cookies) # так как строки неизменные то методы никак их не изменяют и создают новые строки
low_string = "Low string"
print(low_string.split()) # выводит строку в виде листа(массива) делит по пробелам(по умолчанию)
print(low_string.split("w")) # w разделитель

# formation
name = "Jonn"
age = 18
# print("name " + str(age) + "years old")   str(age) преобразует int тип в строку, есть ещё один способ     1 способ почему-то не работает как нужно
name_and_age = "My name is {0}. I\'m {1} years old".format(name,age)
print(name_and_age)

week_days = 'There are 7 days in a week: {5},{0},{3},{1},{2},{4},{Sat}.'\
.format('Monday', 'Wednesday', 'Thursday', 'Tuesday', 'Friday', 'Sunday', Sat ='Saturday')
print(week_days)

float_result = 450 / 8.4
print(float_result)
print(('The result: {0:1.2f}'.format(float_result))) # {}- это плейсхолдер
# отформатировали полученый результат где 1 это минимальное кол-во всех символов в числе а 2f(f-float) максимальное кол-во символов полсе запятой
# если 1-е число указано больше чем то которое мы получили то перед этим числом получается пробел в длинне равной отсутствубщим числам

name = "Jonn"
age = 18
name_and_age = "My name is {0}. I\'m {1} years old".format(name,age)
print(name_and_age)
name_and_age = f"My name is {name}. I\'m {age} years old" # вместо того чтобы указывать .format мы перед строкой написали f(обозначает fstring)
print(name_and_age)
print("My name is %s. I\'m %d years old" %(name,age)) # s-строка d-число (этот метод нет смысла использовать так как в будущем он будет поддерживаться)