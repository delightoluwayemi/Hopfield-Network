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
            self.weight+= (np.outer(index,index))/self.pattern_size
            
        np.fill_diagonal(self.weight, 0) #set diagonal of the matrix to zero
        print ("The weight of the network is:")
        print (self.weight)

    def updating_rule(self, n):
        return 1 if (n>0) else -1

    def update_network_state(self, state):
        self.state = state
        index = rd.randint(0, len(self.state)-1)
        activation = np.dot(self.state, self.weight[:, index])
        self.state[index] = self.updating_rule(activation) #new state of the neuron under consideration
        print ("The state of the network is:")
        print (self.state )
        self.update_energy()
        print ("The energy of the network is:")
        print (self.energy )

    def get_pattern_count(self):
        return self.pattern_count
    
    def get_node_count(self):

        return self.pattern_size
    
    def update_energy(self):
        self.energy = -0.5* np.dot(np.dot(np.transpose(self.state), self.weight), self.state)

if __name__ == "__main__":

    input= [[1,-1,-1,1], [1,1,-1,-1]]
    state = [1,-1,1,-1]
    node_count = len(state)
    sample_net = Hopfield_Network(node_count, input)
    energy = sample_net.update_energy()
    sample_net.train_network()
    count = 5
    while (count >0):
        sample_net.update_network_state(state)
        count -=1

