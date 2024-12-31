#format()- the format() methods specified value(s) and insert them inside the strings placeholder. The placeholder is defined using curly brackets:{}.
str1 = "Welcome to {something} {anything}".format(something="coding",anything="world")
print(str1)
str1 = "Welcome to {0} {1}".format("coding","duniya")
print(str1)
str1 = "Welcome to {} {}".format("new","world")
print(str1)
str1 = "Welcome to {a:10} {b:3}".format(a="apni",b="world")# print a value in 10 character
print(str1)
str1 = "Welcome to {a:^10} {b:3}".format(a="apni",b="world")# ^ it indicate the value of a print in center within given size (10)
print(str1)
# < left like 5----
#< right like ----5
#^ center like --5--
str1 = "Welcome to {a:<10} {b:3}".format(a="apni",b="world")# ^ it indicate the value of a print in center within given size (10)
print(str1)
str1 = "Welcome to {a:>10} {b:3}".format(a="apni",b="world")# ^ it indicate the value of a print in center within given size (10)
print(str1)

