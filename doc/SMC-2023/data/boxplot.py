import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
data = [[0.77,0.76,0.73],
        [0.79,0.80,0.78],
        [0.88,0.86,0.83],
        [0.88,0.87,0.84],
        [0.86,0.85,0.83],
        [0.86,0.81,0.77],
        [0.86,0.85,0.83],
        [0.79,0.78,0.75],
        [0.84,0.83,0.79],
        [0.85,0.85,0.84]]

df = pd.DataFrame(data, columns=['top1', 'top3', 'top5'])

# 创建箱线图
bp = plt.boxplot([df['top1'], df['top3'], df['top5']], patch_artist=True)

# 设置箱体颜色
colors = ['#ffb3b3', '#c1d6eb', '#ffeeba']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# 设置中位数线颜色
for median in bp['medians']:
    median.set(color='#000000')

# # 添加分位点的值
for i, label in enumerate(['Q1', 'Q2', 'Q3']):
    plt.text(i + 1, bp['whiskers'][0 + i * 2].get_ydata()[1], f'{bp["whiskers"][0 + i * 2].get_ydata()[1]:.2f}', ha='center', fontsize=10)
    plt.text(i + 1, bp['medians'][i].get_ydata()[0], f'{bp["medians"][i].get_ydata()[0]:.2f}', ha='center', fontsize=10)
    plt.text(i + 1, bp['whiskers'][1 + i * 2].get_ydata()[1], f'{bp["whiskers"][1 + i * 2].get_ydata()[1]:.2f}', ha='center', fontsize=10)
 
# 设置标签
plt.xlabel('Evaluation Indicator')
plt.ylabel('Score')

# 设置横坐标标签
plt.xticks([1, 2, 3], ['T1', 'T3', 'T5'])
plt.grid(axis='y')

# 显示图表
plt.show()
