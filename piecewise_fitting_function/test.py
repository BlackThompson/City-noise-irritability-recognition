# import numpy as np
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
# from sklearn.metrics import mean_squared_error, r2_score
#
# # 输入数据
# x_data = [7.14, 6.24, 5.64, 5.26, 5.04, 4.69, 4.2, 4.18, 3.89, 3.67, 3.27]
# y_data = [-5.6455, -5.931875, -4.481125, -4.3835, -4.7275, -4.491125, -4.433, -2.549125, -2.11725, -0.21225, 3.0655]
#
#
# # 定义拟合函数
# def piecewise_linear(x, k1, k2, y0):
#     x0 = 4.18
#     return np.piecewise(x, [x <= x0, x > x0],
#                         [lambda x: k1 * (x - x0) + y0, lambda x: k2 * (x - x0) + y0])
#
#
# # 拟合数据
# popt, pcov = curve_fit(piecewise_linear, x_data, y_data)
#
# # 输出拟合结果
# print('k1 =', popt[0])
# print('k2 =', popt[1])
# print('y0 =', popt[2])
#
# # 绘制拟合结果
# x = np.linspace(min(x_data), max(x_data), 100)
# plt.scatter(x_data, y_data, label='data')
# plt.plot(x, piecewise_linear(x, *popt), label='fit')
# plt.legend()
# plt.show()
#
# #
import matplotlib.pyplot as plt
import numpy as np

# 生成一些数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制两条线
line1, = plt.plot(x, y1, "--", label="Sin")
line2, = plt.plot(x, y2, ":", label="Cos")

# 添加图例并显示图像
plt.legend(handles=[line1, line2], labels=["Sine Wave", "Cosine Wave"])
plt.show()

