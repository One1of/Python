# List comprehension(понимание списков)
greeting = 'World!'
letter_list = []
for letter in greeting:
    letter_list.append(letter)
print(letter_list)

letter_list1 = [letter for letter in greeting]
print(letter_list1)
number_list = [number for number in '123456789'] # тут вывод будет в виде строки
print(number_list)
number_list1 = [number for number in range(0, 10)]
print(number_list1)
number_list2 = [number ** 2 for number in range(0, 10)] # как я понимаю сначала создаётся переменная(с которой уже можно как-то взаимодействовать)
print(number_list2) # которая потом исп в цикле и мы в неё засовываем сгенерированные числа

number_list3 = [134, 5, -431, 700]
new_list = [num for num in number_list3 if num > 0] # помещаем num в наш список из последовательности пред списка если этот элемент положительный
print(new_list)
new_list1 = ['+' if num > 0 else '-' for num in number_list3] # с else пишется вначале
print(new_list1)

# Dictionary comprehension
num_dict = {'key': 1, 'key2': 2, 'key3': 3}
new_dict = {key: value ** 4 for key, value in num_dict.items()}
print(new_dict)

number_list4 = [134, 5, -431, 700, 0]
num_dict1 = {number: number ** 2 for number in number_list4} # ключом является пред знач
print(num_dict1)
num_dict1 = {number: '+' if number > 0 else '-' if number < 0 else 'zero' for number in number_list4}
print(num_dict1)

# Sets comprehension
number_list = [134, 5, -431, 700, 0]
num_set = {number ** 2 for number in number_list4} # множества это не упорядоченная последовательность
print(num_set)