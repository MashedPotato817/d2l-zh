import numpy as np
import matplotlib.pyplot as plt

# 生成 10000 个标准正态分布随机数
a = np.random.normal(0, 1, size=100000)

print("样本均值：", a.mean())
print("样本标准差：", a.std())

# -------------------------
# 1. 随机样本直方图
# -------------------------
plt.hist(
    a,
    bins=50,
    density=True,
    alpha=0.6,
    label="Samples"
)

# -------------------------
# 2. 理论正态分布
# -------------------------
x = np.linspace(-4, 4, 200)

y = 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

plt.plot(
    x,
    y,
    linewidth=2,
    label="N(0, 1)"
)

plt.xlabel("x")
plt.ylabel("Density")
plt.title("Random Samples vs Normal Distribution")
plt.legend()

plt.show()