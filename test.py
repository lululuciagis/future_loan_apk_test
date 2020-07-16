# import keyword
# print(keyword.kwlist)
# python底层的关键字有：
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
#  'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
#  'else', 'except', 'finally', 'for', 'from', 'global', 'if',
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
#  'raise', 'return', 'try', 'while', 'with', 'yield']

"""
python底层的关键字有：
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global', 'if',
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
'raise', 'return', 'try', 'while', 'with', 'yield']
# """
# phone=input("lucia 的手机号码为： ")
# print(phone)
# print1=88
# print(type(print1))

# print('scb14-lucia')
# print("scb14-lucia")
# print('''scb14-lucia''')
# print('"scb14-lucia"')
# print("'scb14-lucia'")

# print('''~~~~~~~~~~scb14-lucia~~~~~~~~~~
# %考勤情况：全勤
# %上课学习情况：良好
# %课后作业情况：优秀
#
#      ''')

# str1 = "scb14-lucia"
# print(str1[::]) #默认输出[0:12:1]这种情况下的字符串
# print(str1[:]) #缺省头尾表示从0取到最后一个，步长为默认1
# print(str1[0:])#缺省尾部和步长，表示从0取到最后1个
# print(str1[0:10])#不会取到第10+1位字符a
# print(str1[-2])#表示取倒数第二位字符i
# print(str1[0:len(str1):2])#按步长2输出sb4lca
# str2 = str1.replace("lucia","lulu")
# print(str2)

# str1 = "scb14-lucia"
# print(str1.find("lucia")) # l在str1中的开始索引为6，输出6
# str1 = "scb14-lucia"
# print (str1.find("lulu")) # lulu在str1中不存在，不报错，返回-1

# name_1 = "lucia"
# height_1 = 155
# weight_1 = 44.5
# name_2 = "tracy"
# height_2 = 175
# weight_2 = 65
#
# print('''~~~~~~~~~~{}的基本信息~~~~~~~~~~
# name：{}
# height：{}
# weight：{}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# '''.format(name_2,name_2,height_2,weight_2))    # 没有指定顺序

# print('''~~~~~~~~~~%s的基本信息~~~~~~~~~~
# name：%s
# height：%d
# weight：%d
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# '''%(name_2,name_2,height_2,weight_2))    # 指定了顺序

# a=9
# b=2
# a += b   #a=a+b
# print(a)
# a -= b   #a=a-b
# print(a)
# a *= b   #a=a*b
# print(a)
# a /= b   #a=a/b
# print(a)
# print(13%4)
# a=9
# b=2
# print(not a<b and not b >3)

# str1 = "scb14-"
# str2 = "lucia"
# a = 20
# print((str1 + str2 + str(a))*5)   # (str1 + str2 + str(a))中的内容出现5次

# str1 = "scb14-lucia"
# str2 = "lucia"
# print(str2 in str1)

# str1=input("请输入姓名: ")
# str2=input("请输入年龄: ")
# str3=input("请输入性别: ")
# print("*"*18)
# print('''姓名:{0}
# 性别:{1}
# 年龄:{2}'''.format(str1,str2,str3))
# print("*"*18)

# str1 = "python hello aaa 123123aabb"
# print(str1.index("aaa"))


# list1 = [12,1.23,True,"lucia",[1,2,3]]
# print(list1[3])   #把列表中的lucia字符串取出来
# print(list1[::2])   #每隔一个元素取出
# print(list1[-2])   #取出倒数第二个元素
# print(list1[:len(list1)]) #取出列表中的所有元素
# print(list1[4][2])  #嵌套取值，取出列表中的字列表[1,2,3]中3
# print(list1[3][2])  #嵌套取值，取出列表中的lucia字符串中的c
# list1 = [12, 1.23, True, "lucia", [1, 2, 3]]
# list1.append(123)   #在列表末尾增加一个123
# print(list1)
# list1.insert(2,"tracy")
# print(list1)   #在列表索引为2的地方插入一个tracy字符

