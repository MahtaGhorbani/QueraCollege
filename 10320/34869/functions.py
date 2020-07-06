from sklearn.manifold import TSNE

def tsne(x):
    x_tsne = TSNE(n_components=2, init='pca', random_state=0).fit_transform(x)
    return x_tsne