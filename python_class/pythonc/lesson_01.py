"""
============================
Project: python_class
Author:柠檬班-python
Time:2021/8/10 20:40
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
'''
取名：自己取名叫做--标识符 == 命名规则  --记忆
1、只能包含数字、字母、下划线  == 变量 函数
2、不能以数字开头  
3、不能使用关键字  ==  Python代码有特殊意义的一些字符 ==不需要记
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 'try', 'while', 'with', 'yield']
4、不同的数字和字母之间，最好用下划线隔开  -- 推荐,阅读更佳   python_class_8483 
-- PythonClass --大驼峰，Pythonclass 

运行脚本：很多方式--习惯用哪个
1、右键运行

注释的作用
1、给别人看，自己看  --  解释代码，方便理解
2、改需求，重新写代码  -- 备份
注释方式：
1、单行注释-- # 后面的内容都会被注释掉
2、多行注释 -- ''' '''  包裹内容被注释
3、快捷键 ： ctrl + /  == 注释和反注释 单行/ 多行

Python语法规定
1、Python区分大小写
2、缩进非常敏感，代码顶格编写  == 判断 函数-子代码

常用数据类型：
1、整型 - int ==整数数字
确认数据类型： 
type（）-内置函数：得到出来数据类型
isinstance -- 做个判断-匹配-True， 不匹配-False
2、浮点型 -- 小数 
3、布尔型： True --真(1)   False-假 (0)
4、字符串 ： str  用成对的引号括起来的内容 --单引号，双引号,三引号
1）引号嵌套使用  -- 两种引号
2）三引号-- 可以保持格式-- 所见即所得
常用方法：
1、统计长度 --len()-- 内置函数：统计元素个数-长度
2、字符串的取值：每个元素都有自己的位置 -编号，从0开始 == 索引 [索引]
      取多个值：切片 -- [索引头:索引尾:步长] == 取头不取尾 
            索引头： 默认值=0  --省略
            索引尾： 默认值 =最末尾--省略
            步长：默认=1 --省略
3、最后一个元素 -- -1  ==  扩展：  步长-1 ，实现字符串的逆序输出

变量：存储数据的 
1、取名字 -- 变量名 == 标识符 ==命名规则
2、见名知意 == 阅读星
3、一定要先申明， 再调用  --从上到下运行

'''
info = "丁娇是84期的班花！"  # 变量的定义+赋值 == 申明
    #   0 1 2345 6 7 89
print(len(info)) # 变量的调用
print(info[1])  # 索引
print(info[::-1])
print(info[-1])   # 最后一个元素 -索引  -1

# print -- Python的内置函数 （Python预先写好的，可以实现某个功能），功能-- 打印内容到控制台
# print("小杨是83期的班花！") # 这个是注释
# print("丁娇是84期的班花！")
# print("21是84期的班花！")
# print("88是84期的班花！")
# print(type('''623'''))
# print(isinstance("落雪",str))
print("83期"
      "的'小杨'是班花！")
print('''----88是84期的班花！----
name: 88
    身高：165cm
        体重：45kg
''')

