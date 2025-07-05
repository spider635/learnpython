def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()

next(o)
next(o)
next(o)

def count_up_to(max):  # This is a generator function
    count = 1
    while count <= max:
        yield count  # It yields values one by one
        count += 1

# Using the generator
counter = count_up_to(5)  # This returns a generator object
for num in counter:
    print(num)

def pascal_triangle():
    row = [1]  # 第一行
    while True:
        yield row
        # 生成下一行：
        # 新行 = [1] + [上一行的相邻两数之和] + [1]
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

# 创建一个生成器对象
pt = pascal_triangle()

# 输出前10行杨辉三角
for _ in range(10):
    print(next(pt))

