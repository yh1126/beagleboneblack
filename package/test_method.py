class A(object):
    def __init__(self):
        self.w = 1234

    def test1(self, x):
        print('test1 method', x)
        return x

class B(A):
    def test2(self, x):
        print('test2 method', x)

class C(B):
    def __init__(self):
        super().__init__()

    def test3(self, x):
        super().test2(x)
        super().test1(x)

    def test(self):
        x = self.test3
        x(1)
        print(self.w)

if __name__ == '__main__':
    c = C()
    c.test3(1)
    c.test()
