'''
print("你好！")   # 字符串
print(2333)  # 整数
print(2.33) #小数
print(True) #布尔值 true false
print(())   #元组
print([])   # 数组
print({})   #字典

 多行注释
 还漏顶顶顶顶顶顶顶

print("哈哈",23333,"aaa")  
print("黑皮"+"坏坏")    # 字符串的拼接
print("哈哈"*20)    # 倍数
print(((1+2)*100-220)%2)
print(2>3)
print(3<4)


变量
赋值

a = "张三"   #把张三的这个值复制给a这个变量   变量必须为小写字母
print(a)


a = input("请输入：")
print("input获取的内容：",a)

print(type("aaa"))
print(type(111))
print(type(1.11))
print(type(True))
print(type(()))
print(type([]))
print(type({}))

将字符串转换为整型
a = int("123")
print(type(a))
'''
# a = float(input("第一个数："))
# b = float(input("第二个数："))
# print("两数之和：",a+b)

# 字符串长度
# a ='asadasdsfdfsdggdfgfd  '
# b ='哈哈'
# print(len(a))
# print(len(b))

# a = input("请输入一个数：")
# b = input("请输入另一个数：")
# print("两数相加之和：",a+b)
# print(len(a+b))

# a='adsadasfasd'
# print(type(a))

# 元组  下标：从0开始编号
# a = (1,3,42,21,"梅浩","梅浩","梅浩","梅浩程玲玲","hh")
# print(a[0:4])   #左闭右开
# print(a[4:9])

# print(a[5])
# print(a.count("梅浩"))
# print(a.index("hh"))


# 二维元组
# a = (1,3,42,21,"梅浩","梅浩","梅浩","梅浩程玲玲","hh")
# b = (a,"哈哈","xixixi,jjj")
# print(b[0][3])


# a = [11,13,34,"hailou","程玲玲","梅浩"]
# print(a.index(13))
# print(a.index("梅浩"))
# print(a.count("hailou"))
# a.append("append在末尾")
# print(a)
# a.insert(4,17)
# print(a)
# a.pop(1)
# print(a)
# b=a.pop(4)
# c=a.pop(2)
# print(b+c)
# b = ["aa",12131,"yyy"]
# a.extend(b)
# print(a+b)  #这种方法也可实现
# a.remove("hailou")
# print(a)
# a = {"name": "cll","age":18,"height":"153cm"}
#print(a)
# 取值
#print(a["name"])
#print(a["age"])
#修改
#a["name"] = "lisi"
#print(a)
#增加
#a["zengjia"] = "hailou"
#print(a)
# b=a.get("name")
# print(b)
# b=a.update(name="aaa")
# print(a)
# b = a.pop("name")
# print(a)

# 数组与字典的删除
# del a["name"]
# print(a)
# del a[0]
# print(a)

name = input("请输入姓名：")
age = input("请输入年龄：")
sex =input("请输入性别:")
a={}
# a["name"] = name
# a["age"]=age
# a["sex"]=sex
a.update(name=name)
a.update(age=age)
a.update(sex=sex)
print(a)