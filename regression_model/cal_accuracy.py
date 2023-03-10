# _*_ coding : utf-8 _*_
# @Time : 2022/12/17 13:01
# @Author : Black
# @File : cal_accuracy
# @Project : my_noise_recognize

def classify(predict_score, true_score):
    """
    classify the score in the vague section

    :param predict_score:
    :param true_score:
    :return:
    """
    # class-2 mean: 5.3
    # class-3 mean: 4.4
    # category = [1, 2, 3, 4]
    # predict_class = pre_classify(predict)
    # true_class = pre_classify(true)
    #
    # # there is a score in the vague section
    # # the vague section is near the category section
    # if abs(predict_class - true_class) < 1:
    #     predict_class = round((predict_class + true_class) / 2, 0)
    #     true_class = predict_class
    #
    # # the vague section is not near the category section
    # if abs(predict_class - true_class) >= 1:
    #     if predict_class not in category:
    #         predict_class = int(predict_class)
    #     if true_class not in category:
    #         true_class = int(true_class)
    #
    # # if the predict score and true score is in class-2 and class-3
    # # and their difference is less than (5.3 - 4.4) = 0.9
    # if (predict_class == 2 and true_class == 3) or (predict_class == 3 and true_class == 2):
    #     if abs(predict - true) < 0.9:
    #         predict_class = true_class
    #
    # if (predict_class == 4 and true_class == 3) or (predict_class == 3 and true_class == 4):
    #     if abs(predict - true) < 0.8:
    #         predict_class = true_class
    #
    # return int(predict_class), int(true_class)

    predict_set = {}
    true_set = {}
    predict_class, true_class = 0, 0

    predict_set = pre_classify(predict_score)
    true_set = pre_classify(true_score)

    # 1. If the intersection of two set is empty
    if not predict_set & true_set:
        predict_class = min(predict_set)
        true_class = min(true_set)

    # 2. If the intersection of two set is not empty
    if predict_set & true_set:
        # min() 只是为了把值取出来
        predict_class = min(predict_set.intersection(true_set))
        true_class = predict_class

    return predict_class, true_class


def pre_classify(score):
    """
    judge whether the score is in the vague section

    :param score:
    :return:
    """
    # # 1.5, 2.5, 3.5 are not represent the true number
    # # they mean the vague section
    # category = 0
    #
    # if score >= 6.0:
    #     category = 1
    # elif 5.7 < score < 6.0:
    #     category = 1.5
    # elif 4.9 < score <= 5.7:
    #     category = 2
    # elif 4.8 < score <= 4.9:
    #     category = 2.5
    # elif 4.1 < score <= 4.8:
    #     category = 3
    # elif 4.0 < score <= 4.1:
    #     category = 3.5
    # elif score <= 4.0:
    #     category = 4

    category = {}
    if score < 3.8:
        category = {4}
    elif 3.8 <= score <= 4.3:
        category = {3, 4}
    # elif 4.3 < score < 4.6:
    #     category = {3}
    # elif 4.6 <= score <= 5:
    #     category = {2, 3}
    # elif 5 < score < 5.6:
    #     category = {2}
    # Include all the type 2 and type 3 points into the fuzzy interval
    elif 4.3 < score < 5.6:
        category = {2, 3}
    elif 5.6 <= score <= 6:
        category = {1, 2}
    elif score > 6:
        category = {1}

    # category = {}
    # if score < 3:
    #     category = {4}
    # elif 3 <= score <= 4:
    #     category = {3, 4}
    # elif 4 < score < 4.5:
    #     category = {3}
    # elif 4.5 <= score <= 5.5:
    #     category = {2, 3}
    # elif 5.5 < score < 6:
    #     category = {2}
    # elif 6 <= score <= 7:
    #     category = {1, 2}
    # elif score > 7:
    #     category = {1}

    return category


def accuracy(predict_class_list, true_class_list):
    all = len(predict_class_list)
    same = 0
    for i in range(len(predict_class_list)):
        if predict_class_list[i] == true_class_list[i]:
            same += 1
    return same / all


def return_predict_and_true_class(predict_score_list, true_score_list):
    predict_class_list = []
    true_class_list = []
    for i in range(len(predict_score_list)):
        # predict, true = classify(predict_score_list.iloc[i], true_score_list.iloc[i])
        predict, true = classify(predict_score_list[i], true_score_list[i])
        predict_class_list.append(predict)
        true_class_list.append(true)
    return predict_class_list, true_class_list
