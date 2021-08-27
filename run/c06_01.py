#!/user/bin/env python
# -*- coding:utf-8 -*-
# from  selenium import webdriver
# import selenium.webdriver.common.keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# ii = (3,1,4)


# driver = webdriver.Chrome()
def open_web(driver, webname):
    # driver = webdriver.Chrome()  # 选择Chrome浏览器 --跟浏览器建立会话--->启动浏览器
    driver.maximize_window()
    driver.get(webname)


def send_key(username, password, driver):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()


def findChuKu(driver):
    driver.find_element_by_xpath("//span[contains(text(),\"零售出库\")]").click()

    id = driver.find_element_by_xpath("//div[text()=\"零售出库\"]//..").get_attribute("id")
    # 找到iframe所在div块的id
    frameid = id + "-frame"
    # 拼接id
    driver.switch_to.frame(frameid)
    # 通过id切换iframe

    # driver.switch_to_frame(1)通过序号


def sendM(driver,number = int,str_ = str):
    # print("number=",number,"type=",type(number))
    # driver.implicitly_wait(10)  # 等待页面加载
    driver.find_element_by_xpath("//input[@name=\"searchNumber\"]").send_keys(number)
    driver.find_element_by_xpath("//input[@name=\"searchNumber\"]").send_keys(str_)
    driver.find_element_by_xpath("//input[@name=\"searchNumber\"]").clear()
    time.sleep(2)
    isE = True
    text = driver.find_element_by_xpath("//table[@class=\"datagrid-btable\"]//tbody").text
    if text == "" or text == None:
        isE = False
    return isE


def send_result(driver,ii=list,str_ = str):
    time.sleep(3)
    for i in ii:
        print(i)
        if (sendM(driver,i,str_) == False):
            print("无法查询到id为{}的出库信息".format(i))
        else:
            print("查询成功")
    driver.close()
# open_web(driver, "http://erp.lemfix.com/login.html")  # 打开网页
# send_key("test123", "123456", driver)  # 输入信息登录
# driver.implicitly_wait(10)  # 等待页面加载
# findChuKu(driver)  # 点击出库信息，跳转至其内嵌页面
# ii = (3,1,4)
# send_result(driver, ii ,Keys)  # 循环输入搜索id，控制台输出结果
# open_web("http://erp.lemfix.com/login.html")#打开网页
# send_key("test123","123456")#输入信息登录
# driver.implicitly_wait(10)#等待页面加载
# findChuKu()#点击出库信息，跳转至其内嵌页面
# ii = {3,4,1}
# send_result(ii)#循环输入搜索id，控制台输出结果
