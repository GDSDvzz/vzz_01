#!/user/bin/env python
# -*- coding:utf-8 -*-

from  selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from InClass.run import  c06_01

driver = webdriver.Chrome()
ii = (3,1,4)

print(type(Keys.ENTER))
c06_01.open_web(driver, "http://erp.lemfix.com/login.html")#打开网页
c06_01.send_key( "test123", "123456",driver)#输入信息登录
driver.implicitly_wait(10)#等待页面加载
c06_01.findChuKu(driver)#点击出库信息，跳转至其内嵌页面
c06_01.send_result(driver,ii,Keys.ENTER)#循环输入搜索id，控制台输出结果
