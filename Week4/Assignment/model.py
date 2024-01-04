# Scroll down for instructions

import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        try:
            return self.data.shape[0]       # For np-array and tensors
        except:
            return len(self.data)           # For lists (Using np-array or tensors instead lists for storing data is highly recommended though)

    def __getitem__(self, index):
        sample = self.data[index]
        label = self.labels[index]
        return sample, label

'''
You have to make a DQN model which approximates the value of Q(s, a) given s & a

INSTRUCTIONS:
You must be familiar with how we make a class for any neural network, the class given below has the same format and you have to implement a neural network using linear layers and ReLU activations which takes the states and action as input and gives Q(s, a) as output,
- You have to make a DQN class which accepts appropriate input and gives appropriate output and has a train functionality
- The constructor '__init__' should initialize all the layers for the neural network as class variables
- The forward() function will accept any numpy array of torch tensor of appropriate size and output the value obtained after passing it through all layers
- The train_instance() function accepts a training dataset which is of CustomDataset datatype and represents the replay buffer, and these will be used for training the model for some fixed epochs (iterations). You should use the imported DataLoader class to sample random batches from the given training dataset while model training.
- The save_model() function has already bee implemented and you should use it save your model
- You should declare the layers of the Neural Net as class variables (Allows us to use optimizer easily)

Now some recommendaions:
- PLEASE DO USE optimizer.
- You should declare the optimizer and the loss function in the constructor (__init__) itself as class variables, the optimizer takes parameters and learning rate as input, passing self.parameters() as params to the optimizer passes all the layers in the class (which are declared as class variables) as input by default. Adam optimizer is prefered for optimizer and Huberloss is prefered for loss function in this case. For ex:
    self.optimizer = optim.Adam(params = self.parameters(), lr = 0.001)
    self.loss_func = nn.HuberLoss(delta = 1)
- There can be a lots of different architectures for the neural net layers (it generally doesn't matter much for cartpole as it is a much easy-to-solve environment), but here is one which I've used (not the best, but it works):
    Input Size  |  Layer1 size  |  Layer2 size  |  Layer3 size  |  Output Layer Size
         5             5x64           64x16           16x8           8x1 (Of Course!)

'''

class DQN(nn.Module):

    def __init__(self) -> None:
        super().__init__()
        # Code Here #

    def forward(self, x : np.ndarray | torch.Tensor) -> torch.Tensor:
        # Code Here #
        pass

    def train_instance(self, train_dataset : CustomDataset) -> None:
        # Code Here #
        pass

    def save_model(self, model_name : str):
        torch.save(self, model_name) # Saves the model with with the value of model_name as its name


