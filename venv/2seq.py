user_input=input("Введите числа через запятую: ")
numbers=user_input.split(",")
unique_numbers = list(set(numbers))

res_str=''
for i in range(len(unique_numbers)):
    if res_str!='':
        res_str+=', '
    res_str+=unique_numbers[i]

print(res_str)