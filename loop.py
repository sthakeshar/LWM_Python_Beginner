word='areoplane'

count=0
for ch in word:
    if ch in ['a','e','i','o','u']:
        count+=1

print(count)

print("multiplication of 7")
for i in range(1,11):
    print (f"7 x {i} = {7*i}")

n=5
for j in range(1,n+1):
    print(j * '*')

for i in range(1,n+1) :
    for j in range(i):
        print("*",end="")
    print()

