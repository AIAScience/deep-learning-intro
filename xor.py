import numpy as np
from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import SGD

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(10, input_dim=2, activation="tanh"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer=SGD(lr=0.1))

model.fit(X, y, batch_size=1, epochs=1000, verbose=0)

print(model.predict(X))
