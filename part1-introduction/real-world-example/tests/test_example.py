import numpy as np

from sklearn.linear_model import LinearRegression


def test_example():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
    y = np.array([1, 2, 3, 4])

    model = LinearRegression()
    model.fit(X, y)

    pred = model.predict(X)
    assert len(pred) > 0


def test_example_custom_scaling():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]], dtype=np.float64)
    y = np.array([1, 2, 3, 4])

    model = LinearRegression(custom_scaling=-1.5)
    model.fit(X, y)

    pred = model.predict(X)
    assert len(pred) > 0


def test_example_custom_scaling_copy_x_works():
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]], dtype=np.float64)
    y = np.array([1, 2, 3, 4])

    model = LinearRegression(custom_scaling=-1.5, copy_X=True)
    model.fit(X, y)

    pred = model.predict(X)
    new_X = X

    assert (new_X[0] == [1, 1]).all()
