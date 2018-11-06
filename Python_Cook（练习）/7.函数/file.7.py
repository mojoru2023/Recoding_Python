# ７．７　在匿名函数中绑定变量的值

# 7.7.1 问题

# 我们利用lambda表达式定义了一个匿名函数，但是也希望可以在含税定义的时候完成对特定变量的绑定。
# ７．７．２　　解决方案

x = 10
a = lambda y:x+y
x = 20
b = lambda y:x+y

# a(10) 与 b(10)的结果都是３０

# 这里的问题在于lambda表达式中用到的x是一个自由变量，在运行是才进行绑定而不是定义的时候绑定。因此，lambda表达式中x的值应该在执行时
# 确定　，执行时x的值是多少就是多少。如下

x= 15
print(a(10))

# 如果希望匿名函数可以在定义的时候绑定变量，并保持值不变，那么可以将那个值作为默认参数实现，如下

# x = 10
# a = lambda y,x=x:x+y
# print(a(10))
# x = 20
# b = lambda y,x=x:x+y
# print(b(10))

# 7.7.3 讨论
# 本节中提到的问题一般比较容易出现在那些对lambda函数过于"聪明"的应用上。比方说，通过列表推导来创建一列lambda表达式，或在
# 一个循环中期望lambda表达式能够在定义的时候记住迭代变量，如下

funcs = [lambda x:x+n for n in range(5)]
for f in funcs:
    print(f(0))


#  我们可以注意到所有的函数都认为n的值为４,也就是迭代中的最后一个值。我们再和下面的代码作对比

funcs = [lambda x,n=n:x+n for n in range(5)]
for f in funcs:
    print(f(0))

# 可以看到，现在函数可以在定义的时候捕获到n的值了