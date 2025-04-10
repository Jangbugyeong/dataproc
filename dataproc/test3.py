test_list = ['one','two','three']


for j in test_list:
    print(j)


for j in range(len(test_list)):
    print(j,test_list[j])

for idx, j in enumerate(test_list):
    print(idx,j)

test_tuple = [(1,2),(3,4),(5,6)]
for (first, second) in test_tuple:
    print(first,second)


scores = [90,25,67,45,80]

num=0
for score in scores:
    num+=1
    if score >= 60:
        print("%d번째 학생은 합격입니다."% num)
    else:
        print("%d번째 학생은 불합격입니다."% num)