# Cluster analysis on StudentsPerformance.csv with downloadable plots

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

# --- Load dataset ---
df = pd.read_csv("/mnt/data/StudentsPerformance.csv")

# Select numeric features for clustering
X = df[['math score', 'reading score', 'writing score']].copy()

# Standardize features
scaler = StandardScaler()
Z = scaler.fit_transform(X)

# ------------------------------
# Hierarchical clustering (Ward)
# ------------------------------
link_mat = linkage(Z, method='ward')

# Dendrogram (truncate for readability)
plt.figure(figsize=(10, 5))
dendrogram(link_mat, truncate_mode='lastp', p=20, leaf_rotation=90)
plt.title("Dendrogram (Ward, truncated to last 20 merges)")
plt.xlabel("Cluster Index")
plt.ylabel("Distance")
plt.tight_layout()
dendrogram_path = "/mnt/data/dendrogram_ward.png"
plt.savefig(dendrogram_path)
plt.close()

# Choose k via silhouette for k=2..6
sil_scores_hier = {}
for k in range(2, 7):
    labels_k = fcluster(link_mat, k, criterion='maxclust')
    sil_scores_hier[k] = silhouette_score(Z, labels_k)

best_k_hier = max(sil_scores_hier, key=sil_scores_hier.get)
labels_hier = fcluster(link_mat, best_k_hier, criterion='maxclust')

# ------------------------------
# K-means clustering (non-hierarchical)
# ------------------------------
sil_scores_kmeans = {}
kmodels = {}
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(Z)
    kmodels[k] = km
    sil_scores_kmeans[k] = silhouette_score(Z, labels)

best_k_kmeans = max(sil_scores_kmeans, key=sil_scores_kmeans.get)
kmeans_model = kmodels[best_k_kmeans]
kmeans_labels = kmeans_model.labels_

# ------------------------------
# PCA for 2D visualization
# ------------------------------
pca = PCA(n_components=2, random_state=42)
Z2 = pca.fit_transform(Z)

# Plot KMeans clusters in PCA space
plt.figure(figsize=(7, 6))
plt.scatter(Z2[:, 0], Z2[:, 1], c=kmeans_labels, alpha=0.8)
plt.title(f"K-Means Clusters (k={best_k_kmeans}) in PCA Space")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
kmeans_plot_path = "/mnt/data/kmeans_pca.png"
plt.savefig(kmeans_plot_path)
plt.close()

# Plot Hierarchical clusters in PCA space
plt.figure(figsize=(7, 6))
plt.scatter(Z2[:, 0], Z2[:, 1], c=labels_hier, alpha=0.8)
plt.title(f"Hierarchical Clusters (Ward, k={best_k_hier}) in PCA Space")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.tight_layout()
hier_plot_path = "/mnt/data/hier_pca.png"
plt.savefig(hier_plot_path)
plt.close()

# Save silhouette summaries to a simple text file for reference
summary_text_path = "/mnt/data/cluster_summaries.txt"
with open(summary_text_path, "w") as f:
    f.write("Silhouette Scores (Hierarchical - Ward):\n")
    for k, v in sil_scores_hier.items():
        f.write(f"k={k}: {v:.3f}\n")
    f.write("\nSilhouette Scores (KMeans):\n")
    for k, v in sil_scores_kmeans.items():
        f.write(f"k={k}: {v:.3f}\n")
    f.write(f"\nBest k (Hierarchical) = {best_k_hier}\n")
    f.write(f"Best k (KMeans) = {best_k_kmeans}\n")

# Prepare a small dict of key outputs
{
    "best_k_hierarchical": best_k_hier,
    "best_k_kmeans": best_k_kmeans,
    "dendrogram_path": dendrogram_path,
    "kmeans_plot_path": kmeans_plot_path,
    "hier_plot_path": hier_plot_path,
    "summary_text_path": summary_text_path,
    "kmeans_centers_original_scale": scaler.inverse_transform(kmeans_model.cluster_centers_).round(2).tolist()
}
