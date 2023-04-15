import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Define the dissimilarity matrix
D = np.array([[0, 0.9, 1.43, 0.81, 0.87, 1.32, 0.1],
              [0.9, 0, 1.15, 0.23, 0.15, 1.1, 0.81],
              [1.43, 1.15, 0, 1.45, 1.21, 0.2, 1.67],
              [0.81, 0.23, 1.45, 0, 0.25, 1.2, 0.85],
              [0.87, 0.15, 1.21, 0.25, 0, 1.13, 0.8],
              [1.32, 1.1, 0.2, 1.2, 1.13, 0, 1.23],
              [0.1, 0.81, 1.67, 0.85, 0.8, 1.23, 0]])

# Perform hierarchical clustering with single linkage
Z = linkage(D, method='single')
print(Z)
# Plot dendrogram
plt.figure(figsize=(10, 5))
plt.title('Dendrogram')
plt.xlabel('Node')
plt.ylabel('Distance')
dendrogram(Z, leaf_rotation=90, leaf_font_size=8)
plt.show()
