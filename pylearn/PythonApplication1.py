# import platform


# print('''hello
# world
# nihao''')

# a = 1
# b = 'nihao'
# c = True
# print(a, '\n', b, '\n', c)

# a = 'abc'
# a = 1
# print(a)


# print(platform.python_version())    # 打印python版本


# print('\'a\'')    # \ + 'or" 使其不转义
# print(r'\'"')    # r' ' 使其中默认不转义
# print('''a
# b''')    # ''' ''' 之间可以换行
# print('a' + \
#    'b')    # \ 可以换行输入
# print(10//3)    # 地板除，只保留整数


# print(ord('刘'))    # 显示Unicode编码
# print(chr(75))    # 通过编码显示对应字符
# print('刘'.encode('utf-8'))    # encode来编码为对应格式
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))    # decode来以对应格式解码


# print('it is %s' % 'dio')    # 格式化输出


# listTest = ['1', '2', '3']    # list类型
# print(listTest)
# print(listTest[1])
# print(listTest[-1])
# listTest.insert(0, 'first')
# print(listTest)
# listTest.append('end')
# print(listTest)
# listTest.pop()
# print(listTest)
# listTest.pop(0)
# print(listTest)
# listTest[0] = True
# print(listTest)
# listB = [9, 8, 7]
# listTest.insert(1, listB)
# print(listTest)


# tupleC = (1, 2)    # tuple类型只可读
# tupleC = (1,)    # tuple只有一个元素时需要添加','消除歧义
# print(tupleC)
# tupleC = (1, 2, listB)    # tuple内部list内元素可以更改，tuple的限制只有一级
# tupleC[2][0] = True
# print(tupleC)


# age = input('age:')
# if int(age) >= 18:
#    print('age = %d' % int(age) + '\n>=18')
# elif age <= 15:
#    print('age = %d' % int(age) + '\n<=15')
# else:
# #    print('age = no')
# if age:
#    print(True)


# sum = 0
# for x in [1, 2, 3, 4, 5]:
#    sum = sum + x
# print(sum)
# while x > 0:
#    x -= 1    # python没有 -- ++ 只有 -= +=
#    if(x == 2):
#        continue
#    else:
#        print(x)
#        if(x == 1):
#            break


# d = {'a':1, 'b':2, 'c':3}    # dict对象（字典）
# print(d['a'])
# print('a' in d)
# print('d' in d)
# print(d.get('a', -1))
# print(d.get('d', -1))
# print(d.pop('b'))
# #k = [1, 2, 3]    key的对象不可变
# #d[k] = 'a'


# s = set([1, 2, 3, 3])    # set类型 也是key的集合，但是key不能重复
# print(s)
# s.add(4)
# print(s)
# #s.add([2, 2, 2]) 错误，key的对象不可变，python中字符串、整数等不可变可以作为key，list是可变的，所以不能
# print(s)
# s2 = set([2, 3])
# print(s & s2)
# print(s | s2)


# a = ['c', 'b', 'd', 'a']
# a.sort()
# print(a)


# def my_abs(x):    # Python的函数返回多值其实就是返回一个tuple
#    if not isinstance(x, (int, float)):
#        raise TypeError('bad operand type')
#    if x > 0:
#        return x
#    else:
#        return -x
# x = int(input('input:'))
# print(my_abs(x))

# def my_pass():
#    pass    # pass可以用来做占位符


# def add(x = 1, l = []):    # 默认参数必须为不变对象
#    x += 1
#    l.append('end')
#    print(x)
#    print(l)
# add()
# add()
# add()

# def calc(numbers):
#    sum = 0
#    for n in numbers:
#        sum = sum + n * n
#    return sum
# print(calc([1, 2, 3]))
# #print(calc(1, 2, 3)) 报错，因为变量数量不同 numbers为1  1,2,3为3

# def calc2(a, *numbers, **extra):    # *name 为可变参数，调用时直接传入参数即可 比如 (a, b, c) 或 (*[a, b, c])
#    sum = 0                         # **name 为关键字参数，调用时传入 键-值 name:value，会封装成dict
#    for n in numbers:
#        sum = sum + n * n
#    print(a)
#    print(extra)
#    return sum
# print(calc2(1, 2, 3))
# number = [1, 2, 3]
# print(calc2(*number))
# calc2(1, 1, d1 = {'a':1, 'b':2}, d2 = [1, 2, 3])

# def person(name, age, *b, city, job):    # * 后参数为命名关键字参数，传入时需要指定对应的参数名
#    print(name, age, b, city, job)
# person('a', 18, 1, 2, city = 'c', job = 'd')
# args = (1, 2, 3, 4)    # 传入参数可以用 (*args, **kw) 形式传入
# kw = {'city':'c', 'job':'j'}
# person(*args, **kw)

# def fact(n):    # 递归函数优化——尾递归，仅返回递归函数本身而不进行运算，参数运算会在调用函数之前进行
#    return fact_iter(n, 1)    # 使递归本身无论多少次调用，只占用一个栈，不会出现栈溢出的情况
# def fact_iter(num, product):    # 如果返回递归函数的运算的话，由于不知道下层的返回值，所以会存入栈中
#    if num == 1:    # 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧
#        return product
#    return fact_iter(num - 1, num * product)


# L = list(range(0, 100))
# print(L)
# print(L[10:30])


# #dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()


# g = (x * x for x in range(10)) #()内保存的为一个算法
# for n in g:
#    print(n)

# def odd():
#    print('step 1')
#    yield 1    # 相当于return 但下次继续从这里运行
#    print('step 2')
#    yield(3)
#    print('step 3')
#    yield(5)
# j = [i for i in odd()]
# print(j)
# # 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# # 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。（完整的过程）


# # 可迭代对象：Iterable     迭代器：Iterator     把list、dict、str等Iterable变成Iterator可以使用iter()函数
# # 凡是可作用于for循环的对象都是Iterable类型；
# # 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# # 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

# # test 切片    顾头不顾尾， 起点:终点:间隔
# l = [1, 2, 3, 4, 5, 6, 7]
# print(l[1:3])    # [2, 3]
# print(l[1:-1])    # [2, 3, 4, 5, 6]
# print(l[3:1])    # []
# print(l[1:4:2])    # [2, 4]
# print(l[5:2:-1])    # [6, 5, 4]