from sklearn.preprocessing import MinMaxScaler


def test_with_log_scaling():
    data = [[1, 2], [0.5, 6], [1, 10], [1, 18]]

    scaler = MinMaxScaler(
        log_scaling=True
    )
    scaler.fit(data)
    data_scaled = scaler.transform(data)

    assert data_scaled.min() == 0.0, data_scaled.min()
    assert data_scaled.max() == 1.0, data_scaled.max()
