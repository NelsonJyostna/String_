

'''
st12 = "hello, my name is Peter, I am 26 years old"
k=st12.split(',')
print(k)


st13 = "hello# my name is Nelson, I am 33 years old"
d=st13.split('#')
print(d)

g = '       '
print(g.isspace())'''
###################################################################3################
'''
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
'''
###########################################################################3##########
'''
s = '1,2,3,4'
k = s.split(',')
print(k)
sum = 0

for i in k:
    print(i)
    sum = sum+int(i)
print(sum)
'''
####################################################################################################################################
'''

d=["1,2,3,4"]
sum=0

for i in d:
    print(i)
    k=i.split(',')
    print(k)
    for j in k:
       sum =sum+int(j)
print(sum)'''

############################################################33########################################################
'''
name=('Hello', 'How', 'Are', 'You')
str1='_'.join(name)

print(str1)

str2=' '.join(name)
print(str2)'''
############################################################33#######################################################3

'''
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)'''
####################################################################################################################################
'''
# Interview Question
a=['1,4,5,6', '1,2,4,6']   # find out the common elements

print(a[0])
print(a[1])

def string1(str2):
    k=set(str2[0].split(','));print(k)
    m=set(str2[1].split(','));print(m)
    h=k.intersection(m)
    print(h)
    str2=list(h)
    return str2

# print(string1(['1,2,3', '1,2']))
print(string1(['1,4,5,6', '1,2,4,6'] ))
'''
####################################################################################################################################
'''
count = 0
n = int(input('Enter a no :' ))
for i in range(1, n+1):
    if n%i==0:
        count = count+1
if count==2:
    print('Prime')
else:
    print('Not a prime')
'''
####################################################################################################################################
'''
a =3414
sum=0
while a>0:
    sum = sum + (a%10)
    a= a//10
print(sum)
'''
####################################################################################################################################
'''
l = [1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(l):
    print(l[i]**2, end=" ")
    i=i+1

k =[i**2 for i in l]
print(k)

d=list(map(lambda n:n**2, l))
print(d)

h= set(map(lambda n:n**2, l))
print(h)'''

####################################################################################################################################






