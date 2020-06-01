import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#path="./kddcup.data"

def kmeans(path)
    kdd_data = pd.read_csv(path, header=None)

    kdd_data[1], protocols = pd.factorize(kdd_data[1])
    kdd_data[2], services = pd.factorize(kdd_data[2])
    kdd_data[3], flags    = pd.factorize(kdd_data[3])
    kdd_data[41], attacks = pd.factorize(kdd_data[41])
    #kdd_data.head()

    scaler = MinMaxScaler()
    data_transformed= scaler.fit_transform(kdd_data)

    error = []
    K = range(1,30)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(data_transformed)
        error.append(km.inertia_)

    plt.plot(K, error, 'ox-')
    plt.xlabel('number of clusters k')
    plt.ylabel('Inertia (sum of squared distances)')
    plt.title('Optimal k')
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = str(sys.argv[1])
    else:
        path = "./kddcup.data"

    kmeans(path)
