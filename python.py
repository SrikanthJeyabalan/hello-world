print('Hello World \t hello')
print(len('Hello World'))
a = "Hello, World!"
print(len(a))
txt = "The best things in life are free!"
print("free" in txt)
b = "Hello, World!"
print(b[2:5])
print(b[::-1])
print(b[:-1])
print(a,b)
print(a + "concatenate me")
letter = 'd'
print(letter * 10)
print(a.upper())
print(a.split('l'))
s = 'STRING'
print ('Place another string with a mod and s: %s' %(s))
print ('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))
my_list=[1,2,3]
print (my_list)
print (len(my_list))
print (my_list[1:])
print (my_list[:3])
print(my_list + ["concatenate me"])
my_list = my_list + ["concatenate me"]
print(my_list)
my_list.append(5)
print(my_list)
X = my_list.pop(0)
print (X)
print (my_list)
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
matrix = [l_1, l_2, l_3]
print (l_1, l_2, l_3)
print (matrix [1][0])
first_col = [row[0] for row in matrix]
print (first_col)
d = {}
print (d)
d ['name'] = "John"
d ['age']  = 28
d ['country'] = 'India'
print (d.get ('name'))
print (100>2)
a = 50
b = 10
if a==b:
  print("Yes")
else:
  print("No")