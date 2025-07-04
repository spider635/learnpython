# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

# person('yb', 43)

# def person(name, age, *, city, job):
#     print(name, age, city, job)

# person('yb', 43, city="cd")

# def person(name, age, *args, city, job):
#     print(name)
#     print(age)
#     if args:
#         for x in args:
#             print(x)
#     print(city)
#     print(job)

# person('yb', 43, 34,343,343434,city='CD', job='engineer')

def mul(*args):
    if not args:
        raise TypeError("args is empty.")
    elif len(args) == 1:
        return args[0]
    else:
        sum = 1
        for x in args:
            sum = sum * x
        return sum

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')
