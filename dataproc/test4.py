a= range(10)

print(a)

add=0
for i in range(1,11):
    add=add+i
    print(i,add)

print(add)

for i in range(2,10):
    for k in range(1,10):
        if i % 2 ==0 : print(i, " * ",k,"=",i*k)
        print(i*k, end="")
        print()

a=[70,60,55,75,95,90,80,80,85,100]
total=0
for i in range(10):
    total=total+a[i]
avg=total/len(a)
print(avg)

#다이아몬드 그리기

for i in range(5):
    if i == 0: print("  *")
    if i == 1: print(" *** ")
    if i == 2: print("*****")
    if i == 3: print(" ***")
    if i == 4: print("  *")
diamond=5

for j in range(diamond):
    space = abs(j - diamond//2)
    star = diamond-2*space



    print(' '*space,'*'*star)