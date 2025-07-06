class Student(object):
    def __init__(self, name, score):
        self._name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

yb = Student('yb', 98)

print(yb._name)
# print(yb.__score) # 报错 AttributeError: 'Student' object has no attribute '__score'

# 其实仍然可以通过改写后的名称访问。所以只是一种约定。
print(yb._Student__score)
