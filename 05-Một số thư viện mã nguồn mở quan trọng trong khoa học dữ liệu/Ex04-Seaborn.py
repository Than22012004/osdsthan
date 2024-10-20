import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load dữ liệu (giả sử dữ liệu đã được lưu trong file CSV)
tips = sns.load_dataset("tips")

# 1. Biểu đồ phân tán (scatter plot)
sns.scatterplot(x="total_bill", y="tip", hue="smoker", data=tips)
plt.title("Mối quan hệ giữa tổng hóa đơn và tiền boa")
plt.show()

# 2. Biểu đồ hộp (box plot)
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Phân bố tổng hóa đơn theo ngày")
plt.show()

# 3. Biểu đồ phân phối (histogram)
sns.histplot(data=tips, x="total_bill", hue="sex", multiple="stack")
plt.title("Phân phối tổng hóa đơn theo giới tính")
plt.show()

# 4. Ma trận tương quan (pairplot)
sns.pairplot(tips, hue="smoker")
plt.show()