# list1 = [12, 1.23, True, "lucia", [1, 2, 3]]
# list1.pop()    #默认删除最后一个元素
# print(list1)
# list1.pop(1)    #删除索引为1位置处的元素
# print(list1)

# list1 = [12, 1.23, True, "lucia", [1, 2, 3]]
# list1.remove(1.23)  #指定删除1.23
# print(list1)
#
# list1 = [12, 1.23, True, "lucia", [1, 2, 3],"lucia"]
# list1.remove("lucia")  #指定删除lucia，由于lucia重复，删除先找到的一个lucia
# print(list1)

# list1 = [12, 1.23, True, "lucia", [1, 2, 3],"lucia"]
# list1.clear()
# print(list1)
#
# list1 = [12, 1.23, True, "lucia", [1, 2, 3]]
# list1[3]="lulu"  #把lucia改为lulu
# print(list1)


# dict1 = {"name":"lucia","height":155,"weight":44,"hobby":["shopping","eating"]}
# print(dict1)
# print(dict1["hobby"])  #直接取变量名为hobby对应的value值
# print(dict1.get("weight")) #通过get()函数来取变量名为weight对应的value值
# print(dict1.values()) #通过values()取所有值 ，注意取出来的格式
# print(dict1.items()) # 通过items()获取整个字典的集合，每一个key：value和元祖类似

# dict1 = {"name": "lucia", "height": 155, "weight": 44, "hobby": ["shopping", "eating"]}
# # dict1["color"] = "light yellow"
# # print(dict1)
# # dict1.update({"colour":"light yellow"})
# # print(dict1)
# dict1["colour"] = "light purple"
# print(dict1)
# dict1.pop("colour")
# print(dict1)
#
# salary = int(input("请输入你预期的求职底薪: "))   #input("请输入你预期的求职底薪: ")为字符串，需要强制转换为int
# if salary >25000:
#     print("工资太高，求职单位可能不会同意")
# elif salary >=18000:
#     print("好好面试，有机会通过")
# else:
#     print("工资太低，自己不会考虑")
#
# str1 = "！疫情赶紧过去！"
# for i in str1:
#     print(i)
#
# list1 = ["lucia","tracy",123,"hk"]
# for i in list1:
#     print(i)
#
# tuple1 = ("lucia","tracy",123,"hk")
# for i in tuple1:
#     if i == "tracy":
#         continue
#     print(i)

# dict1 = {"name": "lucia", "height": 155, "weight": 44, "hobby": ["shopping", "eating"]}
# for i in dict1.items():
#     if i == ("weight",44):
#         continue
#     print(i)
#
#
# j = 0
# for i in range(1,8):
#     j += i
# print(j)

# a = [1, 2, '6', 'summer']
# a1 = a[1]
# print(a1 in a)
# a2 = a[2]
# print(a2 in a)
# a3 = a[-2]
# print(a3 in a)
# a4 = a[-1]
# print(a4 in a)
#
# """
# 或者下面
# """
# a = [1, 2, '6', 'summer']
# for i in a:
#     print(i in a)
#
#
# dict_1 = {"class_id": 45, 'num': 20}
# number = dict_1['num']
# if number > 5:
#     print("课堂人数为：{}".format(number))

# list3 = ['先森', '小米椒', 'lucia', 'K', '建文', '婷婷']
# dict1 = {'name': '先森', 'gender': 'M', 'age': 20,'city': '广州'}
# dict2 = {'name': '小米椒', 'gender': 'F', 'age': 21, 'city': '长沙'}
# dict3 = {'name': 'lucia', 'gender': 'F', 'age': 22, 'city': 'HK'}
# dict4 = {'name': 'K', 'gender': 'M', 'age': 23, 'city': 'SZ'}
# dict5 = {'name': '建文', 'gender': 'M', 'age': 24, 'city': '武汉'}
# dict6 = {'name': '婷婷', 'gender': 'F', 'age': 25, 'city': '上海'}
# list3.clear()
# list3.append(dict1)
# list3.append(dict2)
# list3.append(dict3)
# list3.append(dict4)
# list3.append(dict5)
# list3.append(dict6)
# print(list3)
# print("——"*50)
# print("也可以下面方式建列表list")
# print("——"*50)
# list3[0]=dict1
# list3[1]=dict2
# list3[2]=dict3
# list3[3]=dict4
# list3[4]=dict5
# list3[5]=dict6
# print(list3)

