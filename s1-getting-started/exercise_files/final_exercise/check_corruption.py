import numpy as np
from numpy import load
import matplotlib.pyplot as plt
import torch

data = load('/Users/erlahrafnkelsdottir/Documents/dtu-02476-mlops/s1-getting-started/exercise_files/final_exercise/corruptmnist/train_0.npz')
image = data['images']

plt.imshow(image[1])
plt.colorbar()
plt.plot(block=True) # Plot always disappears...