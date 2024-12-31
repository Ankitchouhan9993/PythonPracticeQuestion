# unordered and unindex data type
# {}
# unique elements 

s = {30,70,60,30,40,70,89,78,65}
print(s)

# functions
"""sets()- convert any datatype in set
   add()
   pop()
   remove()
   clear()- return set( )
   discard()
   update()
"""
s.add(50)
print(s)
s.remove(60)
print(s)
s.discard(70)
print(s)

l = [68,76,56,38]
s.update(l)
print(s)
s.clear()
print(s)
