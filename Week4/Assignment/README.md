## Solving CartPole with DQNs

You will use DQNs as function approximator in this assignment to find optimal policies for any CartPole state.
<br>
We use DQN to approximate the Q(s, a) or V(s) functions, in this assignment you will use it for Q(s, a). Inn DQNs we generate targets from an stationery model (or target model) and use it to train an online model, later we update the stationery model with the updated online model and carry out this process several times.

Please take a look at this [documentation](https://gymnasium.farama.org/environments/classic_control/cart_pole/) for details about the OpenGym CartPole environment.

The file DQN.py contains the neural network class of DQN and the cartpole.ipynb notebook contains the RL agent class.

## Instructions for model.py

You have to make a DQN model which approximates the value of Q(s, a) given s & a

You must be familiar with how we make a class for any neural network, the class given below has the same format and you have to implement a neural network using linear layers and ReLU activations which takes the states and action as input and gives __Q(s, a)__ as output,
- You have to make a DQN class which accepts appropriate input and gives appropriate output and has a train functionality
- The constructor '__init__' should initialize all the layers for the neural network as class variables
- The __forward()__ function will accept any numpy array of torch tensor of appropriate size and output the value obtained after passing it through all layers
- The __train_instance()__ function accepts a training dataset which is of CustomDataset datatype and represents the replay buffer, and these will be used for training the model for some fixed epochs (iterations). You should use the imported DataLoader class to sample random batches from the given training dataset while model training.
- The __save_model()__ function has already bee implemented and you should use it save your model
- You should declare the layers of the Neural Net as class variables (Allows us to use optimizer easily)

Now some recommendaions:
- PLEASE DO USE optimizer.
- You should declare the optimizer and the loss function in the constructor (__init__) itself as class variables, the optimizer takes parameters and learning rate as input, passing self.parameters() as params to the optimizer passes all the layers in the class (which are declared as class variables) as input by default. Adam optimizer is prefered for optimizer and Huberloss is prefered for loss function in this case. For ex:
```     
    self.optimizer = optim.Adam(params = self.parameters(), lr = 0.001)
   
    self.loss_func = nn.HuberLoss(delta = 1)
```
- There can be a lots of different architectures for the neural net layers (it generally doesn't matter much for cartpole as it is a much easy-to-solve environment), but here is one which I've used (not the best, but it works):

Input Size  |  Layer1 size  |  Layer2 size  |  Layer3 size  |  Output Layer Size

     5       5x64      64x16     16x8      8x1 (Of Course!)

## Instructions for cartpole.ipynb
Instructions are inside the notebook itself

All the best with the assignment and please ask any theory or implementation doubt. Please do ask for clarifications if you are confused about anything regarding the assignment.