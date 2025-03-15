import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import manifold
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition

#load MNIST dataset, i already it in csv format

data = pd.read_csv('mnist_train.csv')

#separate the labels from the data
labels = data['label']
data = data.drop('label', axis=1)

#extracting top 10000 data points
df_data = data.head(10000)
df_labels = labels.head(10000)
pixel_df = StandardScaler().fit_transform(df_data)

sample_data = pixel_df
pca= decomposition.PCA(n_components=2, random_state=42)
pca_data = pca.fit_transform(sample_data)

# Plotting PCA in two dimensions
# attaching the lbel for each 2-d data point
pca_data = np.column_stack((pca_data, df_labels))
# creating a dataframe for the pca data
pca_df = pd.DataFrame(data=pca_data, columns=['X', 'Y', 'labels'])
sns.FacetGrid(pca_df, hue='labels', height=6).map(plt.scatter, 'X', 'Y').add_legend()
plt.show()

## Applying T-SNE
tsne = manifold.TSNE(n_components=2, random_state=42, verbose=2, n_iter=2000)
transformed_data = tsne.fit_transform(sample_data)

# Creation of new dataframe for plotting
tsne_df = pd.DataFrame(np.column_stack((transformed_data, df_labels)), columns=['X', 'Y', 'labels'])
tsne_df.loc[:, 'labels'] = tsne_df['labels'].astype(int)

# Plotting MNIST data in 2D
grid = sns.FacetGrid(tsne_df, hue='labels', height=8)
grid.map(plt.scatter, 'X', 'Y').add_legend()
plt.title('T-SNE MNIST Data')
plt.show()