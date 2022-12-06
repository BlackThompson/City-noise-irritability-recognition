import os
import numpy as np
import xlrd
from models.soundtype_params import SoundtypeParams

import warnings

warnings.filterwarnings("ignore")

# 【！程序中唯一要改的地方】6个sheets的excel路径, 不成功一般就是excel不完整
# 改完后运行下面第四个cmd窗口的`python calc_param.py`指令即可
xls_path = "E:/artemis/excel/119-REC092212.xlsx"


def _extract_params():
    """
    [0927] 将计算excel指标的函数分离出来
    :return: soundtype_param
    """
    # load excel
    wb = xlrd.open_workbook(xls_path)
    params_dict = {}
    for idx in range(6):
        sheet = wb.sheet_by_index(idx)
        # print("!!!Tab", idx)
        param_type = sheet.cell(10, 1).value
        if param_type == 'pressure':
            param_type = 'leq'
        elif param_type == 'fluctuation strength':
            param_type = 'fluct'
        else:
            param_type = param_type.lower()
        values = []
        for i in range(15, min(sheet.nrows, 65521)):
            values.append(float(sheet.cell(i, 1).value))
        values = np.array(values)
        mean = values.mean()
        var = values.var()
        std = values.std(ddof=1)
        max = values.max()
        p_10 = np.percentile(values, 10, interpolation='midpoint')
        p_25 = np.percentile(values, 25, interpolation='midpoint')
        p_50 = np.percentile(values, 50, interpolation='midpoint')
        p_75 = np.percentile(values, 75, interpolation='midpoint')
        p_90 = np.percentile(values, 90, interpolation='midpoint')
        p_10_90 = p_90 - p_10

        params_dict["%s_mean" % param_type] = mean
        params_dict["%s_var" % param_type] = var
        params_dict["%s_std" % param_type] = std
        params_dict["%s_max" % param_type] = max
        params_dict["%s_10" % param_type] = p_10
        params_dict["%s_25" % param_type] = p_25
        params_dict["%s_median" % param_type] = p_50
        params_dict["%s_75" % param_type] = p_75
        params_dict["%s_90" % param_type] = p_90
        params_dict["%s_10_90" % param_type] = p_10_90

    soundtype_params = None
    try:
        file_name = os.path.basename(xls_path).replace("xlsx", "wav")
        # print(file_name, "!!!???")
        leq_mean = params_dict["leq_mean"]
        leq_std = params_dict["leq_std"]
        leq_25 = params_dict["leq_25"]
        leq_median = params_dict["leq_median"]
        leq_75 = params_dict["leq_75"]
        leq_10_90 = params_dict["leq_10_90"]
        loudness_mean = params_dict["loudness_mean"]
        loudness_std = params_dict["loudness_std"]
        loudness_25 = params_dict["loudness_25"]
        loudness_median = params_dict["loudness_median"]
        loudness_75 = params_dict["loudness_75"]
        loudness_10_90 = params_dict["loudness_10_90"]
        roughness_mean = params_dict["roughness_mean"]
        roughness_std = params_dict["roughness_std"]
        roughness_25 = params_dict["roughness_25"]
        roughness_median = params_dict["roughness_median"]
        roughness_75 = params_dict["roughness_75"]
        roughness_10_90 = params_dict["roughness_10_90"]
        sharpness_mean = params_dict["sharpness_mean"]
        sharpness_std = params_dict["sharpness_std"]
        sharpness_25 = params_dict["sharpness_25"]
        sharpness_median = params_dict["sharpness_median"]
        sharpness_75 = params_dict["sharpness_75"]
        sharpness_10_90 = params_dict["sharpness_10_90"]
        fluct_mean = params_dict["fluct_mean"]
        fluct_std = params_dict["fluct_std"]
        fluct_25 = params_dict["fluct_25"]
        fluct_median = params_dict["fluct_median"]
        fluct_75 = params_dict["fluct_75"]
        fluct_10_90 = params_dict["fluct_10_90"]
        tonality_mean = params_dict["tonality_mean"]
        tonality_std = params_dict["tonality_std"]
        tonality_25 = params_dict["tonality_25"]
        tonality_median = params_dict["tonality_median"]
        tonality_75 = params_dict["tonality_75"]
        tonality_10_90 = params_dict["tonality_10_90"]

        soundtype_params = SoundtypeParams(file_name, leq_mean, leq_std, leq_25, leq_median, leq_75, leq_10_90,
                                           loudness_mean, loudness_std, loudness_25, loudness_median, loudness_75,
                                           loudness_10_90, roughness_mean, roughness_std, roughness_25,
                                           roughness_median, roughness_75, roughness_10_90, sharpness_mean,
                                           sharpness_std, sharpness_25, sharpness_median, sharpness_75, sharpness_10_90,
                                           fluct_mean, fluct_std, fluct_25, fluct_median, fluct_75, fluct_10_90,
                                           tonality_mean, tonality_std, tonality_25, tonality_median, tonality_75,
                                           tonality_10_90)
        print("aaa", soundtype_params)
    except Exception as e:
        print("[ERROR] XlsProcessor: %s" % e)

    txt_content = ("\n".join(['{0}:{1}'.format(item[0], item[1]) for item in soundtype_params.__dict__.items()]))
    print(txt_content)
    file = open("C:/Users/Administrator/Desktop/output.txt", mode="a")
    file.write(xls_path + "\n")
    file.write(txt_content + "\n\n")

    return soundtype_params


_extract_params()
