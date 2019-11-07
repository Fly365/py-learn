# from . import _mklinit
# ImportError: DLL load failed: 找不到指定的模块。
# 上面错误需要配置环境变量
# D:\development\Anaconda3
# D:\development\Anaconda3\Scripts
# D:\development\Anaconda3\Library\bin
import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 给x轴设置值
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
