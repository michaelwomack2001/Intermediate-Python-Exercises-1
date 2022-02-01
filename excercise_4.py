i = 0
sum = 0
while i < 5: 
    is_int = True
    usr_in = input(f'Enter int {i+1}: ')
    try: 
        usr_int = int(usr_in)
    except ValueError:
        print('Invalid input. Please enter a int')
        is_int = False
    if is_int == True:
        sum += usr_int
        i+= 1

print(sum)