fruits = ["apple", "mango", "orange", "banana"]
for i in range(len(fruits)):
    print(i+1,fruits[i])

hardwares = ["mouse","keyboard","printer","monitor"]
for i,hardware in enumerate(hardwares,1):
    print(i, hardware)

i=1

while(i<=10):
    print(i)
    i=i+1

j=10

while(j>=1):
    print(j)
    j=j-1

i = 0

while i < 15:
    i += 1
    if i == 9:
       continue
    print(i)