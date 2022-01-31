import random

random_list = []

for i in range(0,10) :
    n = random.randint(50,100)
    random_list.append(n)
# print(random_list)

for i in random_list :
    print(i)
    

random_no = random.sample(range(30,60000), 30000)
print(random_no)