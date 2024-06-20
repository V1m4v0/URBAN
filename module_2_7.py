def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [123, False, 'string']
value_dict = {'a': 3, 'b': "world", 'c': False}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = [True, 12.5]
print_params(*value_list_2, 42)
