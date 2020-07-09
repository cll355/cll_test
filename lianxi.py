# 练习1
#通过代码获取两段内容，并且计算他们的长度
a = input("请输入：")
b = input("请输入：")
print(len(a+b))


#练习2
#获取用户的个人信息，并且存储到字典中
#个人信息包括，name age、 sex
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


#练习3
#  现有11个学生的成绩，
# 这11个学生姓名是"张三","李四","王二麻","程玲玲","梅浩","程晨","程志威","程红","鲁班","树是","呃呃"
#并且名字和分数需要对应上
# 大于60的 和小于60的分开存放

highscore={}
lowscore={}
name=["张三","李四","王二麻","程玲玲","梅浩","程晨","程志威","程红","鲁班","树是","呃呃"]
a=0
while a < len(name):
    score = int(input("请输入"+name[a]+"的成绩:"))
    if score >= 60:
        highscore[name[a]]=score
    else:
        lowscore[name[a]]=score
    a=a+1
print("大于60：",highscore)  
print("小于60：",lowscore)   

highscore={}
lowscore={}
name=["张三","李四","王二麻","程玲玲","梅浩","程晨","程志威","程红","鲁班","树是","呃呃"]
for i in name:
    score = int(input("请输入"+i+"的成绩:"))
    if score >= 60:
        highscore[i]=score
    else:
        lowscore[i]=score
print("大于60：",highscore)  
print("小于60：",lowscore)   

# 练习4
# 打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i, "*" ,j, "=" ,i*j,end="  ")  #end="  "是实现空格
    print()  # 换行


# 练习5
# 通过print打印，模拟一个红绿灯功能，注意：红灯30次，路灯35次，黄灯3次
while True:        
    light = {"红灯":30,"绿地":35,"黄灯":3}
    for i in light:
        for j in range(light[i]):
            print(i,"距离结束还有",light[i]-j,"秒")


#练习6
#用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写字母开头
#并存储到字典中;
username = input("请输入账号：")
password = input("请输入密码：")
a={}
if(len(username)>=5 and len(username)<=10):
    if(username[0] in "abcdefghijklmnopqrstuvwxvz"):
        if(len(password)<=12 and len(password) >=6):
            print("注册成功")
            a["username"]=username
            a["password"]=password
            print(a)
    else:
        print("首位字母请输入小写")
else:
    print("请输入5-8位的账号")

#练习6
#定义一个方法判断用户输入的账号密码是否符合规范，用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写字母开头
#并存储到字典中;
# 这个代码出错
def guifan(username,password):
    if len(username)>=5 and len(username)<=8:
        if len(password)>=6 and len(password)<=12:
            if username[0] in "abcdefghijklmnopqrstuvwxyz":
            else:
                print("账号要以小写字母开头")
        else:
            print("密码位数不对")
    else:
        print("请输入正确位数的账号")
print(username,password)












