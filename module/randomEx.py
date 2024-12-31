import random  as ran

print(ran.randint(2,10))

n1 = ran.randrange(1,20) # 1 included and 20 excluded
print(n1)

l = [20,40,60,50,30]
lc= ran.choice(l)
print(lc)
ran.shuffle(l)
print(l)

u = ran.uniform(3,9)
print(u)


