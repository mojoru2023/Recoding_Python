#  1.2 如何使用特殊方法

#  首先明确一点，特殊方法的存在是为了被python解释器调用的，也就是说没有my_object.__len__()这种写法，而应该是len(my_object)
#  在执行len(my_object)的时候，如果my_object是一个自定义类的对象，那么python会自己去调用其中由你自己去实现的__len__方法

#  然而如果是python内置的类型，比如列表(list),字符串(str),字节序列(bytearray)等，CPython会抄近路，__len__实际上会直接返回PyVarObject
#  里的ob_size属性．PyVarObject是表示内存中长度可变的内置对象的C语言结构体．直接读取这个值比调用一个方法要快很多

#  很多时候,特殊方法的调用是隐式的,比如for i in x:这个语句,背后其实用的是iter(x) ,而这个函数的背后是x._iter__()方法.
#  当然前提是这个方法在x中被实现了.
#  通常你的代码无需直接使用特殊方法,除非有大量的元编程存在,直接调用特殊方法的频率应该远远低于你去实现的次数.唯一的例外可能是__init__方法,
#  你的代码里可能经常用到它们,目的是在你自己的子类的__init__方法中调用超类的构造器

#  通过内置的函数(如,len,iter,str等)来使用的特殊方法是最好的选择.这些内置函数不仅会调用特殊方法,通常还提供额外的好处,而且瑞雨内置的类来说,它们的速度更快

#  不要自己想当然随意添加特殊方法,比如__foo__之类的,

#  1.2.1  模拟数值类型

#  利用特殊方法,可以让自定义对象通过加号"+"(或别的运算符)进行运算

#  我们来实现一个二维向量(vector)类,这里是几何概念

#  python内置的complex类可以用来表示二维向量,但是我们这个自定义的类可以扩展到n维向量

#  为了给这个类设计api,我们先写个模拟的控制台来做doctest

from vector import Vector

v1 = Vector(2,4)
v2 = Vector(2,1)
print(v1+v2)

# 注意其中的+运算符所得到的结果也是一个向量,而且结果能被控制台友好的打印出来,abs是一个内置函数,如果输入是整数或浮点数,它返回的是输入值的绝对值;
#  如果输入是复数(complex number)那么返回这个复数的模.为了保持一致性,我们的api在碰到abs函数的时候,也应该返回该向量的模

print('~'*88)

v = Vector(8,8)
print(abs(v))

#  我们还可以利用*运算符来实现向量的标量乘法(即向量与数的乘法,得到的结果向量的方法与原向量一直,模变大)

print(v*3)
print(abs(v*3))


# 下面示例包含了一个Vector类的实现,上面提到的操作在代码里是用这些特殊方法实现的:__repr__,__abs__,__add__,__mul__

#  虽然代码的里有6个特殊方法,但是这些方法(除了__init__)并不会在这个类自身的代码中使用.即便其他程序要使用这个类的这些方法也不会直接调用它们
#  一般只有python的解释器会频繁地直接调用这些方法.接下来看看每个特殊方法的实现


#  1.2.2  字符串表示形式

#  python有一个内置的函数叫repr,它把一个对象用字符串的形式表达出来以便辨认.这就是"字符串表示形式".repr就是通过__repr__这个特殊方法来得到一个对象的字符串
#  表示形式的.如果没有实现__repr__,当我们在控制台里打印一个向量的实例时,得到的字符串可能会是
#
#  交互式控制台和调试程序(debugger)用repr函数来获取字符串表示形式,在来的使用%符号的字符串格式中,这个函数返回的结果用来代替%r 所代表的对象;同样
#  str.format函数所用新式字符串格式化语法也就是利用了repr,才把!r 字段变成字符串

#  %　和　str.format这两种格式化字符串的手段都会用到

#  在__repr__的实现中，我们用到了%r来获取对象各个属性的标准字符表示形式---它暗示一个关键：Vector(1,2) 和Vector('1','2')是不一样的
#  后者在我们的定义中会报错，因为向量对象的构造函数只接受数值，不接受字符串
#  实际上Vector的构造函数接受字符串．而且，对于使用字符串构造的Vector,这６个特殊方法中，只有__abs__和__bool__会报错

#  __repr__所返回的字符串应该准确，无歧义，并且尽可能表达出如何用代码创建出这个被打印的对象．因此这里使用了类似调用对象构造器的表达形式(比如Vector(3,4))

#  __repr__和__str__的区别在于，后者是在str()函数被使用，或是在用print函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好

#  如果你只想实现这两个特殊方法中的一个，__repr__是更好的选择，因为如果没有一个对象没有__str__函数，而且python又需要调用它的时候，解释器会用__repr__作为替代

#  １．２．３　算术运算符

#  通过__add__和__mul__，为向量类带来了+和*这两个算术运算符．值得注意的是，这两个的返回值都是新创建的向量对象，被操作的两个向量(self或other)
#  还是原封不动的，代码里只是读取了它们的值而已．中辍运算符的基本原则就是不改变操作对象，而是产出一个新的值

#  乘法的交换律则被湖绿

#  １．２．４　　自定义的布尔值

#  尽管python里有bool类型，但实际上任何对象都可以用于需要布尔值的上下文中(比如if或while语句，或and,or,not运算符)为了判定一个值x为真还是为假
#  ，python会调用bool(x) ，这个函数只能返回True或Ｆalse
#  默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对__bool__或__len__函数有自己的实现．bool(x) 背后是调用x.__bool__()的结果；
#  如果不存在__bool__方法，那么bool(x)会尝试调用x.__len__().若返回０，则bool会返回False；否则返回True

#  我们对__bool__的实现很简单，如果一个向量的模是0,那么就返回False，其他情况则返回True.因为__bool__函数的返回类型应该是布尔类型，
#  所以我们通过bool(abs(self)) 把模值变成了布尔值

#  通过__bool__,你定义的对象就可以与这个标准保持一致

#  如果想让Vector.__bool__更高效，可以采用如下实现形式：

def __boo__(self):
    return bool(self.x or self.y)

# 通过bool把返回类型显式转换为布尔值是为了符合__bool__对返回值的规定，因为or运算符可能会返回x或返回y本身的值：若x的值等价于真，
#  则or返回x的值；否则返回y的值






