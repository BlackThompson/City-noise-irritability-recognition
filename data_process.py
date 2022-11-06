# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score = pd.read_excel('原始数据197.xlsx')
    # represent the number of people
    num_person = score.shape[0]
    noise = '请对您听到的声音，表达您的吵闹感受，1表示非常吵闹，9表示一点也不吵闹'
    anl = '请对您听到的声音，表达您的烦躁感受，1表示非常烦躁，9表示一点也不烦躁'
    quiet = '请对您听到的声音，表达您的安静感受，1表示一点也不安静，9表示非常安静'

    # set the columns in the table
    score_columns = [noise, anl, quiet]
    new_columns = ['吵闹度', '烦躁度', '安静度']
    # read noise, anl, quiet from score (from excel)
    data = score[score_columns]

    data.columns = new_columns
    # data['序号'] = np.ones(num_person)
    # dfmi.loc[:, ('one', 'second')]
    data.loc[:, '序号'] = np.ones(num_person)
    for i in range(1, 83):
        # total 83 different kinds of sounds
        score_columns = [noise + '.%d' % i, anl + '.%d' % i, quiet + '.%d' % i]
        temp = score[score_columns]
        temp.columns = new_columns
        temp['序号'] = np.ones(num_person) * (i + 1)
        data = pd.concat([data, temp])
    writer = pd.ExcelWriter('处理后数据197_精简版.xlsx')
    data.to_excel(writer, float_format='%.5f')
    writer.save()
    writer.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
