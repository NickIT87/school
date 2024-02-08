from sklearn import datasets
import matplotlib.pyplot as plt


iris = datasets.load_iris()

# _, ax = plt.subplots()
# scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
# ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
# _ = ax.legend(
#     scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
# )

# unused but required import for doing 3d projections with matplotlib < 3.2
# import mpl_toolkits.mplot3d  # noqa: F401

from sklearn.decomposition import PCA

fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=iris.target,
    s=40,
)

ax.set_title("First three PCA dimensions")
ax.set_xlabel("1st Eigenvector")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("2nd Eigenvector")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("3rd Eigenvector")
ax.zaxis.set_ticklabels([])

plt.show()

