#  14.13  案例分析:在数据库转换工具中使用生成器

#  14.14  把生成器当成协程

#  与.__next__()方法一样,.send()致使生成器前进到下一个yield语句,不过,.send()方法还允许使用生成器的客户把数据发给自己,即不管传给.send()方法
#  什么参数,那个参数都会成为生成器函数定义体中对应的yield表达式的值..send()方法允许在客户代码和生成器之间双向交换数据.而.__next__()方法
#  只允许客户从生成器中获取数据
#  这是一项"改进",甚至改变了生成器的本性:生成器就变成为协程

#  生成器用于生成供迭代的数据
#  协程是数据的消费者
#  不要把生成器和协程 混为一谈
#  协程与迭代无关.注意,虽然在协程中会使用yield产出值,但这与迭代无关

#  杂谈
#  生成器函数的语法糖更多一些更好.协程经常会用到特殊的装饰器,这样就能与其他的函数区分开.可是生成器函数不常使用装饰器,因为我们不得不扫描函数
#  的定义体,看有没有yield关键字,以此判断它究竟是普通的函数,还是完全不同的东西

#  生成器与迭代器的语义对比
#  思考迭代器与生成器之间的关系时,可以从三个方面入手:

#  1. 接口. Python的迭代器协议定义两个方法:__next__和__iter__.生成器对象实现了这2个方法,因为从这方面来看,所有生成器都是迭代器.由此
#  可以得到,内置的enumerate()函数创建的对象是迭代器

from collections import abc

e = enumerate('ABC')
print(isinstance(e,abc.Iterator))
#  2. 实现方式.从这角度来看,生成器这种python语言结构可以使用两种方式编写:含有yield关键字的函数,或生成器表达式.调用生成器函数或执行
#  生成器表达式得到的生成器对象属于语言内部的GeneratorType类型
#  从这个方面来看,所有生成器都是迭代器,因为GeneratorType类型的实例实现了迭代器接口.不过,我们可以编写不是生成器的迭代器,方法是
#  实现经典的迭代器模式.
#  生成器-迭代器对象的类型,调用生成器函数时写成

#  3. 概念.在典型的迭代器设计模式中,迭代器用于遍历集合,从中产出元素.迭代器可能相当复杂,例如,树状数据结构,但是,不管典型的迭代器中有多少逻辑,都是
#  从现有的数据源中读取值;而且,调用next(it)时,迭代器不能修改从数据源中读取的值,只能原封不动地产出值

#  而生成器可能无需遍历集合就能生成值,例如range函数.即便依附于集合,生成器不仅鞥产出集合中的元素,还可能产出派生自元素额其他值.enumerate函数
#  是很好的例子.根据迭代器设计模式的原始定义,enumerate函数返回的生成器不是迭代器,因为创建的是生成器产出的元组

#  从概念方面来看,实现方式无关紧要.不使用python生成器对象也能编写生成器