import numpy as np


# sigmoid activation function (used for binary classification)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# sigmoid derivative
def sigmoid_derivative(y):
    return y * (1 - y)


# squared error loss function
def squared_error(y, y_hat):
    return 0.5 * np.sum(np.power(y - y_hat, 2))


# squared error derivative
def squared_error_derivative(predicted, actual):
    return predicted - actual


# MLP Training: Stochastic Gradient Descent
# single hidden layer
class MLP:
    def __init__(self, input, target, lr, wh, wo, bh, bo):
        self.x = input
        self.y = target
        self.lr = lr
        self.wh = wh
        self.wo = wo
        self.bh = bh
        self.bo = bo

    def forward_propagation(self):  # feed forward phase
        self.z = sigmoid(np.dot(self.wh.T, self.x) + self.bh)
        self.o = sigmoid(np.dot(self.wo.T, self.z) + self.bo)

    def backpropagation(self):  # backpropagation phase
        # net gradients
        delta_o = sigmoid_derivative(self.o) * squared_error_derivative(self.o, self.y)
        delta_h = sigmoid_derivative(self.z) * np.dot(self.wo, delta_o)
        # gradient descent for bias vectors
        grad_bo = delta_o
        self.bo = self.bo - self.lr * grad_bo
        grad_bh = delta_h
        self.bh = self.bh - self.lr * grad_bh
        # gradient descent for weight matrices
        grad_wo = np.dot(self.z, delta_o.T)
        self.wo = self.wo - self.lr * grad_wo
        grad_wh = np.dot(self.x, delta_h.T)
        self.wh = self.wh - self.lr * grad_wh

    def train(self, epochs):
        for i in range(epochs):
            self.forward_propagation()
            self.backpropagation()


# example 1
input = np.array([[0.35, 0.9]]).T
target = np.array([[0.5]]).T
wh = np.array([[0.1, 0.4], [0.8, 0.6]])
wo = np.array([[0.3, 0.9]]).T
bh = np.array([[0, 0]]).T
bo = np.array([[0]]).T
learning_rate = 1

# example 2
# input = np.array([[1, 0, 1]]).T
# target = np.array([[1]]).T
# wh = np.array([[0.2, -0.3], [0.4, 0.1], [-0.5, 0.2]])
# wo = np.array([[-0.3, -0.2]]).T
# bh = np.array([[-0.4, 0.2]]).T
# bo = np.array([[0.1]]).T
# learning_rate = 0.9

model = MLP(input, target, learning_rate, wh, wo, bh, bo)
model.train(1)
# print(model.o)
# print(model.z)
# print(model.wh)
# print(model.wo)
# print(model.bh)
# print(model.bo)
