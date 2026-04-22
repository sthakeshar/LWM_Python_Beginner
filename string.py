#for loop practice
name='keshar'
city='tokyo'
country='japan'

for ch in name:
    print(ch)

for ch in city:
    print(ch)

for ch in country:
    print(ch)

#for loop using range
for i in range(21):
    print(i)

for i in range(101):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,51):
    print(i)

for i in range(1,101):
    print(i)

#for loop using range and step
print('odd numbers from 1 to 20 are:')
for i in range(1,21,2):
    print(i)
print('even numbers from 1 to 20 are:')
for i in range(0,21,2):
    print(i)


for i in range(10,0,-1):
    print(i)

for i in range(25,9,-1):
    print(i)

for i in range(100,49,-1):
    print(i)

#break example
for i in range(1,11):
    if i==7:
        break
    print(i)

for i in range(1,50):
    if i==15:
        break
    print(i)

for i in range(1,11):
    if i==7:
        break
    print(i)

#continue example
for i in range(1,50):
    if i==15:
        continue
    print(i)

for i in range(10,0,-1):
    if i==7:
        continue
    print(i)

#sum from 1 to 100
sum=0
for i in range(1,101):
    sum+=i

print(f'sum from 1 to 100 is:{sum}')

#factorial from 1 to 10
fact=1
for i in range(1,11):
    fact*=i

print(fact)