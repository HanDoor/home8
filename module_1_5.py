immutable_var = 55,77,9,
print(immutable_var)
#immutable_var[10]=50
#print(immutable_var)#ошибка, tuple не любит изменение элементов
mutable_list = [1,2,3],[4,5,6],[7,8,9]
mutable_list[2][2] = 77
print(mutable_list)
