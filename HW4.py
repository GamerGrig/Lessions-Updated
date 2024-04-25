immutable_var = 1, 2, True, 'String', 1.2
print(immutable_var)
#immutable_var [2] = 2
print(immutable_var) # Кортеж не изменяемый

mutable_list = [1,False,'string',1.2]
print(mutable_list)
mutable_list[0] = 3
mutable_list[1] = 'string'
mutable_list[2] = True
mutable_list[3] = 2.1
print(mutable_list)