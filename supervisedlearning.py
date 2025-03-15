import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#generate some example data
data = np.random.rand(100, 10) # 100 samples, 10 features

#perform PCF for dimensionality reduction
reduced_data = PCA(n_components=2).fit_transform(data)

#determine the optimal number of clusters using the elbow method
inertia_values = []
possible_clusters = range(1, 11)
for k in possible_clusters:
    kmeans = KMeans(init="k-means++", n_clusters=k, n_init=4)
    kmeans.fit(reduced_data)
    inertia_values.append(kmeans.inertia_)

#choose the optimal number of clisters (e.g., where the curve starts to flatten)
optimal_clusters = 3 # replace the clister number with the one you find optimal

#perform KMeans clustering with the chosen number of clusters
kmeans = KMeans(init="k-means++", n_clusters=optimal_clusters, n_init=4)
kmeans.fit(reduced_data)

#Plot both images side by side
plt.figure(figsize=(12, 6))

#elobow curve plot
plt.subplot(1, 2, 1)
plt.plot(possible_clusters, inertia_values, marker='o')
plt.title('Elbow Method for optimal K')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia(sum of squared distances)')

# K-means clustering result plot
plt.subplot(1, 2, 2)
h = 0.02
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.imshow(Z, interpolation="nearest", extent=(xx.min(), xx.max(), yy.min(), yy.max()), cmap=plt.cm.Paired, aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=169, linewidths=3, color='w', zorder=10)
plt.title("K-means clustering result (PCA-reduced data)\n"
          "Centroids are marked with white cross")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

#adjust layout for better visualization
plt.tight_layout()
plt.show()