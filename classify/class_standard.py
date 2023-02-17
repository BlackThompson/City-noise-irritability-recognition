# _*_ coding : utf-8 _*_
# @Time : 2023/2/17 18:37
# @Author : Black
# @File : class_standard
# @Project : my_noise_recognize

def classify(score):
    category = 0

    if score >= 5.85:
        category = 1
    elif 4.85 < score <= 5.85:
        category = 2
    elif 4.0 < score <= 4.85:
        category = 3
    elif score <= 4.0:
        category = 4

    return category

