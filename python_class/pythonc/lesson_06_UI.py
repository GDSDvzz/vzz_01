"""
Project: python_class
Author:柠檬班-Tricy
Time:2021/8/21 18:54
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
"""
"""
人  --操作--  浏览器 
代码      ----翻译（中间件）-----   浏览器
python/java    浏览器驱动
          Chrome/Firefox/IE/Edge驱动
          
借助工具：selenium工具包--了解 === UI自动化，python/java通用--三个部分
1、ide --- 录制脚本  --- 不精确，改善
2、webdriver : 库--提供对网页操作的各种方法，结合语言来用 == 驱动--重点
3、grid -- 分布式 。同时对多个浏览器执行并发  -- 少

跟浏览器建议个会话--启动了一个浏览器：各种操作
1、打开网址
2、窗口最大化
3、前进 后退 刷新
4、关闭浏览器

暂停-等待：time
"""
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()  # 选择chrome浏览器 --跟浏览器建立会话 ==赋值 给driver
# 1、打开具体的网址
# driver.get("https://baidu.com")
# #2、窗口最大化
# driver.maximize_window()
# #3、前进 后退 刷新
# driver.get("https://taobao.com")
# time.sleep(2)  # 等待= 2s
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# #4、关闭浏览器
# driver.close()  # 关闭当前的窗口
# driver.quit() # 关闭整个浏览器

"""
页面的元素定位==  找元素== 操作（点击 输入等）
html页面： HTML + css + js
HTML：定义页面呈现的内容 ：标签语言  ==元素都在页面
CSS：控制页面的如何呈现 -- 布局设置 --字体 颜色 大小
js：控制页面行为== 不同情形做不同事情

html 标签语言 ==  标签名 + 属性  ==元素寻找
input  -- 输入内容
div ==块
前端开发  -- 页面 遵循法则 --原则 ： 标签 --  id -- 唯一
人  -- 名字，身高，体重。。。身份证ID

1、元素定位方法： id ，name, xpath(重点)
2、四大-进行操作：
输入内容:send_keys
点击:click
获取文本:text
获取属性：get_attribute

xpath：元素再html页面里的路径

绝对路径：从根节点开始，按照下标来一级一级找  == 以/开始，严格继承关系，容易导致这个元素找不到 -- 非常少
/html/body/div[1]/aside/div/section/div[1]/div[2]/p
相对路径：以//开头，不管你前面有多少/谁，当前从这个标签开始； 不完全依赖父子  兄弟（偶尔可以借用）--灵活，非常多
//input[@id="username"]  === 不会去拷贝，会自己编写xpath的表达式

面试题：xpath 浏览器 唯一定位 --- 代码运行报错 找不到元素 ？？--高频
1、页面没加载完  -- 等待
2、当页面里存在子页面 --进行子页面的切换 ==iframe， 切换
3、id变化的

如何切换iframe：
1、id/name 切换 --id
注意： 当id 是变化的，就不能被用来作为元素定位。
2、没有id， 通过元素定位 切换

三大等待： 当页面发生切换，页面很有可能需要时间加载 --在页面切换之后，加一个等待。
1） 强制等待：设置的时间，必须等完 --不太灵活，影响代码运行速度
2） 智能等待： 只要元素出现了，也可以继续往下面执行
 a、隐式等待：一般一个会话（浏览器打开--浏览器关闭）只执行一次-- 写在代码顶部 + 强制等待
 b、显示等待： 以后在自动化学习！

"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐式等待 == 10s，如果元素提前出现，提前结束等待； 10s后还没有出现，报错！==整个会话
driver.get("http://erp.lemfix.com/login.html")
# 页面的标题
title = driver.title  # 获取页面的标题
print(title)
username = driver.find_element_by_id("username")  # id 唯一
username.send_keys("test123") # 输入内容-- 用户名
driver.find_element_by_id("password").send_keys("123456")  # 输入密码
driver.find_element_by_id("btnSubmit").click() # 点击操作
# time.sleep(2)  # 强制等待
# 判断是否登录成功
username = driver.find_element_by_xpath("//p").text  # 获取元素的文本
if username == "测试用户":
    print("登录用户是：{}".format(username))
else:
    print("用例执行失败！")

driver.find_element_by_xpath('//span[text()="零售出库"]').click()
time.sleep(2)
# 寻找到了子页面，进行iframe的切换
id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id") # 获取元素的属性值
frameid = id + "-frame"
print(frameid)
# driver.switch_to.frame(frameid)  # 通过id切换iframe子页面
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(frameid))) # 通过元素定位 切换iframe

#下面的代码都在子页面的
driver.find_element_by_id("searchNumber").send_keys("448")
driver.find_element_by_id("searchBtn").click()
time.sleep(1)  # 隐式等待+ 强制等待
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text # 获取文本
if "448" in num:
    print("搜索正确！")
else:
    print("搜索失败！")

"面试题：你们公司这个自动化框架的目录结构是什么样子？"

