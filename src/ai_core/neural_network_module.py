# neural_network_module.py
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

class NeuralNetworkModule:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.model = self._create_model()

    def _create_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(self.hidden_dim, activation='relu', input_shape=(self.input_dim,)),
            tf.keras.layers.Dense(self.hidden_dim, activation='relu'),
            tf.keras.layers.Dense(self.output_dim, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=10):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        self.model.fit(X_train_scaled, y_train, epochs=epochs)

    def predict(self, X_test):
        scaler = StandardScaler()
        X_test_scaled = scaler.transform(X_test)
        return self.model.predict(X_test_scaled)

    def evaluate(self, X_test, y_test):
        scaler = StandardScaler()
        X_test_scaled = scaler.transform(X_test)
        return self.model.evaluate(X_test_scaled, y_test)
