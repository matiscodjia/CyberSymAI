import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN, KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# === 1. Charger ton fichier CSV ===
# Remplace par le chemin vers ton vrai fichier
data = pd.read_csv("../data/processed/features.csv")  # Exemple : ["tcp", "udp", "icmp"]
features = ["tcp", "udp", "icmp"]

# === 2. Standardiser les données ===
X = data[features].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === 4. KMeans clustering ===
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# === 8. Visualisation 3D colorée (KMeans) ===
fig3d = plt.figure(figsize=(6, 6))
ax3d = fig3d.add_subplot(111, projection="3d")
ax3d.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans_labels, cmap="viridis", alpha=0.6)
ax3d.set_xlabel("tcp")
ax3d.set_ylabel("udp")
ax3d.set_zlabel("icmp")
ax3d.set_title("3D Clustering (KMeans)")

plt.show()
