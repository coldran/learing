class Chain(object):

    n = 0
    m = 0
    
    def __init__(self, path=''):
        __class__.m += 1
        print(self.m)
        self._path = path

    def __getattr__(self, path):
        __class__.n += 1
        if __class__.n > 2:
            print('self.path:', self._path)
        print('path:', self.n, path)
        return Chain('%s/%s' % (self._path, path)) #实际上调用了很多次这个函数

    def __str__(self):
        return self._path

    __repr__ = __str__

Chain().status.user.timeline.list