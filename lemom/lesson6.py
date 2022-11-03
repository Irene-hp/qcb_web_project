import time
def open_url(url,driver):  # 打开网页
    driver.get(url)
    driver.maximize_window()

def login_page(username,password,driver):   # 形参  -参数化 --提高代码复用率
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('btnSubmit').click()

def search_key(url,username,password,s_key,driver):
    open_url(url,driver)  # 调用函数
    login_page(username,password,driver)  # 调用函数
    page_text = driver.find_element_by_xpath("//p[text()='测试用户']").text
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
    F_id = P_id + '-frame'
    driver.switch_to.frame(F_id)
    driver.find_element_by_id('searchNumber').send_keys(s_key)
    driver.find_element_by_xpath("//span[@class='l-btn-left']").click()
    time.sleep(2)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']//div").text
    return num





