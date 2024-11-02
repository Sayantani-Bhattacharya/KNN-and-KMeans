from k_nearest_neighbors import knn, generate_confision_matrix
import pytest
from starter import read_data, show


def test_knn():
    train = [
        [1, [1, 0, 1, 0]],
        [0, [0, 1, 0, 1]],
        [1, [1, 1, 1, 1]],
        [0, [1, 0, 0, 1]],
        [0, [1, 0, 1, 1]],
        [0, [0, 1, 1, 0]],
        [1, [1, 0, 0, 0]],
        [1, [1, 0, 1, 1]],
        [0, [1, 1, 0, 1]],
        [1, [0, 1, 1, 1]],
        [1, [1, 0, 1, 0]],
        [0, [0, 1, 1, 0]]
    ]
    query = [[1, [1, 0, 1, 0]], [1, [1, 1, 1, 1]], [0, [0, 0, 0, 1]]]
    assert knn(train=train, query=query, metric='euclidean', k=3) == [1, 1, 0]
    assert knn(train=train, query=query, metric='cosim', k=3) == [0, 1, 1]


def test_confusion_matrix():
    train = [
            [1, [1, 0, 1, 0]],
            [0, [0, 1, 0, 1]],
            [1, [1, 1, 1, 1]],
            [0, [1, 0, 0, 1]],
            [0, [1, 0, 1, 1]],
            [0, [0, 1, 1, 0]],
            [1, [1, 0, 0, 0]],
            [1, [1, 0, 1, 1]],
            [0, [1, 1, 0, 1]],
            [1, [0, 1, 1, 1]],
            [1, [1, 0, 1, 0]],
            [0, [0, 1, 1, 0]]
    ]
    query = [[1, [1, 0, 1, 0]], [1, [1, 1, 1, 1]], [0, [0, 0, 0, 1]]]
    predicted_labels = knn(train=train, query=query, metric='euclidean', k=3)
    expected_labels = [q[0] for q in query]
    confusion_matrix = generate_confision_matrix(
        predicted_labels, expected_labels)
    assert confusion_matrix.shape == (2, 2)
    assert confusion_matrix[0][0] == 1
    assert confusion_matrix[0][1] == 0
    assert confusion_matrix[1][0] == 0
    assert confusion_matrix[1][1] == 2
