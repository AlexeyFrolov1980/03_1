user_input=input("Введите числа через запятую (список 1): ")
list_1=user_input.split(",")
user_input=input("Введите числа через запятую (список 2): ")
list_2=user_input.split(",")

res=(set(list_1) - set(list_2))
res_list=list(res)
print(res_list)