# list1 = [1,2,'lucia']
# list1.append("lulu")
# print(list1)
# print(list1.pop(1))  #同append函数，仅能改变值，函数本身没有return值，所以返回打印为none
#
# list1 = [1, 2, 'lucia']
# list1.pop()
# # print(list1)
# print(list1.pop(1))  #同append函数，仅能改变值，函数本身没有return值，所以返回打印为none

# dict1 = {"我司": "lucia"}
# print(dict1)
#
# dict1=dict(name='lucia', city='hk')
# print(dict1)
# def good_job(bonus,subsidy,salary=18000,*args,**kwargs):   #salary,bonus,subsidy为形参
#     print("salary:{}".format(salary))
#     print("bonus:{}".format(bonus))
#     print("subsidy:{}".format(subsidy))
#     print("args:{}".format(args))
#     print("kwargs:{}".format(kwargs))
#     sum = salary + bonus + subsidy
#     for i in args:
#         sum +=i
#     for j in kwargs:
#         sum += kwargs.get(j)
#     print("总工资为:{}".format(sum))
#     return sum,bonus  #如果没有返回值，则输出为none
#
# sum1 = good_job(2000,1000,28000,1500,2500,3500,bonus1=1000,bonus2=1000)  #定义一个变量接收函数的返回值
# print(sum1)
# print(sum1[0])
# if sum1[0] >=50000:
#     print("工资不错，好好加油，争取工资再上一层楼")
# else:
#     print("不要泄气，慢慢努力，找到好工作")

# list3 = ['先森', '小米椒', 'lucia', 'K', '建文', '婷婷']
# dict1 = dict(name = "先森", gender ='M',age = 20, city = '广州')
# dict2 = dict(name = "小米椒", gender ='F',age = 21, city = '长沙')
# dict3 = dict(name = "lucia", gender ='F',age = 22, city = 'HK')
# dict4 = dict(name = "K", gender ='M',age = 23, city = 'SZ')
# dict5 = dict(name = "婷婷", gender ='F',age = 24, city = '上海')
# list3.clear()
# list3.append(dict1)
# list3.append(dict2)
# list3.append(dict3)
# list3.append(dict4)
# list3.append(dict5)
# print(list3)

# sum = 0
# for i in range(23,58):
#     sum += i
# print(sum)

# def bigger_than_5(a):
#     print(len(a) > 5)
#
# bigger_than_5({"name": "lucia","height":155,"weight":44})
# bigger_than_5(["name", "lucia", "height", 155,"weight", 44])
# bigger_than_5("abcd")

#
# a = "lucia height"
# list1 =[]
# for i in range(0,len(a)):
#     list1.append(a[i])
# print(list1)
# dict1 = {"name":12,"age":34,"hei":56}
# dict1.update({"whatq":12})
# print(dict1)
#
# dict1 = {"name": "lucia", "height": 155, "weight": 44, "hobby": ["shopping", "eating"]}
# dict1["color"] = "light yellow"
# print(dict1)
# dict1.update({"color":"light purple"})
# print(dict1)

