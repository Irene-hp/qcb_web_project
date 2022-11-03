'''
web自动化：
Python -----> 浏览器驱动（准备） ----->  Chrome
selenium: Python的工具，三个部分 --> 了解
1）IDE：录制脚本--用得少
2）webdriver：库--提供对网页的各种操作+结合语言使用 -- Python Java --重点
3）grid：分布式 --用得少

基础知识：web项目= HTML+CSS+Javascript  --扩展 了解
html：标签语言 <标签名>值</标签名> == 呈现页面内容
CSS：页面布局设置，字体颜色，字体大小 样式
JS：依据不同 渲染效果
'''

import time
from selenium import webdriver  # 从selenium库中导入webdriver库
driver = webdriver.Chrome()   # 选择chrome这个浏览器，初始化driver == 可与浏览器进行沟通 建立会话 session
driver.implicitly_wait(10) # 隐式等待，默认等待10s == 最多等待10s，提前出现了就不继续等待了
# 验证打开一个网址
driver.get('http://erp.lemfix.com/login.html')
driver.maximize_window() # 浏览器界面最大化
time.sleep(3)  # 等待 默认时间为秒
driver.get('https://registry.npmmirror.com/binary.html?path=chromedriver/106.0.5249.21/')  # 打开新页面
driver.back()  # 退回上一页面
driver.forward()  # 跳转到下一页面
driver.refresh()  # 刷新页面
# 退出
driver.quit()  # 关闭驱动 session关闭
driver.close()  # 关闭当前窗口，不会退出会话

'''
以上为浏览器常规操作，非常规操作如何实现？ == 元素定位
元素的特征：根据页面设计规则，有些特征是唯一的 == 开发遵循这个规则的前提下
id：类比身份证号 == 仅限于当前页面 username password
注意：id不是固定的话，不能使用来定位

XPath：
1、绝对路径：/html/body/div[1]/div/div[2]/div[1]/input  --根节点，顺序性、继承关系，若代码改动则失效
2、相对路径：只靠自己的特征定位 表达方式：//标签名[@属性名=属性值] --//input[@id='username']  
3、层级定位：//标签名[@属性名=属性值]//标签名[@属性名=属性值] -- //div[@class='login-logo']//b
4、文本定位：//标签名[text()=文本值]  -- //b[text()='柠檬ERP']
5、包含属性值：//标签名[contains(@属性名/text(),属性值)] -- //b[contains(text(),'柠檬')]  //div[contains(@class,'pull-left info')]

对页面进行相应的操作：
1、点击：click()
2、传值 send_keys()
3、获取页面文本：test
4、获取属性：get_attribute()

但凡是切换了页面，页面没有加载完，元素不显示 == 最好加个等待
三种等待方式：
1、强制等待：time.sleep() == 没有完成等待时间，不往下执行
2、智能等待：
  隐式等待：implicitly_wait(),可以设置一个等待时间，在这个等待时间还没结素之前元素找到了，不继续等待，继续执行下面的代码； --灵活
  注意：一个session里只执行一次
  显示等待：expecte_condition  == 指定某个指令等待
  
八大元素定位方式
三个等待
三种操作
'''
# 通过id定位
# 验证输入正确的用户名和密码能正常登录
driver.find_element_by_id('username').send_keys('test123') # 找到有username这个id的元素--输入内容
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('btnSubmit').click()  # 通过id找到登录按钮并点击

# XPath定位
# driver.find_element_by_xpath("//input[@id='username']").send_keys('test123') # 通过相对路径定位元素
# login_text = driver.find_element_by_xpath("//div[@class='login-logo']//b").text # 找到这个元素的位置后获取页面标题 层级定位
# login_text1 = driver.find_element_by_xpath("//b[text()='柠檬ERP']").text  # 文本定位

# 验证页面标题
page_text = driver.find_element_by_xpath("//b[contains(text(),'柠檬')]").text  # 包含属性值定位
page_title = driver.title  # 获取页面的标题
print('这个页面的标题是：{}'.format(page_title))
if page_text == '柠檬ERP':
    print('这个页面的标题是：{}'.format(page_text))
else:
    print('这条测试用例未通过')

# 验证正常登录，登录成功
# time.sleep()
log_user = driver.find_element_by_xpath("//p[text() = '测试用户']").text
#log_user = driver.find_element_by_xpath("//div[contains(@class,'pull-left info')]").text  # 获取登录用户名
print(log_user)

# 点击零售出库
#driver.find_element_by_xpath("//a[@title="零售出库"]//span").click()
driver.find_element_by_xpath("//span[text()='零售出库']").click()

'''
1、识别是否有子页面的方式：页面层级路径里出现iframe：需要去切换路径，才可以进行元素的定位
2、怎么去切换：
1）找到这个iframe元素，切换

切换有三种方式：
1、通过id来切换
2、通过xpath定位元素来切换iframe路径
3、iframe下标：从0开始 html-页面=0，第一个子html为-1
'''
# 验证输入单据编号并进行搜索
# 由于这个iframe的id是动态的，需要在前面找到规律（即这个动态id是随前面的id变化而变化），然后通过找到前面这个元素--获取id属性
P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
F_id = P_id + '-frame'  # 通过获取前面id的属性，进行iframe动态id的拼接
# 通过id进行iframe路径的切换
driver.switch_to.frame(F_id)
driver.find_element_by_id('searchNumber').send_keys('258')  # 传值
# 通过xpath定位元素来切换iframe路径
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="{}"]'.format(F_id)))
# driver.find_element_by_id('searchNumber').send_keys('314')
# 通过iframe下标来来切换路径
# driver.switch_to.frame(1)
# driver.find_element_by_id('searchNumber').send_keys('314')
# 点击搜索按钮
driver.find_element_by_xpath('//span[@class="l-btn-left"]').click()
time.sleep(2)
# 找到单据编号
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]//div').text
if '258' in num:
    print("单据编号正确！")
else:
    print('测试用例不通过')

