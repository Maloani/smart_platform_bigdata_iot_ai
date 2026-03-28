import numpy as np
from lstm_model import create_model

# Données simulées
X = np.random.rand(100, 10, 1)
y = np.random.rand(100, 1)

model = create_model()
model.fit(X, y, epochs=5)

model.save("model.h5")
print("Model saved")