#导入requests第三方库
import requests
#导入jsonpath第三方库
import jsonpath
#def post(url, data=None, json=None, **kwargs):  post请求函数
#:param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`. #headers，注意看是字典格式
# url_register = 'http://120.78.128.25:8766/futureloan/member/register'  #注册模块的接口地址
# json_register = {
#   "mobile_phone": "15914114801",
#   "pwd": "qwe12345",
#   "type":"1",
#   "reg_name":"lucia"
# }   # 注册模块的请求正文
# headers_register = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'} #注册模块的请求头
#
# result_register = requests.post(url = url_register,json = json_register , headers = headers_register) #全部用关键字传参，post请求
# print(result_register.content.decode('utf8'))
#print(result_register.text)
# print(result_register.json())
########################登录请求#################################
# url_login = 'http://120.78.128.25:8766/futureloan/member/login'  #登录模块的接口地址
# json_login = {
#   "mobile_phone": "15914114801",
#   "pwd": "qwe12345",
# }   # 登录模块的请求正文
# headers_login = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'} #登录模块的请求头
#
# result_login = requests.post(url = url_login,json = json_login , headers = headers_login) #全部用关键字传参，post请求
# print(result_login.json())
########################充值请求#################################
# url_recharge = 'http://120.78.128.25:8766/futureloan/member/recharge'  #充值模块的接口地址
#字典嵌套取值
# token_login = result_login.json()['data']['token_info']['token']
# member_id = result_login.json()['data']['id']

#利用jsonpath第三方库来充值
# token_login = jsonpath.jsonpath(result_login.json(),'$..token')[0]#$..token也可以为$.data.token_info.token[0]
# member_id = jsonpath.jsonpath(result_login.json(),'$..id')[0]#$..id也可以为$.data.id[0]
# #print(token_login,member_id)
# json_recharge ={
#         "member_id": member_id,
#         "amount": "100"
# }
# 充值模块的请求正文
# headers_recharge = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer'+' '+token_login} #充值模块的请求头
#
# result_recharge = requests.post(url = url_recharge,json = json_recharge , headers = headers_recharge) #全部用关键字传参，post请求
# print(result_recharge.json())

# #定义一个接口测试的函数，post请求方式
# def api_test(url1,json1,headers1):
#     result = requests.post(url=url1, json=json1, headers=headers1)
#     return result.json() #也可以设置a =result.json(), return a

#调用函数------注册模块
# url_register = 'http://120.78.128.25:8766/futureloan/member/register'  #注册模块的接口地址
# json_register = {
#   "mobile_phone": "15914114999",
#   "pwd": "qwe12345",
#   "type":"1",
#   "reg_name":"lucia"
# }   # 注册模块的请求正文
# headers_register = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'} #注册模块的请求头
# result_register = api_test(url1=url_register,json1=json_register,headers1=headers_register)
# print(result_register)


#定义一个接口测试的函数，post请求方式
# def api_test(url1,json1,headers1):
#     result = requests.post(url=url1, json=json1, headers=headers1)
#     response = result.json()
#     return response #也可以直接设置return result.json()
# #################调用函数-----登录模块#######################3
# url_login = 'http://120.78.128.25:8766/futureloan/member/login'  #注册模块的接口地址
# json_login = {
#   "mobile_phone": "15914114999",
#   "pwd": "qwe12345"
# }   # 登录模块的请求正文
# headers_login = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'} #注册模块的请求头
# ######################### 调用函数，实现登录模块接口测试###############################3
# response_login = api_test(url1=url_login,json1=json_login,headers1=headers_login)
# print(response_login)
#
# member_id = jsonpath.jsonpath(response_login,'$..id')[0]
# token_login = jsonpath.jsonpath(response_login,'$..token')[0]
# url_recharge = 'http://120.78.128.25:8766/futureloan/member/recharge'  #充值模块的接口地址
# json_recharge = {
#   "member_id": member_id,
#   "amount": 1000
# }   # 充值模块的请求正文
# headers_recharge = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer'+' '+token_login} #充值模块的请求头
# ######################### 调用函数，实现充值模块接口测试###############################3
# response_recharge = api_test(url1=url_recharge,json1=json_recharge,headers1=headers_recharge)
# print(response_recharge)




#定义一个接口测试的函数，get请求方式
# def api_test(url1,headers1):
#     result = requests.get(url=url1, headers=headers1)
#     return result.content.decode('utf8')
#
# ##################调用函数-----访问百度网页#######################3
# url_baidu = 'https://www.baidu.com'
# headers_baidu = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'} #查看F12
#
# response_baidu = api_test(url1=url_baidu,headers1=headers_baidu)
# print(response_baidu)
#
# headers_baidu = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# response_baidu = requests.get(url = 'https://www.baidu.com',headers=headers_baidu)
# print(response_baidu.content.decode('utf8'))


