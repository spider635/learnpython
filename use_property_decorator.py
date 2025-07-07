'''
class Student(object):
    @property # 把一个getter方法变成属性，只需要加上@property就可以了。此时，@property本身又创建了另一个装饰器@score.setter
    def score(self):
        return self._score

    @score.setter # 装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.score(60)
print(s.score) # OK，实际转化为s.score()
s.score = 9999 # ValueError
'''

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def resolution(self):
        return self._width * self._height
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @height.setter
    def height(self, value):
        self._height = value

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
