def add_digits_to_set(char_set):
    digit_set = {str(i) for i in range(10)}

    result_set = char_set.union(digit_set)
    return result_set

char_set = {'c', 'd'}

result = add_digits_to_set(char_set)

print("Результуюча множина:", result)