#定义一个接口测试的函数，post请求方式，返回token
# def api_test(url1,json1,headers1):
#     result = requests.post(url=url1, json=json1, headers=headers1)
#     response = result.json()
#     member_id = jsonpath.jsonpath(response,'$..id')[0]
#     token_login = jsonpath.jsonpath(response,'$..token')[0]
#     return response,member_id,token_login
# #定义一个接口测试的函数，post请求方式,不返回token
# def api_test_notoken(url1,json1,headers1):
#     result = requests.post(url=url1, json=json1, headers=headers1)
#     response = result.json()
#     return response
# url_login = 'http://120.78.128.25:8766/futureloan/member/login'  #注册模块的接口地址
# json_login = {
#   "mobile_phone": "15914114999",
#   "pwd": "qwe12345"
# }   # 登录模块的请求正文
# headers_login = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json'} #注册模块的请求头
# response_login = api_test(url1=url_login,json1=json_login,headers1=headers_login)  #调用
# print(response_login)
# url_recharge = 'http://120.78.128.25:8766/futureloan/member/recharge'  #充值模块的接口地址
# json_recharge = {
#    "member_id": response_login[1],
#    "amount": 1000
# }   # 充值模块的请求正文
# #print("id调用了没:{}".format(response_login[1]))
# headers_recharge = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer'+' '+response_login[2]} #充值模块的请求头
# #print("token调用了没:{}".format(response_login[2]))
# response_recharge = api_test_notoken(url1=url_recharge,json1=json_recharge,headers1=headers_recharge)
# print("我的余额为:{}".format(response_recharge['data']['leave_amount']))


# #安装导入openpyxl库
# import openpyxl
# #定义一个python读取excel列表的函数
# def read_excel(workbookname,sheetname):
#     # 工程中放入excel表格
#     #加载工作簿
#     workbook = openpyxl.load_workbook(workbookname)
#     #获取表单
#     sheet = workbook[sheetname]
#     data_api_test = [] #创建一个空列表，用来存放所有测试用例
#     #获取单元格
#     for i in range(2,sheet.max_row+1):#注意range()，读头不读尾，这里取值max_row+1
#         dict_excel = \
#             dict(
#             case_id_excel = sheet.cell(row=i,column=1).value,    #获取case_id
#             url_excel = sheet.cell(row=i,column=5).value,    #获取url
#             data_excel = sheet.cell(row = i,column = 6).value,  #获取data
#             expected_excel = sheet.cell(row = i,column = 7).value   #获取expected
#             )
#         data_api_test.append(dict_excel)  #循环一次，追加一次生成的字典到列表中
#     #print(data_api_test) #打印最终列表结果
#     return data_api_test
#
# api_test_data = read_excel('api_test.xlsx','register')   #调用函数
# print(api_test_data)

# #安装导入openpyxl库
# import openpyxl
# #定义一个python写数据至excel中的函数
# def write_excel(workbookname,sheetname,row1,column1,content):
#     #加载工作簿
#     workbook = openpyxl.load_workbook(workbookname)
#     #获取表单
#     sheet = workbook[sheetname]
#     #写入结果
#     sheet.cell(row=row1,column=column1).value=content
#     workbook.save(workbookname)
#
# #调用函数
# api_test_passorfalse = write_excel('api_test.xlsx','register',2,8,'pass')
#
#
#
# b='12+20'
# print(eval(b))
# a = {'X-Lemonban-Media-Type':'lemonban.v2','Content-Type':'application/json','Authorization':'Bearer'}
# print(eval(a))



# a = tuple("abc")
# b = str('123')
# c = list('12345')
# print(a)
# print(b)
# print(c)

# a = 'wkdj  lkjdkf  dhfka'
# list1 = list(a)
# print(list1)

def bigger_than5(a):
    if type(a)==list or type(a)==str or type(a)==dict:
        if len(a)>=5:
            print("True")
        else:
            print('False')
    else:
        print("输入对象不是列表、字典或字符串")

result = bigger_than5("8765")


