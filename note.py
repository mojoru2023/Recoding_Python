

import os


themes = ["1.数据结构和算法","2.字符串和文本","3.数字，日期和时间","4.迭代器和生成器","5.文件和I_O","6.数据编码和处理","7.函数","8.类与对象","9.元编程","10.模块和包","11.网络和Web编程","12.并发","13.实用脚本和系统管理","14.测试、调试以及异常","15.C语言扩展"]
base = "/home/karson/Recoding_Python/"
for i in themes:
    file_name = base + str(i)
    os.mkdir(file_name)