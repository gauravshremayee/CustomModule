#!/usr/bin/python

#import sttaements - libraries we are importing . 
import sys
import addStr as ad
from libDir import addNumMod as a

# function defintions 
finalStr=ad.returnAddedStr("Hey","FromBangalore!")

print("Final String is",finalStr)
a.test()
#main section  


print (sys.path)



import sys
print ("hello")

#Python variables are dynamic typed
#int ,str

var=5.2

print(type(var))

var2="World"

var3=str(var)+var2

print(var3)

var4=6/7

print(var4)

#taking input from user from argument and keyboard
#string ,numbers,data types 

input_var=input("Enter a number")

print(input_var)

str1="Hello"
str2="World"

strMain=str1+str2

print("Result string is",strMain)
#taking input as argument

num1=sys.argv[1]
num2=sys.argv[2]
print (type(num2))
sum=int(num1)+int(num2)

print (sum)

#literals processing 

#string literals numeric literals boolean
#Python multiline documentation

test="""gtkjkjtjtjkjdkjd
jfjjfjjfkjfkfkkf"""

print(test)


# single quotes
sq_str='Who was "that  person  or new one"?'

print(sq_str)
# double quotes
dq_str="Height varies from 5' to 3'."

print(dq_str)
# escaped quotes
eq_str= "\"That's pretty good !\" said his personal assistance."
# creates: "That's not fair!" yelled my sister
print(eq_str)
# triple quoted strings, with single quotes
tq_str= '''This one string can go
over several lines'''
print(tq_str)
# "raw" strings, mostly used for regular expressions
r_str= r"\"That's not fair!\" yelled my sister."
# creates: \"That's not fair!\" yelled my sister

print(r_str)

# You can even have raw triple double quoted strings!
rs_tq_str ="""So there!"""


#escaping the \ 
newline=r"Hey ! How are you  windows path \now i am  here?"

print (newline)

#boolean literals

ten=0b1010

print(ten)

hexd=0xa

print (hexd)
