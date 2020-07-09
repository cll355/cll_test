# a = input("请输入姓名：")
# b = input("请输入年龄：")
# try:
#     if int(b) >= 18:
#         print(a,"成年了")
#     else:
#             print(a,"未成年")    
# except:
#     print("年龄的格式输入错误")

# import time
# import random
# for i in range(10):
#     time.sleep(1)
#     print(i)
# a = random.randint(1,1000)
# print(a)

class BoyFriend():
    def __init__(self,sex,height,weight):
        self.sex = sex
        self.height= height
        self.weight= weight

    def caiyi(self):
        print("性别为"+self.sex+"身高为"+self.height+"体重为"+self.weight+"的男朋友")
        print("会放屁")
    def chuyi(self):
        print("样样精通")

# 类的实例化
# mh = BoyFriend("男","170","55kg")
# mh.caiyi()
# mh.chuyi()
# print(mh.height)
class NanPengY(BoyFriend):
    def chuyi(self):
        print("韭菜炒鸡蛋")

mh = NanPengY("男","170cm","59kg")
mh.caiyi()
mh.chuyi()