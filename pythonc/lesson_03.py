"""
============================
Project: python_class
Author:柠檬班-Tricy
Time:2021/8/14 19:19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
'''
字典：-- dict  -{} --重要
1、元素： 多个键值对  key ： value
2、使用场景：什么时候需要使用字典保存数据？ -- 属性名字-属性值 == 方便取值
   人的信息：名字，年龄，身高 体重 爱好 电话号码
3、key 不可以被改变的（列表，字典--字符串做为key），不能重复的 （唯一的）;value 可以是任何数据类型，可以变化的；
4、字典的取值: 字典无序的--没有索引的 == 通过key 取value
5、字典里的value可以改变-- 增加 删除  修改
6、长度 -- 
'''
dict_info = {"name":"Rella","age":"18","height":"165cm","weight":"45kg"}
# 增加、修改
dict_info["hobby"] = "sing"  #赋值新的键值对 --key不存在，新增
dict_info["age"] = "19" # 赋值新的键值对--key存在 ，修改
# print(dict_info)
# 增加多个 -- 字典合并
dict_info.update({"city":"北京","gender":"female"})  # 一次性添加多个键值对
# print(dict_info)
# 删除
dict_info.pop("weight")   # 无序 --最后一个？？== 只能指定key删除
# print(dict_info)
# print(dict_info["name"])  # 通过key取值value
# print(dict_info.get("name"))  # 通过key取值value
# print(dict_info.keys())
# print(dict_info.values())
# print(dict_info.items())
# print(len(dict_info))

'''
集合-- set {} --扩展内容
1、元素是不能重复
2、无序的
3、使用场景  -- 可以给列表 去重
'''
# list1 = [11,22,33,44,44,77,77,11]
# print(list1)
# # 不重复元素的个数 -- 把列表转化为集合 -自动去重
# set1 = set(list1)  # 把列表转化为集合 --set() --内置函数
# print(set1)
# list2 = list(set1)
# print(list2)

'''
Python控制流：if判断， for循环
if判断 --分支
语法：
1、elif可以没有，可以有多个
2、条件一定是成立的--才会进入分支 -- True
3、冒号-- 父子关系 --子代码 == 四个空格缩进（tab键）
if  条件（身高180）：-- 条件成立
    分支-执行语句（男朋友）
elif  条件（帅）：
    分支-执行语句（考察）
elif 条件（钱）：
    分支-执行语句（考察）
elif 条件（才华）：
    分支-执行语句（考察）
else:--- 没有条件，
    单身汪
'''
# money = int(input("请输入你的财产金额："))  # input输入内容-字符串
# if money >= 200:  # True
#     print("买大房子！")
# elif money  >=100:
#     print("付首付")
# elif money >= 50:
#     print("买车")
# elif money >=10:
#     print("吃好的，旅游！")
# else:
#     print("乖乖学习，好好工作！")

'''
for循环：遍历所有的元素-- 字符串，列表 元组  字典 
冒号： 缩进--子代码== 循环体
1、循环次数-- 由谁来决定？==元素个数（长度）
2、debug --调试
1） 打断点 -- 调试会这行开始执行
2） 点击dbeug 按钮
3） 单步执行
3、跳出循环 
1) break: 满足条件的时候跳出整个循环 --后面的所有的循环都不会执行
2)continue：满足条件的时候跳出当次循环 --后面的所有的循环继续执行
4、内置函数经常一起使用-- range
生成一个整数序列 -- range()  range(0,10,1) -- 0,1,2,3,4,5,6,7,8,9
开始数字：0 --省略 --默认0
结束数字:10 --取头不取尾 -- 必须要写
步长:1 --默认1
'''
# count = 0
# str3 = "柠檬班全程班的学生是最棒的！"
# for i in str3:
#     if i == "全":
# #        break
#         continue
#     print(i)
#     print("*" * 20)
#     count += 1
# print(count)
# print(len(str3))
# for i in range(5):
#     print(i)

'''
Python的函数:
如果有一段代码需要被重复的使用-- 封装成函数 -- 调用这个函数就可以了 = 提高代码复用率
1、封装函数的语法：
def 函数名(): -- 自己取名的== 标识符，符合命名规则
    函数体（实现函数功能的具体代码）
2、函数定义完之后，要调用才会被运行！！--怎么调用？--使用函数名调用！

3、如果是容易变化的值-不会写死在函数里--传入==定义成为函数的参数
用变量代替具体的值 -- 括号里== 参数-- 形参

3.1 定义函数的时候，定义的参数 
必备参数：定义了必须要传，不传报错！
默认参数：当参数有一些经常使用的值的时候，设置为默认参数==定义默认值，可以不传；可以传入-- 以实参为准！
 位置要求：默认参数要在必备参数的后面！
不定长参数：不确定有还是没有，有多少？
  *args：前面的必备参数 默认参数都接受完了，剩下的所有的参数都被args参数接受，并且以元组的格式保存。--- 位置传参
  **kwargs: 前面的必备参数 默认参数都接受完了，剩下的所有的参数都被kwargs参数接受,并以字典的格式保存 -- 关键字传参
  
3.2 调用函数的时候，传入的参数， 实参
1) 位置传参：参数相关的 
2）关键字传参：不会跟位置性格，顺序错没有关系 -- 精确
3) 混合传参：关键字传参 一定要放在位置传参的后面 

函数有进有出-- 进- 参数，出-返回值
返回值：函数运行完会后，有数据要给别人用的 -- 这个数据定义为返回值！==得到这个返回值。
怎么定义？ -- return
得到返回值？--  调用时候，接受这个返回值
1、返回值 可以没有-- None
2、也可以有一个，可以有多个 --逗号隔开，接受的是用元组保存的。
3、定义返回值--- 意味着函数结束，后面的代码都不会再运行了！
'''
# print('66666') # 无用代码
def good_job(salary,bonus,subsidy=500,*args,**kwargs):  # 形参
    print("salary参数的值是：{}".format(salary))
    print("bonus参数的值是：{}".format(bonus))
    print("subsidy：{}".format(subsidy))
    print("arges参数的值是：{}".format(args))
    print("kwarges参数的值是：{}".format(kwargs))
    sum1 = salary + bonus + subsidy
    for i in args:
        sum1 += i
    for j in kwargs:
        sum1 += kwargs.get(j)
    print("这个工作的工资总和是：{}".format(sum1))
    return sum1, salary # 定义了返回值
    print("这个代码运行完了么？")

result = good_job(9000,2000,800,100,200,300,a=100,b=200,c=300)  # 函数的调用--参数的传入 = 实参
print(result)
# 变量来接受函数的调用-- 返回值
# if result > 10000:
#     print("这是一个好的工作！")
# else:
#     print("这个工资不行！")
'''
内置函数：
1、print，type  isinstance , input
2、len(),range()
3、int, float, bool,str, list , tuple, set, dict
4、字符串的方法： str.index str.find str.replace str.split count 
5、列表 字典的方法： list.append，list.insert，list.pop, list.remove
'''
dic1 = {"name":"青栀子","age":"18"}
dict2 = dict(name="青栀子",age=18)
print(type(dict2))




