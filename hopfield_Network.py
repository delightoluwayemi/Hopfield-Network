import numpy as np
import random as rd

class Hopfield_Network:

    def __init__(self, pattern_size, input): 
        self.pattern_size = pattern_size #no of nodes in a pattern
        self.patterns_array = np.array(input) #memory of network
        self.weight = np.zeros((pattern_size, pattern_size))
        self.state = np.array(pattern_size) #current configuration of network

        self.pattern_count = len(input) #no of patterns in the network
        self.energy = 0
        
    def train_network(self) :
        for index in self.patterns_array:
            self.weight= self.weight + (np.outer(index,index))/self.pattern_size
            
        np.fill_diagonal(self.weight, 0) #set diagonal of the matrix to zero

    def updating_rule(self, n):
        return 1 if (n>0) else -1

    def update_network_state(self, state):
        self.state = state
        final_state = False
        while final_state == False:
            node = rd.randint(0, len(self.state)-1)
            activation = np.dot(self.state, self.weight[:, node])
            self.state[node] = self.updating_rule(activation) #new state of the neuron under consideration
            self.update_energy()
            for index in self.patterns_array:
                if np.all(self.state == index):
                    final_state = True
        return self.state
    
    def get_pattern_count(self):
        return self.pattern_count
    
    def get_node_count(self):
        return self.pattern_size
    
    def update_energy(self):
        self.energy = -0.5* np.dot(np.dot(np.transpose(self.state), self.weight), self.state)

