from functools import wraps

def log(arg):
    # 判断参数是字符串（带参数调用）还是函数（无参数调用）
    if isinstance(arg, str):
        # 带参数的情况，arg是前缀字符串
        prefix = arg
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print(f'{prefix} begin call')
                result = func(*args, **kwargs)
                print(f'{prefix} end call')
                return result
            return wrapper
        return decorator
    else:
        # 不带参数的情况，arg就是被装饰的函数
        func = arg
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('begin call')
            result = func(*args, **kwargs)
            print('end call')
            return result
        return wrapper

# 不带参数的情况
@log
def f():
    print('f() is running')

f()
# 输出:
# begin call
# f() is running
# end call

# 带参数的情况
@log('execute')
def g():
    print('g() is running')

g()
# 输出:
# execute begin call
# g() is running
# execute end call
