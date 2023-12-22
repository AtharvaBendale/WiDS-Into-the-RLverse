## Goal

Implement the algorithms you have learnt to find optimal policies as well as the value functions for the given MDPs (Value Iteration - a special case of Policy Iteration).

## Test MDPs format

You are given two MDPs to test on in the [MDPs](./MDPs) folder. Both are continuing MDPs. They follow the format:

```html
states <number of states>
actions <number of actions>
tran <initial state> <action taken> <final state> <reward> <transition probability>
...all the other transitions...
tran <initial state> <action taken> <final state> <reward> <transition probability>
gamma  <discount rate>
```

The solutions to the MDPs are contained in the same directory. You can use these solutions to verify the output of your MDP planner. The format:

```html
<optimal value function for first state> <optimal action for first state>
...one entry for each state...
<optimal value function for last state> <optimal action for last state>
```

## A Rough Outline

- The first step would be parse through the MDP files and store them into suitable data structures in python.
- Next, you have to implement the algorithms and store their results in the code.
- Finally, you have to store the results generated in an output text file so that you verify the solution.
- You can refer to the solution text files inside the [MDPs](./MDPs) folder for checking your program correctness but note that the assignment will be graded on some other MDP.

Note : You can submit any one of the file type .py or .ipynb as you like

Note : This assignment needs you to access the given text files, and if you cannot use python on your own system and are planning to use Google Colab and not sure how to access text files from colab please DM me for instructions.

You can now apply the same algorithm and get the optimal policies and values for the multi-armed bandits you constructed last week.
