import numpy as np
from keras.layers.core import Dense, Activation
from keras.models import Sequential
from keras.optimizers import SGD

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

model = Sequential()
model.add(Dense(8, input_dim=2))
model.add(Activation("tanh"))
model.add(Dense(1))
model.add(Activation("sigmoid"))

sgd = SGD(lr=0.1)
model.compile(loss="binary_crossentropy", optimizer=sgd)

model.fit(X, y, batch_size=1, epochs=500, verbose=0)

print(model.predict(X))
