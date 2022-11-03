# lesson4 for循环+函数

'''
for循环：遍历 数据对象里的所有元素：str，list，tuple，dict
for 变量名 in 数据对象
    子代码（循环体）
循环次数由元素个数决定！
中断：break continue

range() --内置函数：生成一个整数序列：1,2,3,4,5
跟 for 循环一起使用：start--开始 ==默认值为0，stop--结束，step--步长 ==取头不取尾
'''

count = 0 # 计数器
list_1 = ['方方土','七木','荷花鱼','kingo','Amiee','焕蓝']
for name in list_1:
    if name == '荷花鱼':
        # break     # 跳出整个循环
        continue    # 跳出本次循环
    print(name)
    print('*' * 18)
    count += 1
print(count)
print(len(list_1))

for i in range(1,10,2):
    print(i)

'''
函数：封装成函数，调用 --- 提高代码的复用率，提高执行效率
语法：
def 函数名()
    子代码（函数体）--实现功能
注意：函数只定义了 没有调用是不会执行的：如何调用？ --写函数名

函数里不固定的数据 -- 定义成函数的参数--括号里
1、形参--函数定义的时候定义的
2、实参：调用函数时传入的数据

参数定义的类型：
1、必备参数：定义了就必须要传入的参数--不传会报错
2、默认参数（缺省参数）：可以定义的时候赋一个默认值 --调用时可传，可不传值，若传则替换掉默认值
注意：默认参数必须在必备参数后面！！！
3、不定长参数(*args)：等前面的必备参数和默认参数都接收完，剩下的参数都传给不定长参数接收
*args：接收不定数量，个数的参数 --可以不传，也可以传入（1个，多个）==元组接收 --位置传参
**kwargs：字典接收，传参的方式--关键字传参方法

传参的方式类型：（实参）
1、位置传参：按照位置传入参数
2、关键字传参：指定参数名来进行传参，不关心顺序 --可靠
3、混合传参：位置和关键字混合，注意：关键字传参必须跟在位置传参后面！
'''

def good_job():  # 定义函数名
    base_salary = 7000
    bouns = 3000
    allowance = 800
    sum_sal = base_salary + bouns + allowance
    print('这个工作的薪酬总和为：{}'.format(sum_sal))
good_job()  # 用函数名进行函数的调用，函数才会被执行

def good_job(base_salary,bouns,allowance,*args,**kwargs):  # 定义函数名 == 函数的参数--形参--变量替代
    sum_sal = base_salary + bouns + allowance  # 实现功能
    print('base_salary的值：{}'.format(base_salary))
    print('bouns的值：{}'.format(bouns))
    print('allowance的值：{}'.format(allowance))
    print('args的值：{}'.format(args))
    print('kwargs的值：{}'.format(kwargs))
    for i in args:  # 遍历
        sum_sal += i
    for j in kwargs:
        kwargs.get(j) # 字典的取值--通过key取value
        sum_sal += kwargs[j]
    print('这个工作的薪酬总和为：{}'.format(sum_sal))
good_job(8000,2000,500,100,300,500,a=500,b=500,c=800)  # 用函数名进行函数的调用，函数才会被执行 --实参

'''
函数有进有出：进--参数，出--返回值
1、返回值:函数给出的数据，以做后续操作 --- 调用函数的时候，可以获取这个返回值 ---return
2、调用-- 变量接受返回值
3、如果没有返回值-- None，可以有return：可以有多个--元组保存
4、注意：返回值写在函数的最后一行--标志着函数的结束
'''
def good_job(base_salary,bouns,allowance,*args,**kwargs):  # 定义函数名 == 函数的参数--形参--变量替代
    sum_sal = base_salary + bouns + allowance  # 实现功能
    for i in args:
        sum_sal += i
    for j in kwargs:
        kwargs.get(j) # 字典的取值--通过key取value
        sum_sal += kwargs[j]
    return sum_sal  # 可以有多个返回值
result = good_job(8000,2000,500)  # 用函数名进行函数的调用，函数才会被执行 --实参
print(result)

# 作业
# 1．把字符串转成列表--list()
str1 = ('霉霉','君君','小海','呜呜')
print(str1)
list1 = list(str1)
print(list1)

# 2．完成任意整数序列的相加--生成一个整数序列，里面全是数字，求里面所有数字的和
def add_fun(num):
    sum = 0
    for i in range(num):
        sum += i
    print(sum)
add_fun(10)

# 3．定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。--if判断嵌套
def length_function(object):
    #if type(object) == list or type(object) == dict or type(object) == str:
    if isinstance(object,list) or isinstance(object,dict) or isinstance(object,str):
        length = len(object)
        if length > 5:
            print('True')
        else:
            print('False')
    else:
        print('数据类型不能计算长度')
length_function([1,2,3,4,5,6])

#length_function({'name':'久久','age': 18,'gender':'female','city':'深圳','birthday':'9.15','hobby':'cook'})

