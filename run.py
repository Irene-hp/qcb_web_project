from lemom import lesson6  # 导入函数文件
from test_data import test_data  # 导入测试数据文件
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 调用函数 --1、先将参数取出  2、传参到函数调用里
url = test_data.url['url']  # 取值 url
user = test_data.login_page['username']  # 取值 登录用户名
pwd = test_data.login_page['password']  # 取值 登录的密码
s_key = test_data.s_key['s_key']   # 取值 搜索关键字
print(url,user,pwd,s_key)
# 函数的调用 传参
# 给函数定义了一个返回值-- 调用的时候用一个变量接收返回值：
result = lesson6.search_key(url=url,username=user,password=pwd,s_key=s_key,driver=driver)
if s_key in result:
    print("单据编号是：{}".format(result))
else:
    print('测试用例不通过！')



