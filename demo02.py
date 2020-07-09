# a = int(input("请输入一个数："))
# if a == 23:
#     print("这是23的结果")

# == 判断是否相等
 #  = 赋值 
# a=int(input("请输入一个数："))
# if a==1:
#    print("hahahaha")
# elif a==2:
#     print("xixixixixi")
# else:
#     print("你好")      

# a ="你bu好"
# if a in "你好，哈哈哈":
#     print("ok")
# else:
#     print("not ok")

# a = input("请输入：")
# if a == "":
#     print("不能为空")
#     exit()
# if a in "01234567":
#     a=int(a)
# else:
#     print("请输入正确得格式")
#     exit()
# if a > 5:
#     print("好")
# else:
#     print("不好")

# a = 1
# if type(a) is int:
#     print("这是int型")
# elif type(a) is str:
#     print("这是字符串")
# else:
#     print("其他")

#  练习

# highscore={}
# lowscore={}
# name=["张三","李四","王二麻","程玲玲","梅浩","程晨","程志威","程红","鲁班","树是","呃呃"]
# a=0
# while a < len(name):
#     score = int(input("请输入"+name[a]+"的成绩:"))
#     if score >= 60:
#         highscore[name[a]]=score
#     else:
#         lowscore[name[a]]=score
#     a=a+1
# print("大于60：",highscore)  
# print("小于60：",lowscore)   



#a = "梅浩是黑皮"
# a=["张三","李四","王二麻","程玲玲","梅浩","程晨","程志威","程红","鲁班","树是","呃呃"]
# for i in a:
#     print(i)

# for i in range(10):
#     print(i)

#自动生成数列
#a = list(range(0,18,2))  # 2指的是0-18（左闭右开） 中的步长
#print(a)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i, "*" ,j, "=" ,i*j,end="  ")
#     print()


# for i in range(9):
#     if(i == 5):
#         continue
#     print(i)


# for i in range(9):
#     if(i == 5):
#         break
#     print(i)

# def sum(a,b):
#     '''
#       实现两个数的加法
#     '''
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else:
#         print("数据类型输入错误")
# sum(1,2)

# sum(23,354)

'''
①
def sum(a,b):
  
      实现两个数的加法
    
    if type(a) is int and type(b) is int:
        return a+b
    else:
        return "数据类型输入错误"
②
# a=sum(12,20)
# b=a+8
# print(b)
②
print(sum(1,2))
②
try:        
    print(sum(1+jhh))
except:
    print("上面代码错误")
'''    

# def sum(a,b):
#     '''
#       实现两个数的加法
#     '''
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         return "数据类型输入错误"

# try:        
#     print(sum(1+jhh))
# except Exception as e:
#     print("上面代码错误",e)