def get_unique_list(usr_list):
    unique = []
    is_unique = True
    for i in range(len(usr_list)):
        is_unique = True
        if(i == 0):
            unique.append(usr_list[i])
        for j in unique:
            if i == 0:
                is_unique = False
                break 
            if usr_list[i] == j:
                is_unique = False
                break
        if is_unique == True:
            unique.append(usr_list[i])

    return unique

my_list = [2, 2, 3, 2, 5, 4]
unique_list = get_unique_list(my_list)


print(unique_list)
