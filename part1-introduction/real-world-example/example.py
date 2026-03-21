import matplotlib.pyplot as plt

from sklearn.datasets import load_wine

import numpy as np
from sklearn.preprocessing import MinMaxScaler


if __name__ == '__main__':
    wine_dataset = load_wine()["data"]
    alcohol, proline = wine_dataset[:, [0, 12]].T

    plt.scatter(alcohol, proline)
    plt.title("Alcohol vs. proline, raw data")
    plt.xlabel("Alcohol")
    plt.ylabel("Proline")
    plt.show()

    scaler = MinMaxScaler(
        log_scaling=True
    )
    wine_features = np.vstack((alcohol, proline)).T
    scaler.fit(wine_features)
    alcohol_scaled, proline_scaled = scaler.transform(wine_features).T

    plt.scatter(alcohol_scaled, proline_scaled)
    plt.title("Alcohol vs. proline, scaled data")
    plt.xlabel("Alcohol")
    plt.ylabel("Proline")
    plt.show()
