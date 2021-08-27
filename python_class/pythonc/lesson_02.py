"""
============================
Project: python_class
Author:柠檬班-Tricy
Time:2021/8/13 19:22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
'''
find --  ok ,不推荐使用
_num -- ok
7val -- 不可以，数字开头
add. --- 不可以
def  ---   不可以 ，关键字
pan  --  ok
-print --  不可以，_ -
open_file  --ok
FileName  -- ok
print -- 可以的，不推荐；--影响函数的功能使用
INPUT --  ok，input()--大小写
ls -- ok
user^name -- 不可以
list1 -- ok， 推荐使用
str_  --  ok

字符串的常用方法续：
1、通过元素找位置 -- 获取索引
find  -- 返回元素的索引,元素不存在--返回-1，代码继续执行
index -- 返回元素的索引,元素不存在--代码报错，不会继续向下执行
2、count -- 统计这个元素出现的次数 （元素是可以重复）
3、替换 -- replace(old,new)
4、拆分 -- split : 把字符串按照指定的字符进行拆分，拆分结果存在列表里；
5、格式化输出 : 字符串输出的时候有些内容是变化的，向字符串里传入变量 == 
占位符-- {} -- 需要传变量的位置占位
format -- 变量传入 
1) 默认不指定位置 --  按照变量的顺序  传入
2） 指定位置传入  --- 不用按照位置输入变量  --索引
不同混合使用！

--扩展： %s-字符 ==全能 %d-数字 %f -小数
'''
# str1 = "二丫,itt,移动"
# # print(str1.find("小"))
# # print(str1.index("扬"))
# print(str1.count("t"))
# st2 = str1.replace("itt","青栀子")
# print(st2)
# tt = str1.split(",")
# print(tt)

# name = "yc"
# height = "168"
# weight = "45kg"
# print('''----%s是84期的班花！----
# name: %s
# 身高：%s
# 体重：%s
# '''%(name,name,weight,height))

# print('''----{}是84期的班花！----
# name: {}
# 身高：{}
# 体重：{}
# '''.format(name,name,weight,height))

'''
python运算符：
1、算术运算符 ： + - * /
+: 表示两个字符串的拼接
扩展：数据强制转化： int -> str  == int()-转化为整形，str()--转化为字符串，float(),bool()
*：字符串的重复输出 

2、赋值运算符  = +=  -= 
= : 右边的内容赋值给左边的变量

3、 比较运算符： > < >= <= == !=     ---- 运行结果是bool值
== : 表示字符串的相同比较 -- 测试结果比对-断言 == 预期结果 vs  执行结果

4、逻辑运算符 ：  与 - and(真真为真)，或-or(假假为假),非-- not  ------ 运行结果是bool值

5、成员运算符 ： in ， not in   ------- 运行结果是bool值

'''
# str4 = "青栀子oneday"
# print("二丫" not in str4)

# print(5 < 6 or 6 > 7)
# print( not 7 >= 8)
# print(5 < 4)
# print( "操作成功" == "操作成功")

# a = 10
# a += 5  # a = a + 5
# a -= 6
# print(a)
# print(2 + 3)
# print("小杨"+"棒")
# print("abc"+ str(123))
# print(10 - 4)
# print("我爱你" * 3000)

'''
数据类型： int float bool str , list  tuple  dict set
列表：list  --[]
1、元素可以是任意的数据类型 
2、统计元素个数 -长度 == len（）
3、取值 ： 索引取值 
   取多个值：切片 
扩展：列表的嵌套取值 -- print(list1[4][3])
4、列表的元素是可以被改变的
增加 删除 修改
5、元素是可以被重复的 -- count
'''
list1 = [20,3.14,False,"高进锋",[1,2,3,4,5]]   #列表定义
# 增加
list1.append("纯纯") # 追加元素到末尾 --最多
print(list1)
# list1.insert(3,"Rella") # 指定位置进行元素的添加
# list1.extend(["二丫","小梨","东东","熊熊","二丫"])  # 列表合并 -- 添加多个元素进列表
# # 删除
# print(list1)
# list1.pop(5) # pop 默认删除最后一个元素；但是可以指定索引进行删除元素
# list1.remove(False) # 指定元素本身进行删除
# # list1.remove("二丫")  # 如果元素重复了，删除找到的第一个
# # list1.clear() # 清除所有元素 --少
# print(list1)
# # 修改 --重新赋值
# list1[1] = "海豹"
print(list1.count("二丫"))
'''
元组：tuple  --()
1、元素可以是任意的数据类型 
2、统计元素个数 -长度 == len（）
3、取值 ： 索引取值 
   取多个值：切片 
扩展：嵌套取值 -- print(list1[4][3])
4、元组的元素是不可以被改变的  -- 列表区别
5、元素是可以被重复的 -- count
'''
tuple1 = ('Rella', '高进锋', '纯纯', '二丫', '小梨', '东东', '熊熊', '二丫')
# tuple1[0] = "Vicky"

'''
字典，集合 if判断   for循环 
'''
name = input("请输入你的名字：")  # 内置函数  --  获取在控制台输入内容
print(name)

