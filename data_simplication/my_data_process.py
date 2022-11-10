# _*_ coding : utf-8 _*_
# @Time : 2022/10/27 20:53
# @Author : Black
# @File : my_data_process
# @Project : my_noise_recognize

import pandas as pd
import numpy as np

data = pd.read_excel('原始数据197.xlsx')

new_columns = ['声音类别', '姓名', '年龄', '职业', '学历', '性别',
               '最喜欢的声音类别', '最讨厌的声音类别', '心情', '感觉听到的声音类别',
               '吵闹度', '烦躁度', '安静度']

# test

num_person = data.shape[0]
like_content = ''
dislike_content = ''

like_sound = ['5 (鸟鸣虫叫)', '5 (海浪流水)', '5 (风雨)',
              '5 (生活、运动、交谈)', '5 (汽车声)', '5 (室外广播音乐)',
              '5 (机器施工声)', '5 (其他)']

dislike_sound = ['6 (鸟鸣虫叫)', '6 (海浪流水)', '6 (风雨)',
                 '6 (生活、运动、交谈)', '6 (汽车声)', '6 (室外广播音乐)',
                 '6 (机器施工声)', '6 (其他)']

for j in range(0, len(like_sound)):
    num = j + 1
    flag = data.loc[0, like_sound[j]]
    if (flag == 1) & (like_content == ''):
        like_content = str(num)
    elif (flag == 1) & (like_content != ''):
        like_content = like_content + ',' + str(num)

for j in range(0, len(dislike_sound)):
    num = j + 1
    flag = data.loc[0, dislike_sound[j]]
    if (flag == 1) & (dislike_content == ''):
        dislike_content = str(num)
    elif (flag == 1) & (dislike_content != ''):
        dislike_content = dislike_content + ',' + str(num)

test = data.iloc[:, 28:]
test.drop(test.columns[[-1, ]], axis=1, inplace=True)

test_list = list(test)
len(test_list)

# data.loc[0, '您的姓名：']
# data.loc[0, '1. 您的年龄']

processed_data = pd.DataFrame(columns=new_columns)

for i in range(0, num_person):
    like_content = ''
    dislike_content = ''

    name = data.loc[i, '您的姓名：']
    age = data.loc[i, '1. 您的年龄']
    job = data.loc[i, '2.您的职业']
    edu = data.loc[i, '3.您的学历']
    gender = data.loc[i, '4.您的性别']
    mood = data.loc[i, '7.您的心情如何？']

    for j in range(0, len(like_sound)):
        num = j + 1
        flag = data.loc[i, like_sound[j]]
        if (flag == 1) & (like_content == ''):
            like_content = str(num)
        elif (flag == 1) & (like_content != ''):
            like_content = like_content + ',' + str(num)

    for j in range(0, len(dislike_sound)):
        num = j + 1
        flag = data.loc[i, dislike_sound[j]]
        if (flag == 1) & (dislike_content == ''):
            dislike_content = str(num)
        elif (flag == 1) & (dislike_content != ''):
            dislike_content = dislike_content + ',' + str(num)

    for k in range(1, 84):
        listen_content = ''

        # sound_category = (k // 12) + 1
        sound_category = k

        sound_processing = test.iloc[i, ((k - 1) * 12): k * 12]

        for j in range(0, 9):
            num = j + 1
            flag = sound_processing[j]
            if (flag == 1) & (listen_content == ''):
                listen_content = str(num)
            elif (flag == 1) & (listen_content != ''):
                listen_content = listen_content + ',' + str(num)
        # 吵闹度
        noise = sound_processing[9]
        # 烦躁度
        anl = sound_processing[10]
        # 安静度
        quiet = sound_processing[11]
        # new_columns = ['声音类别', '姓名', '年龄', '职业', '学历', '性别',
        # '最喜欢的声音类别', '最讨厌的声音类别', '心情', '感觉听到的声音类别','吵闹度', '烦躁度', '安静度']
        temp = [sound_category, name, age, job, edu, gender, like_content, dislike_content,
                mood, listen_content, noise, anl, quiet]

        processed_data.loc[len(processed_data)] = temp

writer = pd.ExcelWriter('处理后数据197_完整版.xlsx')
processed_data.to_excel(writer)
writer.save()
writer.close()
