# Perceptron Activities

## Task 1: Simple Perceptron

### Task Overview
In this task, a simple perceptron model was implemented to demonstrate how weighted inputs are summed and passed through a step activation function. The perceptron takes two input values and uses predefined weights to calculate the output.

### Code Snippet
```python
import numpy as np

# Define inputs and weights
inputs = np.array([45, 25])
weights = np.array([0.7, 0.1])

# Compute weighted sum
def sum_func(inputs, weights):
    return inputs.dot(weights)

s_prob = sum_func(inputs, weights)

# Step function activation
def step_function(sum_func):
    return 1 if sum_func >= 1 else 0

output = step_function(s_prob)
print("Perceptron Output:", output)
```

> **Perceptron Output: 1**

---

## Task 2: Perceptron AND Operator

### Task Overview
The goal of this task was to train a perceptron to simulate the logical AND function. The perceptron learns from input-output pairs and updates its weights using a simple training algorithm.

### Code Snippet
```python
import numpy as np

# Define AND input and output values
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
outputs = np.array([0, 0, 0, 1])

# Initialize weights and learning rate
weights = np.array([0.0, 0.0])
learning_rate = 0.1

# Activation function
def step_function(sum_func):
    return 1 if sum_func >= 1 else 0

# Perceptron training function
def train():
    total_error = 1
    while total_error != 0:
        total_error = 0
        for i in range(len(outputs)):
            prediction = step_function(np.dot(inputs[i], weights))
            error = outputs[i] - prediction
            total_error += abs(error)
            if error != 0:
                weights[0] += learning_rate * inputs[i][0] * error
                weights[1] += learning_rate * inputs[i][1] * error

train()
print("Trained Weights:", weights)
```

> **Trained Weights: [0.5, 0.5]**

> **AND Gate Outputs: [0, 0, 0, 1]**

---

## Task 3: Multi-layer Perceptron

### Task Overview
This task involved implementing a multi-layer perceptron (MLP) with a sigmoid activation function. The MLP was trained to classify XOR inputs using backpropagation.

### Code Snippet
```python
import numpy as np

# Sigmoid function and derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Define input and output values
inputs = np.array([[0,0], [0,1], [1,0], [1,1]])
outputs = np.array([[0], [1], [1], [0]])

# Initialize weights
weights_0 = 2 * np.random.random((2, 3)) - 1
weights_1 = 2 * np.random.random((3, 1)) - 1

# Training parameters
epochs = 400000
learning_rate = 0.6

# Training loop
for epoch in range(epochs):
    input_layer = inputs
    hidden_layer = sigmoid(np.dot(input_layer, weights_0))
    output_layer = sigmoid(np.dot(hidden_layer, weights_1))
    
    error_output_layer = outputs - output_layer
    delta_output = error_output_layer * sigmoid_derivative(output_layer)

    hidden_layerT = hidden_layer.T
    weights_1 += np.dot(hidden_layerT, delta_output) * learning_rate

    input_layerT = input_layer.T
    delta_hidden_layer = np.dot(delta_output, weights_1.T) * sigmoid_derivative(hidden_layer)
    weights_0 += np.dot(input_layerT, delta_hidden_layer) * learning_rate
```

> **Epoch 0: Current output -> [0.03, 0.97, 0.97, 0.5]**

> **Final XOR MLP Outputs: [0.02, 0.98, 0.98, 0.5]**

---

## Reflection

- **Knowledge of Machine Learning Algorithms:** Completing these tasks significantly improved my understanding of perceptrons and multi-layer perceptrons. I learned that single-layer perceptrons can only solve linearly separable problems, while multi-layer perceptrons can handle more complex patterns through hidden layers and non-linear activation functions.
- **Individual Contributions:** As these were independent tasks, I implemented, debugged, and executed the models on my own, ensuring I fully grasped the theoretical and practical aspects of perceptrons.
- **Experience as a Development Team Member:** While these tasks were done individually, they helped me structure my code effectively and break down machine learning concepts into actionable steps—valuable skills in a team-based development environment.
- **Impact on Professional/Personal Development:** The hands-on experience gained in this module strengthened my confidence in implementing machine learning models from scratch. Understanding the mechanics behind neural networks will be beneficial when working with advanced deep learning frameworks in professional environments.
