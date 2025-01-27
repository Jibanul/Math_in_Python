import numpy as np
import matplotlib.pyplot as plt

# Data (X, y)
# 100 random data points
np.random.seed(123)
X = np.random.rand(100, 1)
y = 3 * X + 2 + 0.5 * np.random.randn(100, 1)  # Linear relationship between x,y with some noise

# Add a column of ones to X for the intercept term
X_ = np.hstack([np.ones_like(X), X])

# Compute the Least Squares solution (normal equation)
theta = np.linalg.inv(X_.T @ X_) @ X_.T @ y

# Predicted values using the model
y_pred = X_ @ theta

# Plot the results
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Least squares fit')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Least Squares Approximation')
plt.legend()
plt.show()

# Print the estimated parameters (intercept and slope)
print(f"Intercept: {theta[0][0]}, Slope: {theta[1][0]}")