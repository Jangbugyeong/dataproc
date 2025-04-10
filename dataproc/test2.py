hit=0

while hit < 10:
    hit = hit +1
    print("나무를 %d번 찍었습니다" % hit)
    if hit == 10:
        print('나무가 넘어갑니다.')
hit=0
while True:
    hit = hit + 1
    if hit % 2 == 0:
        print("나무를 %d번 찍었습니다" % hit)
    if hit == 10:
        print('나무가 넘어갑니다.')
        break


j=0
while True:
    j += 1
    if j <=5:
        print('*'*j)
        if j >5:
            break
