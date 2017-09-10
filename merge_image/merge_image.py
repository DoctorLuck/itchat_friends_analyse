import PIL.Image as Image
from get_friends.get_friends import get
import os
import math


# get()
# 这是一个列表
img_list = os.listdir('E:/itchat_friends_analyse/friend_head')
path='E:/itchat_friends_analyse/friend_head/'
# 规定一行放的图片数目
line_num = math.ceil(math.sqrt(len(img_list)))
# print(img_list)
# 规定每个图片的大小
size = 60
# 定义最后生成的图片的大小
all_img = Image.new('RGB',((line_num-1)*60,(line_num-1)*60))
row = 0
column = 0
for i in range(1,len(img_list)):
    img = Image.open(path+str(i)+'.jpg')
    img = img.resize((size,size),Image.ANTIALIAS)
    all_img.paste(img,(row*size,column*size))
    column += 1
    if column==line_num:
        row +=1
        column = 0

all_img.save('friends.jpg')



