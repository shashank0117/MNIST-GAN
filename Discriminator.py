import torch
import torch.nn as nn
import torch.nn.functional as F

class Discriminator(nn.Module):
    def __init__(self, input_size, hidden_dim, output_size):
        '''
        The constructor class for the Discriminator

        Arguments:
        - input_size : the number of input neurons
        - hidden_dim : the number of hidden neurons in the last layer
        - output_size : the number of output neurons
        '''
        
        # Define the class variables
        self.input_size = input_size
        self.hidden_dim = hidden_dim
        self.output_size = output_size

        # Define the required modules for this architecture
        self.fc1 = nn.Linear(self.input_size, self.hidden_dim*2)
        self.fc2 = nn.Linear(self.hidden_dim*2, self.hidden_dim*3)
        self.fc3 = nn.Linear(self.hidden_dim*3, self.hidden_dim)

        self.fc4 = nn.Linear(self.hidden_dim, self.output_size)

        self.dropout = nn.Dropout(0.3)

    def forward(self, x):
        '''
        This method defines the forward pass for the Discriminator module

        Arguments:
        - x : the input to the network

        Returns:
        - out : the output of the network
        '''
        # Flatten the images
        x = x.view(-1, 784)

        # Forward pass
        x = F.leaky_relu(self.fc1(x), 0.2)
        x = self.dropout(x)

        x = F.leaky_relu(self.fc2(x), 0.2)
        x = self.dropout(x)

        x = F.leaky_relu(self.fc3(x), 0.2)
        x = self.dropout(x)

        out = self.fc4(x)

        return out
