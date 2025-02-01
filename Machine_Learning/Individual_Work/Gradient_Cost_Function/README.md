# Task Overview

This task involves running the `gradient_descent_cost_function.ipynb` tutorial to observe how the cost function decreases with changes in iteration count and learning rate. The goal is to understand how gradient descent converges and how parameter tuning impacts efficiency.

# Code Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# Gradient descent function with modified parameters
def gradient_descent(x, y, iterations=100, learning_rate=0.08):
    m_curr = b_curr = 0
    n = len(x)
    cost_values = []

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)])
        md = -(2/n) * sum(x * (y - y_predicted))
        bd = -(2/n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        cost_values.append(cost)

    return cost_values

# Define data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

# Run gradient descent with different configurations
cost_1 = gradient_descent(x, y, iterations=100, learning_rate=0.08)
cost_2 = gradient_descent(x, y, iterations=500, learning_rate=0.08)
cost_3 = gradient_descent(x, y, iterations=100, learning_rate=0.01)

# Plot cost reduction over iterations
plt.figure(figsize=(8, 5))
plt.plot(cost_1, label="100 Iterations, LR=0.08", linestyle='-', linewidth=2)
plt.plot(cost_2, label="500 Iterations, LR=0.08", linestyle='--', linewidth=2)
plt.plot(cost_3, label="100 Iterations, LR=0.01", linestyle='-.', linewidth=2)
plt.xlabel("Iterations")
plt.ylabel("Cost Function Value")
plt.title("Gradient Descent: Cost Function Reduction")
plt.legend()
plt.yscale("log")  # Use a logarithmic scale for better readability
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
```

![image](https://github.com/user-attachments/assets/1aefa27e-3961-4ddd-9957-9a5987a907cb)

# Observations

The cost function consistently decreases over iterations, confirming the expected behavior of gradient descent:

- **With 100 iterations and a learning rate of 0.08**: Cost reduces steadily and converges.
- **With 500 iterations and the same learning rate**: Further reduction is observed, showing prolonged training improves convergence.
- **With 100 iterations but a smaller learning rate (0.01)**: Cost decreases much more slowly, indicating that too small a learning rate slows convergence significantly.

# Reflection

### Understanding Machine Learning Algorithms
This task reinforced my understanding of gradient descent and the importance of hyperparameter tuning. Experimenting with different iteration values and learning rates provided insights into how these factors influence convergence speed and stability.

### Individual Contribution
This was an independent exercise where I executed, modified, and evaluated the gradient descent algorithm. The hands-on approach strengthened my understanding of theoretical concepts and their practical applications.

### Experience as a Learner
Working on this task helped me better grasp the importance of debugging machine learning models. Observing cost reduction visually made it easier to understand the impact of hyperparameters.

### Impact on Professional Development
This exercise directly improves my ability to fine-tune machine learning models. Understanding gradient descent's behavior is crucial for optimising models in real-world scenarios, making this task highly valuable for my future career.
