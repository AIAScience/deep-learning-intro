import sklearn.neural_network
import numpy as np

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

model = sklearn.neural_network.MLPClassifier(
    activation="relu", max_iter=10000, hidden_layer_sizes=(8, 2)
)
model.fit(x, y)

print("score:", model.score(x, y))
print("predictions:", model.predict(x))
print("expected:", np.array([0, 1, 1, 0]))
