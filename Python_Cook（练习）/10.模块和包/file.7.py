# 10.7 让目录或zip文件成为可运行的脚本

# 10.7.1 问题
# 我们的程序已经从一个简单的脚本进化为一个设计多个文件的应用。我们希望能有某种简单的方法让用户来运行这个程序
# 10.7.2 解决方案
# 如果应用程序已经进化为有多个文件组成的“庞然大物”，则可以把它们放在专属的目录中，并为之添加一个__main__.py.例如，可以
# 创建一个这样的目录：
# 如果有__main__.py,就可以额在顶层目录中运行Python解释器，
#  bash % python3 myapplication
# 解释器会把__main__.py文件作为主程序来执行
# 这项技术在我们把所有的代码打包进一个zip文件中时同样有效

# 10.7.3  讨论
# 创建一个目录或zip文件，并在其中添加一个__main__.py，这是一个打包规模较大的python应用程序的可行方法。但是这和安装到
# Python标准库中的包有所不同，在这种情况下，代码并不是作为标准库中的模块来使用的。相反，这里只是把代码打包起来方便其他人执行

# 由于目录和zip文件同普通文件相比有一些小的区别，我们可能也想添加一个shell脚本来让执行步骤变得简单。如果，代码位于名为myapp.zip的文件中
# 则可以想如下创建一个顶层的脚本：

#! /usr/bin/env python3 /usr/local/bin/myapp.zip

