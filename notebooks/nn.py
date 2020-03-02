import numpy as np


class ReLULayer:
    def __init__(self, input_dim, output_dim):

        self.weights = np.zeros(shape=(input_dim, output_dim))
        self.bias = np.zeros(shape=(1, output_dim))
        self.inputs = np.zeros(shape=(1, output_dim))
        self.activation = np.zeros(shape=(1, output_dim))
        self.delta = np.zeros(shape=(1, output_dim))
        self.input_dim = input_dim
        self.output_dim = output_dim

        self.sigma = lambda x: np.maximum(x, 0)
        self.sigmaprime = lambda x: np.maximum(1, 0)
        return

    def initialize(self):
        self.weights = np.random.uniform(
            -np.sqrt(self.output_dim), np.sqrt(self.output_dim), size=self.weights.shape
        )
        self.bias = np.random.uniform(
            -np.sqrt(self.output_dim), np.sqrt(self.output_dim), size=self.bias.shape
        )

    def forward(self, x):
        self.inputs = np.dot(x, self.weights) + self.bias
        self.activation = self.sigma(self.inputs)
        return self.activation



