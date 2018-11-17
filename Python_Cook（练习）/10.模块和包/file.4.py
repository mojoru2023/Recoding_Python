# 10.4 将模块分解成多个文件
# 10.4.1 问题
# 我们想将一个模块分解成多个文件。但是，我们不想破坏下载已经在使用这个模块中的代码，而是希望可以将多个单独的文件在逻辑上统一成一个单独的模块

#10.4.2  解决方案
#可以通过将模块转换为包的方式将模块分解成多个单独的文件。考虑下面这个简单的模块：

# 假设想把mymodule.py分解为两个文件，每个文件中包含一个类的定义。要做到这点，可以从把mymodule.py替换成目录mymodule开始
# 最后在文件__init__.py将来两个文件绑定在一起

# 10.4.3 讨论
#　本节主要考虑的是一个设计上的问题。即，我们希望用户使用大量的小型模块，还是希望它们只使用一个单独的模块。例如，在一个庞大的代码库中，
# 我们可以把所有的东西分解成单独的文件，并让用户写下大量的import语句。
# 通常，可以吧啊mym想象成一个大型的源文件。但是，本节演示了如何在逻辑上把多个文件拼接成一个单独的命名空间的技术。关键之处在于创建一个包目录
# ，并通过__init__.py文件将各个部分粘连在一起

# 当分解模块时，需要对跨我文件名的引用要多加小心。如，本例中，class B需要把class A当做基类来访问。我们采用from.a import  Az这种
# 相对包的导入方式来获取class A的定义

# “惰性”导入。__init__.py文件一次性将所有需要的组件导入进来。但是，对于非常庞大的额模块，也许
# 只希望在实际需要的时候才加载那些组件。
# class A 和 class B 已经由函数取代了。当首次访问它们时会加载需要的了i

# 惰性加载的主要缺点在于会破坏继承和类型价差机制