"""
============================
Project: python_class
Author:柠檬班-Tricy
Time:2021/8/17 14:53
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
'''
1、在pycharm的控制台里输入以下内容，并且以如下格式输出到控制台

2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python' -- 取多个值= 切片 [0:6]
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？--in 
3）替换python为 “lemon”. -- replace
4) 找到aaa的起始位置 -- 索引
'''
# name = input("请输入你的名字：")
# # age = input("请输入你的年龄：")
# # gender = input("请输入你的性别：")
# # print('''********************
# # 姓名：{}
# # 年龄：{}
# # 性别：{}
# # ********************'''.format(name,age,gender))
# str1 = 'python hello aaa 123123aabb'
# print(str1[0:6:1])
# print("o a" in str1)
# print("he" in str1)
# print(str1.replace("python","lemon"))
# print(str1.find("aaa"))
# print(str1.index("aaa"))

'''
接口自动化测试--项目：
安装第三方库:  --别人写好的，封装，可以直接拿来使用的
两步操作： pip -- 安装第三方库的工具
1、安装： pip install requests / pycharm安装
2、导入：import requests   ===  Python文件里
发送接口请求： 
注意： requests（除了url之外）所有的参数都必须用字典的格式传输
'''
import requests  # 导入库
import pprint # prety-print
import jsonpath
#注册
url_wuye = "http://47.115.15.198:7001/smarthome/user/register"   # 定义变量接受 接口地址
test_date = {
  "phone": "15215541772",
  "pwd": "lemon123",
  "rePwd":"lemon123",
  "userName":"83期唐僧",
  "verificationCode":"lemon"}  #定义参数
# head = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}  # 定义请求头部
# response = requests.post(url=url_wuye,json=test_date,headers=head)  # 发送接口请求的 --响应消息
# print(response.json())  # 得到json 格式响应体

#登录
# url_login = "http://47.115.15.198:7001/smarthome/user/login"
# login_date = {"pwd": "lemon123","userName": "83期唐僧"}
# head_login = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
# res_login = requests.post(url=url_login,json=login_date,headers=head_login)
# pprint.pprint(res_login.json())

# 登录完后取值-- id token
# id = res_login.json().get("data").get("id")  # 通过字典的取值  提取 id
# token = res_login.json().get("data").get("token_info").get("token")
# id = jsonpath.jsonpath(res_login.json(),"$..id")[0]
# token = jsonpath.jsonpath(res_login.json(),"$..token")[0]
# pprint.pprint(id)
# pprint.pprint(token)

# 完善信息接口
url_info = "http://47.115.15.198:7001/smarthome/merchant/complete"
data_info = {
  "address": "湖南省长沙市岳麓区xx街道12345678901234567",
  "establishDate": "2021-04-02",
  "legalPerson": "韩",
  "licenseCode": "xh430646464sdfa",
  "licenseUrl": "http://127.0.0.1/smarthome/aaa.jpg",
  "merchantName": "青海文梅科技有限公司1234567890",
  "merchantType": 2,
  "registerAuthority": "城中区派出所123456789012345678901234",
  "tel": "18888888888",
  "userId": id,
  "validityDate": "2033-05-02"
}
# head_info = {"X-Lemonban-Media-Type":"lemonban.v2",
#  "Content-Type":"application/json",
#              "Authorization":"Bearer "+token}
# result = requests.put(url=url_info,json=data_info,headers=head_info)
# pprint.pprint(result.json())

"""
扩展内容： requests 发送百度的请求
响应不对：
1、长度和内容不对 --大型网站，反爬机制-爬虫 == 假装自己是个浏览器发送请求 
2、乱码 -- 中文编码
"""
# url_baidu = "https://www.baidu.com/"
# head = {"User-Agent":
# 	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
# resp = requests.get(url=url_baidu,headers=head)  # 带上头部发送请求
# # print(resp.text)  # 文本结果 --自动解码 --80%
# print(resp.content.decode("utf8")) # 手动指定解码方式

# https://www.baidu.com/s?wd=柠檬班  --带参数的请求
url_baidu = "https://www.baidu.com/s"
head = {"User-Agent":
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
data_baidu ={"wd":"柠檬班"}
resp = requests.get(url=url_baidu,headers=head,params=data_baidu)  # 带上头部发送请求
# print(resp.text)  # 文本结果 --自动解码 --80%
print(resp.content.decode("utf8")) # 手动指定解码方式




