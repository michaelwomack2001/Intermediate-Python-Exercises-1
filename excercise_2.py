def combine_dicts(dict1, dict2):
    new_dict = {}
    value_int = 0
    for i in dict1:
        for j in dict2:
            if i == j:
                value_int = dict1[i] + dict2[j]
                new_dict.update({i : value_int})
                print('match')
    return new_dict


my_dict_1 = {'a' : 5, 'b' : 12, 'c' : 3, 'd': 9}
my_dict_2 = {'b' : 4, 'c' : 9, 'd' : 10, 'e': 16}
combined_dict = combine_dicts(my_dict_1, my_dict_2)
print(combined_dict)
