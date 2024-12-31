str = "Welcome to coding world"
print("lower:",str.lower())
print("upper:",str.upper())
print("title:",str.title())
print("capitalize:",str.capitalize())


print(str.find("m"))# give index number
print(str.find("e"))
print(str.find("e",2))
print(str.find("z"))# give -1 because z is not in string


print(str.index("e"))
print(str.index("e",2))
#print(str.index("z"))# give value error

# isalpha()
print(str.isalpha())
print(str.isdigit())
print(str.isalnum())

# chr()- take one argument as an integer and its check Ascii value and return character value 
x = chr(65)
print(x,type(x))

#ord()- it take a single unicode character (string of length 1) and returns an integer, so the formal is  
x = ord('A')
print(x,type(x))