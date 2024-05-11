
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 黑體字


# 外层数据
sizes_outer = [70, 20, 10]
labels = ['A', 'B', 'C']
labels2 = ['2019年', '2020年', '2021年']
colors = ['#ff9999','#66b3ff','#99ff99']

# 中间层数据
sizes_middle = [50, 40, 10]

# 内层数据
sizes_inner = [45, 30, 20]

# 绘制圆环图
fig, ax = plt.subplots()

# 绘制外层圆环
wedges_outer, _ = ax.pie( sizes_outer, colors=colors, radius=1.3, wedgeprops=dict(width=0.3, edgecolor='w'), startangle=90)

# 绘制中间层圆环
wedges_middle, _ = ax.pie(sizes_middle, colors=colors, radius=1.3-0.3, wedgeprops=dict(width=0.3, edgecolor='w'), startangle=90)

# 绘制内层圆环
wedges_inner, _ = ax.pie(sizes_inner, colors=colors, radius=1.3-0.6, wedgeprops=dict(width=0.3, edgecolor='w'), startangle=90)

# 在图表的外侧添加图例
ax.legend(wedges_outer, labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# 添加圓環中間的年份標籤，顯示在各層圓環內部

ax.text(0, -1.3+0.6+0.15,  labels2[0], ha='center', va='center', color='black', fontsize=10)
ax.text(0, -1.3+0.3+0.15,  labels2[1], ha='center', va='center', color='black', fontsize=10)
ax.text(0, -1.3+0.15,  labels2[2], ha='center', va='center', color='black', fontsize=10)
# 保证为正圆以避免变形
plt.axis('equal')

# 显示图形
plt.show()