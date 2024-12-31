str = "Welcome to coding world"
print("str[0:7]=",str[0:7])
print("str[0:]=",str[0:])
print("str[:10]=",str[:7])
print("str[:]=",str[:])
print("str[0:7:2]=",str[0:7:2])
print("str[0::2]=",str[0::2])

# reverse the string 
print("Reverse string", str[-1::-1],"\n")

# Iteration of string 
for i in range (0,len(str)):
    print(str[i])
 
for i in range(-1,-len(str),-1):
    print(str[i],"\n")
    
#print string character one by one without using range function 
str1 = str[-1::-1]
for i in str1:
    print(i)