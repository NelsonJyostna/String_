##################3#################################################################################
'''
l2='     nelsonandshivaji     '
print(l2.strip())

l3="   nelson   "
print(l3)
'''
###################################################################################################

'''
l4='nelson'
# print(l4.split())
# print(l4)
for i in l4:
    print(l4.split(i))
'''

#######################################################################################################

'''
l4='nelson'
print(l4.upper())
print(l4.isupper())
print(l4.islower())
print(l4.capitalize())
print(l4.find('e'))
print(l4.index('s'))
print(l4.startswith('o'))

'''
##############################################################################################################

'''
string="Nelson"
print(type(string))
print(id(string))

d=string.replace("s", "Mom")
print(d)
print(type(d))
print(id(string))
'''
######################################################################################################################
'''


# print("44".isdigit())
# print("a".isdigit())
# print("44".isalpha())
# print("a".isalpha())
# print("44a".isalnum())
# print("a".isalnum())
# print("44".isalnum())

#print(True.isalnum())#AttributeError: 'bool' object has no attribute 'isalnum'

# print("a".isupper())
# print("A".isupper())
# print("a".islower())
# print("A".islower())
# print("Aa".istitle())
# print("AA".istitle())
# print("Aa".istitle())

text='asdadsadfdf'
# print(text.isspace())
text='  A '
# print(text.isspace())   # is the string made of spaces only ?
# text='asdadsadfdf'
# print(text.count('a'))

a='this is python'
# print(a.title())
# print(a.capitalize())
# print(a.upper())
# print(a.title())

a='this is PYTHON'
# print(a.lower())
# print(a.swapcase())

a='        this is NELSON           '
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
'''
################################################################################################################3

'''
a='this is this PYTHON'
# print(a.replace('is','the', 1))
# print(a.translate(str.maketrans(' ',' ', 'aeiou')))

# print('35',a.partition('is'))#'th', 'is','is this python'
# print(a.rpartition('is'))
# print('37','this is this PYTHON'.partition(' is '))
#
# print(a.endswith('hon'))
# print(a.endswith('HON'))
# print(a.startswith('thi'))
# print(a.startswith('THI'))

# print(a.find('is'))#2     #tricky
# print(a.rfind('PYTHON'))   #tricky
a='I am is PYTHON'
# print(a.index('is'))#like find but raises error when substring is not found

'''
############################33########################################################################################
'''
#JOIN
#A useful function is the split() methods that splits a string according to a character. The inverse function exist and is called join().


message = ' '.join(['this' ,'is', 'a', 'useful', 'method'])
# print(message)
#O/P:-'this is a useful method'

# print(message.split(' '))
# print(message.split(' ',2))   # starting ka 2 split kiya sirf
#O/P:-['this', 'is', 'a', 'useful', 'method']

message = ' '.join(['this' ,'is', 'a', 'useful', 'method'])
# print(message.rsplit(' ', 2))   # right side ka 2 chodke

# print('this is an example\n of\n dummy sentences'.splitlines())
#o/p:-['this is an example', ' of', 'dummy sentences']

# print("this is an exemple".split(" an "))    #tricky
# print("this is an exemple".split(" is "))    #tricky

'''
##############################################################################################################

'''
email_passed='email'
email_req="gmail.com"  and "yahoo.com"

if not email_req in email_passed:
       print("mbmbm")
'''
#######################################################################################################
'''
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)


myList=['Nelson', 'shivaji', 'Avinash', 'Abhijeet']
mySeparator = "TEST"
y = mySeparator.join(myList)
print(y)
'''
#######################################################################################################################

'''
from collections import Counter
test_list = ["geeksforgeeks is best for geeks"]
print("The original list : " + str(test_list))

chr_list = ['e', 'b', 'g']
res = {key: val for key, val in dict(Counter("".join(test_list))).items() if key in chr_list}

print("Specific Characters Frequencies : " + str(res))
'''
########################################################################################################################
# Split Method Explanation

# Syntax : str.split(separator, maxsplit)

# Parameters :
# separator : This is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.

# maxsplit : It is a number, which tells us to split the string into maximum of provided number of times. If it is not provided then the default is -1 that means there is no limit.

# Returns : Returns a list of strings after breaking the given string by the specified separator
#################################################################################################
'''
s='1,2,3,4'   #o/p-->10
t=s.split(',')
print(t)
sum=0
for i in t:
    sum=sum+int(i)
print(sum)
'''

#####################################################################################################3

'''
d=["1,2,3,4"]    # o/p --> 10
sum=0
for i in d:
    print(i, "Value of i")
    k=i.split(',')
    print(k, '$$$')
    for j in k:
        # print("****")
        # print(j)
        sum=sum+int(j)
print(sum)
'''


