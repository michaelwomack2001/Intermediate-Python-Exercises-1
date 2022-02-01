def make_dict(string_in):
    new_dict ={}
    for i in string_in:
        count = 0
        for j in range(len(string_in)):
            if i == ' ': 
                break
            if i.isupper() == True:
                break
            if i not in new_dict:
                new_dict.update({i : count})
            if i == string_in[j]:
                count += 1
                new_dict.update({i : count})
    return new_dict

usr_string  = str(input('Enter a String: '))
string_dict = make_dict(usr_string)
print(string_dict)