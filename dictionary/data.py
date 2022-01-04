data={1:'hardik', 2:'helly', 3:'rajsir', 4:'python'}
print(data[2])
print("'using get' :",data.get(1))#op hardik
print("'using get' :",data.get(5))#op none
print("'using get' :",data.get(5,'not found'))#op not found

keys= ['navin', 'kiran', 'harsh']
values=['python','java','js']
DATA=dict(zip(keys,values))
print("1",DATA)
DATA['monica'] ='cs'
print("2",DATA) # monica:cs added in DATA
del DATA['navin']
print("3",DATA) # deleted navin:python