'''
for i in d:
    for j in i:
        print(j)
        sum=sum+int(j)
print(sum)'''
###################################################################################################################
'''
word = 'CatBatSatFatOr'

# Splitting at t
print(word.split('t'))'''
#################################################################################################


'''
seperate=["Apple", "Bat", "Cog"]

for i in seperate:
      print(i)
'''
################################################################################################################

'''
k="Rahul Kumar"
h=k.split(" ")
print(h)
'''

##################################################################################################################

'''
name="Nelson"
l=name.replace('Nel', 'mom')
print(l)
'''

##################################################################################################################
'''

name=('Hello', 'How', 'Are', 'You')
str1='_'.join(name)
print(str1)
str2=' '.join(name)
print(str2)

# for i in str2:
#     print(i)

'''
###################################################################################################################

'''
word = 'geeks, for, geeks, pawan'

# maxsplit: 0
print(word.split(',', 0))

# maxsplit: 4
print(word.split(',', 4))

# maxsplit: 1
print(word.split(',', 1))

print(word.split(',', 8))
'''
#####################################################################################################################
'''
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 3)

print(x)
'''
############################################################################################################
'''
txt = "apple#banana#cherry#orange"

x = txt.split("#")
print(x)
'''

###############################################################################################

'''
str1 = 'geeks for geeks'
# Print the string without striping.
print(str1)

# String whose set of characters are to be remove from original string at both its ends.
str2 = 'ekgs'

# Print string after striping str2 from str1 at both its end.
print(str1.strip(str2))

'''
#####################################################################################################################

'''
# Interview Question
a=['1,4,5,6', '1,2,4,6']   # find out the common elements

print(a[0])
print(a[1])
# Getting an Output

def string1(str2):
    k=set(str2[0].split(','));print(k)
    m=set(str2[1].split(','));print(m)
    h=k.intersection(m)
    #print(h)
    str2=list(h)
    return str2

#print(string1(['1,2,3', '1,2']))
#print(string1(['1,4,5,6', '1,2,4,6']))
#set1 ={'1,2,3'}; set2={'1,2'}
#print(set1.intersection(set2))

s=['1,2,3', '1,2']
print(s[1].split(','))
'''


'''
# Not geeting an o/p from this program

for i in a:
    print(i)
    k=i.split(',')
    # print(k)
    d=set(k)
    print(d)
    # for k in d:
    #   h=

'''
#####################################################################################################

'''
s='1,2,3,4'
t=s.split(',')
print(t)
sum=0
for i in t:
    sum=sum+int(i)
print(sum)
'''

###########################################################################
'''
d=["1,2,3,4"]  # o/p --> 10

sum=0
for i in d:
    print(i, "Value of i")
    k=i.split(',')
    print(k, '$$$')
    for j in k:
        # print("****")
        # print(j)
        sum=sum+int(j)
print(sum)
'''


##############################################################################################################################
# Write a python function that takes a string, counts the number of integers in that string, and returns the count.
# For the purposes of this question, an integer is simply defined as a sequence of one or more digits.

# Thus if the function is called as: numints('11 degrees celcius is 51.8deg fahrenheit')
# then it should return 3 (because by our definition of integer, 11, 51 and 8 are 3 different integers.)

'''
def string(str1):
   str2=str1.split(',')
   print(str2)
   for i in str2:
       print(i)
       # str3=i.split(",")
       print(str3)
   return str3
'''
'''
def count(x):
    length = len(x)
    digit = 0
    # letters = 0
    # space = 0
    # other = 0
    for i in x:
        # if x[i].isalpha():
        #     letters += 1
        if i.isnumeric():
            digit += 1
        # elif x[i].isspace():
            # space += 1
        # else:
            # other += 1
    return digit
    # return number,word,space,other

s='11 degrees celcius is 51.8deg fahrenheit'
print(count(s))


letters = sum(c.isdigit() for c in s)
print(letters)


def count1(x):
    s=sum(c.isdigit() for c in len(x))
    return s


s1='11 degrees celcius is 51.8deg fahrenheit'
print(count1(s1))'''
###################################################################################################
'''

secondlast=('Sales,Nashik,6 Feb 2020,233')

h=secondlast.split(',')
print(h)
print(h[2])
print(type(h[2]))
'''
####################################################################################################

'''
def process_list(l1):
    l2=set(l1)
    l3=len(l2)
    return l3
print(process_list(['navin', 3, 7, 'navin', 3]))
'''
##################################################################################################
'''
o="aabbbbcccaa"
c="a2b4c3a2"

# h=o.count('a')
# print(h)

# k="2".join(o)
# print(k)
f=""
for i in o:
    k=i.count(i)
    if k==2:
        f='2'.join(i)
        print(f)


# for i in o:
#     k=i.split(',')
#     print(k)
# h=[i.split(',') for i in o]
# print(h)
'''
######################################################################################