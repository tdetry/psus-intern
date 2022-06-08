# lambda functions
# below function prints power of a number
print((lambda x, y: int(x)**int(y))(input("enter a number "),input("enter its power ")))

#Comprehension

temp = [[1 * j for j in range(1,i)] for i in range(1,100)]
print(*temp,sep='\n')