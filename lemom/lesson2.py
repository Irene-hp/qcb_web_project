# lesson2 Python基础语法

'''
变量：存储数据的 == 存储东西
数据类型：int float bool str
变量名：标识符 ---标识符命名规则1，2，3，4，5，见名知意，6，变量名一定要先声明（定义并赋值），在调用，否则报错
'''

'''
字符串(str)的操作：
1. 取值：元素 位置--索引，从0开始,依次加1
2. 取多个值：切片--[开始：结束：步长] === 取头不取尾
开始头--省略 == 默认从0开始
结束 -- 省略 == 默认末尾结束
步长 -- 省略 == 默认为1
3. 负数：从右边开始取 -1==最后一个
4. 元素个数：len()--内置函数：统计元素个数（长度）
5. 替换字符串里的元素：replace()
6. 索引index() --如果元素没有找到会报错
find() --如果元素没有找到不会报错，返回-1
count() --计算某元素出现的次数
'''
info = '黄佩最美！'
print(info)

str1 = "hello world!"  # 定义一个字符串变量
print(str1[6])  # 取值
print(str1[0:8:3]) # 取多个值
print(str1[-2])  # 从有往左取值
print(len(str1))  # 统计元素个数
print(str1[0:len(str1):3]) #
str1 = str1.replace("world","huanghuang") # 替换字符串元素
print(str1)
print(str1.index("l"))  # 检索字母l
print(str1.find("h"))  # 检索字母h
print(str1.count('u'))  #计算u出现次数

'''
格式化输出
1、 .format()
1)占位符：{} --用在需要传变量的地方 .format()
2).format() 可以默认按顺序传入变量；也可以指定位置传入变量 == 注意：默认和指定不能混合使用
2、 %s--字符串 ==匹配所有  %d--整数  %f--小数  ---了解
'''
name = 'irene'
age = 18
hobby = '吃饭'
# 默认顺序传入变量
print('''-----{}----
name:{}
age:{}
hobby:{}
'''.format(name,name,age,hobby))
# 指定位置传入变量
print('''-----{1}----
name:{1}
age:{0}
hobby:{3}
'''.format(age,name,age,hobby))

# %占位符
name = 'irene'
age = 18
hobby = '吃饭'
print('''-----%s----
name:%s
age:%s
hobby:%s
'''%(name,name,age,hobby))


'''
Python运算符
1、算数运算符：+ - * / % **
2、赋值运算符：= += -= ：方向性--右边赋值给左边
3、比较运算符： < <= > >= == != ---运算结果为布尔值True False
4、逻辑运算符：与-and==真真为真  或-or==假假为假  非-not  ---运算结果为布尔值True False
5、成员运算符：in, not in ---运算结果为布尔值True False
'''

# 1、算数运算符：+ - * / % **
print(10 + 50) # 两个数字的相加
print('Love'+'Study')  # 两个字符串拼接
# int --> str：str()--强制字符串的转化，int(), float(), bool()
print(str(123)+'abc')
print(30 - 1) # 两个数字的相减
print(3 * 5) # 两个数字的相乘
print('I Love You' * 5) # 字符串重复输出 * 次数
print(10 / 2) # 结果浮点数

# 2、赋值运算符：= += -= ：方向性--右边赋值给左边
a = 10
a += 10 # == a = a + 10
a -= 5 # == a = a - 5
print(a)

# 3、比较运算符： < <= > >= == !=
print(3<2)
print('登录成功' == '登录成功')

# 4、逻辑运算符：与-and==真真为真  或-or==假假为假  非-not
print(3 < 5 and 2 < 8)
print(not 2 < 1)

# 5、成员运算符：in, not in
str2 = 'chifan'
print('5' in str2)

# input()内置函数--在控制台输入值并赋值给num这个变量--输入的值数据类型为字符串str
num = input("请输入您的数字：")
print(num)


# 作业
# 1. 在pycharm的控制台里输入以下内容，并且以如下格式输出粗到控制台：
name1 = input('请输入姓名：')
age1 = input('请输入年龄：')
sex = input('请输入性别：')
print('*' * 18) # 字符串重复输出 * 次数
print('''姓名：{0}
性别：{1}
年龄: {2}'''.format(name1,age1,sex))  # .format()格式化输出
print('*' * 18)

# 2. 现在有字符串：str1 = 'python hello aaa 23123aabb'
# 1) 请取出并打印字符串中的'python'
str3 = 'python hello aaa 23123aabb'
print(str3[0:6:1]) # 切片

# 2) 请判断 'o a' 'he' 'ab' 是否是改字符串中的成员
# 成员运算符
print('o a' in str3)
print('he' in str3)
print('ab' in str3)

# 3) 替换python为'lemon'
str3 = str3.replace('python','lemon')
print(str3)

# 4) 找到aaa的起始位置
print(str3.index('aaa'))
print(str3.find('aaa'))

