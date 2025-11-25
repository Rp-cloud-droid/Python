import matplotlib.pyplot as plt

import numpy as np

# Creating dataset

np.random.seed(23685752)

N_points = 10000

n_bins = 20

# Creating distribution

x = np.random.randn(N_points)

y = .8 ** x + np.random.randn(10000) + 25 # Not used, but kept for completeness

# Creating histogram

fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

axs.hist(x, bins=n_bins, color='skyblue', edgecolor='black')

# Labels

axs.set_title("Histogram of Normal Distribution")

axs.set_xlabel("x values")

axs.set_ylabel("Frequency")

plt.show()