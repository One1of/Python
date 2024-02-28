# Booleans(булевы значения) многое не записано так как я и так это знаю
print(ord('b')) # позволяет узнать ASCII код строчного символа(буквы)
# можно сравнить их код ASCII
print(ord('a'))
print(ord('c'))
print('a' < 'c')
# age = input('Input your age')
#print(age) тут можно написать если твой возраст больше либо меньше другого то будет выводится что-то но мне в падлу

# Logical operators
x = 3
y = 7
print(x > 5 and y > 5)
print(x > 5 or y > 5)
print(not y < 7)

name = 'Soso'
age = 12
brawlstars = False
if age > 10 and brawlstars == False:
    print('Hi {} you pider'.format(name))

# Conditional operators
str1 = 'Hello'
if str1 == 'Hello':
    print('Hi')
elif not str1 == 'Hello':
    print('?')
else:
    print('Say Hello')

