import numpy as np
import pandas as pd
import re
import csv


f=open('province.csv','a+',encoding='utf-8',newline='')
writer=csv.writer(f)
friends_file = pd.read_csv('E:/itchat_friends_analyse/merge_image/friends_file.csv')
sex = friends_file.groupby('sex').size()
city = friends_file.groupby('city').size()
province = friends_file.groupby('province').size()
sex_type = list(sex.index)
sex_num = list(sex)
province_name = list(province.index)
province_num = []
city_name = list(city.index)
city_num = list(city)
dele_num = 0
for i in range(len(province_name)):
    s=province_name[0]
    l=len(re.findall('[a-zA-Z]',s))
    if l!=0:
        province_name.pop(0)
        dele_num +=1
for j in range(len(province_name)):
    province_num.append(province[j+dele_num])
province_name.pop(9)
province_num.pop(9)
for i in range(len(province_name)):
    writer.writerow([province_name[i],province_num[i]])

# print(province_name)
# print(province_num)

# print(province_num)

# print(city)
# print(province)
# print(type(friends_file))
# head = friends_file.head(10)
# print(head['sex'])
# print(head.values)
# print(head.columns)
# print(head.describe)
# print(pd.Series().value_counts())
# group = head.groupby('city').sum()      #以该属性分组,其他属性相加
# group1 = head.groupby('city').size()    #统计中某一列中各个数据出现的次数
# print(group)
# print(type(group1))
# print(group1)   #是Series类型
# print(group1[0])    #得到第一个数据的出现次数
# sex = head.groupby('sex').size()
# print(sex)
