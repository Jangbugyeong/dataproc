def add(a,b):
    return a+b

print(add(3,5))

c=add(4,8)
print(c)

def add_and_mul(a,b):
    return a+b,a*b

print(add_and_mul(3,8))
c, _=add_and_mul(4,10)
print(c)

def say_hello():
    print("hello")
say_hello()

def add_many(*args):
    result = 0
    for j in args:
        result += j
    return result

print(add_many(1,2,3,4,5,6))

def add_sub(choice,a,b):
    if choice == 'add':
        return a+b
    elif choice == 'sub':
        return a-b
    else:
        print("choice를 다시 입력 해 주세요. add나 sub이어야 합니다")

print(add_sub('add',3,4))
print(add_sub('sub',3,4))
print(add_sub('mul',3,4))

def read_num(num):

    if num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 0:
        return 'zero'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    elif num == 9:
        return 'nine'
    elif num == 10:
        return 'ten'
print(read_num(1))
print(read_num(2))
print(read_num(0))

def tri(a):
    return a*3
print(tri(3))
print(tri('x'))
