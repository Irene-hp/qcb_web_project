# Python列表 + 字典 + 控制流

'''
常用数据类型：列表（list） 元组 字典 集合

列表（list）：[] ---重要重要！！！
1、元素可以是任意的数据类型：int float bool str list tuple...
2、取值：索引取值--类比字符串
取多个值：切片--[开始：结束：步长] === 取头不取尾
扩展：列表的嵌套取值
3、列表的元素是可以被改变的！ --增加，修改，删除
4、列表的元素是可以重复的 --统计个数 count()
5、len() ---统计元素个数
'''

# 列表
list1 = [14,3.14159,'小美眉','小富婆',[1,3,5,7,9]]
#print((type(list1)))
print(list1[3]) # 取值
print(list1[2:4]) # 取多个值
print(list1[4][3]) # 列表的嵌套取值

# 增加
list1.append('大富翁') # 默认追加元素到列表的末尾 --P1
list1.insert(3,'君君') # 指定位置进行元素插入 --P2
list1.extend(['喵喵','一搏','中中']) # 相当于两个列表的合并 --P3
print(list1)

# 删除
list1.pop(0) # 默认删除最后一个元素，也可以指定位置（索引）进行删除
list1.remove('小美眉') # 指定元素本身进行删除
#list1.clear() # 清除所有元素 --了解
print(list1)

# 修改 --先取值，再重新赋值
list1[0] = '钱钱'
print(list1)

list1.append('小富婆')
print(list1)
print(list1.count('小富婆')) # 统计列表中'小富婆'的个数
print(len(list1)) # 统计列表中元素的个数

'''
元组 tuple：() --P2
1、元素可以是任意的数据类型：int float bool str list tuple...
2、取值：索引取值--类比字符串
取多个值：切片--[开始：结束：步长] === 取头不取尾
扩展：列表的嵌套取值
3、元组的元素是不可以被改变的！
4、元组的元素是可以重复的 --统计个数 count()
5、len() ---统计元素个数
6、list tuple 间的转化 ---扩展
'''

tuple1 = ('钱钱','小美眉','小富婆','大富翁','二哈','一搏','中中','小富婆')
print(len(tuple1))
print(tuple1.count('小富婆'))
print(tuple1)

list2 = list(tuple1) # 把元组转化为列表
list2[-2] = '富婆'  # 修改
print(list2)
tuple2 = tuple(list2)
print(tuple2)

'''
字典 dict {}  --P1 重要重要！！！
1、元素：key：value （键值对）
2、场景：存储数据属性：人--身高 名字 体重
key：1）不能是可改变的数据类型（list，dict）---通常为字符串
     2）不能重复，唯一的
value：可以是任意数据类型 --可以被改变 ==增删改
3、字典是没有顺序的！！ --不能用索引取值 --- 取值：通过key取value
4、len() -- 长度
'''

dict1 = {'name':'小富婆','height':'155','weight':'90'}
print(dict1['name']) # 通过key取value
print(dict1.get('weight'))  # 通过key取value
# 用内置函数dict()创建一个字典
dict2 = dict(name='小富婆',age=18,gender='famale')
print(dict2)
# 修改
dict1['height'] = '165' # key存在，修改对应key的value
print(dict1)
# 增加
dict1['age'] = 18 # 若key不存在，则添加键值对
print(dict1)
dict1.update({'city':'深圳','hobby':'学习'}) # 增加多个值，相当于字典的合并
print(dict1)
# 删除
dict1.pop('height') # 指定key删除对应的键值对
print(dict1)
#del(dict1)  # 删除整个字典 包括所有key和value--对象不存在了
# print(dict1)

'''
集合：set {}, 元素单个 --了解
1、集合是没有顺序的
2、元素不可以重复 --使用场景：去重
'''
list3 = [11,22,33,44,55,11,22] # 去重
print(list3)
set1 = set(list3)  # set() --将list3 转化为集合
print(set1)
list3 = list(set1)  # list() --将set1 转化为列表
print(list3)

'''
控制流：代码的执行顺序 --从上至下依次执行：判断 循环 可以控制代码执行顺序
判断：if 语法
if 条件： ---成立（bool值True） ---冒号：缩进（4个空格==tab键）
    子代码（执行语言）
elif 条件：---成立
    执行语句（子代码）
。。。（elif可以没有，也可以有多个）
else：（后面没有条件--兜底） --可以没有
    执行语句
'''

money = int(input('please enter your leave_amount:'))
if money >= 800:
    print('在深圳买房！')
elif money >= 500:
    print('在广州买房！')
elif money >= 200:
    print('在佛山买房！')
elif money >= 100:
    print('在韶关买房！')
elif money >= 50:
    print('买车！')
else:
    print('努力学习赚钱')

# 作业
# 1、a=[1,2,'6','summer'］请用成员运算符判断i是否在这个列表里面
a=[1,2,'6','summer']
#print('i' in a)
if 'i' in a:
    print('i是成员')
else:
    print('i不是成员')

# 2、dict_1={"class_id":45，'num'：20｝请判断班级上课人数是否大于5（注：num表示课堂人数。如果大于5，输出人数）
dict_1 = {"class_id":45,'num':20}
#num = dict_1.get('num')
if dict_1['num'] > 5:
    print('班上人数是：{}'.format(dict_1['num']))
else:
    print('班上人数不足5人')

# 3、list1＝［'方方土', '七木','荷花鱼','kingo','Amiee','焕蓝']列表当中的每一个值包含：姓名、性别、年龄、城市,以字典的形式表达。
# 并且把字典都存在新的 list中，最后打印最终的列表。
# 方法1：手动扩充--字典-存放在列表里面；
# 方法2：自动--dict（）
name = ['方方土','七木','荷花鱼','kingo','Amiee']
gender = ['Female','Male','Female','Male','Female']
age = [19,21,23,25,27]
city = ['深圳','广州','韶关','东莞','佛山']
list_2 = [] # 空列表，用来存新字典
for i in range(5):
    dict1 = dict(Name=name[i],Gender=gender[i],Age=age[i],City=city[i])
    list_2.append(dict1)  # 在空字典里追加元素
print(list_2)