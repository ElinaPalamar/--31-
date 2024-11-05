def split_list_by_value(lst, split_value):
    less_than_value = [x for x in lst if x < split_value]
    greater_equal_value = [x for x in lst if x >= split_value]
    return less_than_value, greater_equal_value

user_input = input("Введіть список чисел, розділених пробілом: ")
lst = list(map(int, user_input.split()))

split_value = int(input("Введіть значення для розбиття списку: "))

less_than, greater_equal = split_list_by_value(lst, split_value)

print("Список з елементами, меншими за", split_value, ":", less_than)
print("Список з елементами, більшими або рівними", split_value, ":", greater_equal)

