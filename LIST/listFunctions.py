# Functions for delete elements from list
"""
del
pop()
remove()
clear() 
"""
l = [23,80,67,45,34,86]
print(l)
del l[0]
print("list after del:",l)
print(l.pop(0))# delete elements by index
print(l)
l.remove(67) # remove element wise 
print(l)
l.clear()
print(l)

# update elements from list
l = [89,45,87,34,97,90,67]
l[0]=10
print(l)

l.insert(12)
print(l)

