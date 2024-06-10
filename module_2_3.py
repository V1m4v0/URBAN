x = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while x < len(my_list):
    if my_list[x] > 0:
        print(my_list[x])
        x = x + 1
        continue
    elif my_list[x] == 0:
        x = x + 1
    else:
        break
