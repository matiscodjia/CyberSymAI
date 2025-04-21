import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("../data/processed/features.csv")
print(df.describe())
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")

ax.scatter(df["tcp"], df["udp"], df["icmp"], c="gray", alpha=0.6)
ax.set_xlabel("tcp")
ax.set_ylabel("udp")
ax.set_zlabel("icmp")

plt.show()
