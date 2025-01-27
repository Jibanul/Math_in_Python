import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment

def compute_optimal_transport(cost_matrix):
    """
    Solves the Optimal Transport problem using the Hungarian algorithm.

    Parameters:
        cost_matrix (np.ndarray): The cost matrix where cost_matrix[i, j] is the cost
                                  of moving mass from distribution i to distribution j.

    Returns:
        row_indices (np.ndarray): Optimal row indices.
        col_indices (np.ndarray): Optimal column indices.
        total_cost (float): The total cost of the optimal transport.
    """
    row_indices, col_indices = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_indices, col_indices].sum()
    return row_indices, col_indices, total_cost

def normalize_distribution(distribution):
    """
    Normalizes a distribution to ensure it sums to 1.

    Parameters:
        distribution (np.ndarray): The input distribution.

    Returns:
        np.ndarray: The normalized distribution.
    """
    return distribution / np.sum(distribution)

# Matching Two 1D Distributions
np.random.seed(42)

# Generate two distributions; discrete probability masses
source = np.array([0.1, 0.2, 0.4, 0.3])
target = np.array([0.3, 0.1, 0.4, 0.2])

# Normalize the distributions
source = normalize_distribution(source)
target = normalize_distribution(target)

# Generate a cost matrix (Euclidean distance)
n = len(source)
cost_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        cost_matrix[i, j] = abs(i - j)  # Distance metric

# Compute Optimal Transport
row_indices, col_indices, total_cost = compute_optimal_transport(cost_matrix)

# Plot the result
plt.figure(figsize=(8, 6))
plt.scatter(range(len(source)), source, label='Source Distribution', color='blue', s=100)
plt.scatter(range(len(target)), target, label='Target Distribution', color='red', s=100)
for r, c in zip(row_indices, col_indices):
    plt.plot([r, c], [source[r], target[c]], 'k--')
plt.title('Optimal Transport between Two Distributions')
plt.xlabel('Index')
plt.ylabel('Probability Mass')
plt.legend()
plt.grid()
plt.show()

# Print the results
print("Optimal Transport Results:")
print(f"Row Indices (Source): {row_indices}")
print(f"Column Indices (Target): {col_indices}")
print(f"Total Transport Cost: {total_cost}")