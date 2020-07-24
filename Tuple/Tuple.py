import ast,sys
input_str = input()
input_tuple = ast.literal_eval(input_str)

a=list(input_tuple)
a.append('Python')
tuple_2=tuple(a)

# Make sure to name the final tuple 'tuple_2'
print(tuple_2)










