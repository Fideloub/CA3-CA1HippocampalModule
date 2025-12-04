from .neurons import Neuron
from .synapses import Synapse

class CA3CA1Network:
    def __init__(self, n_ca3=100, n_ca1=100):
        self.ca3 = [Neuron(i) for i in range(n_ca3)]
        self.ca1 = [Neuron(i) for i in range(n_ca1)]
        self.synapses = []

    def connect(self):
        import random
        for pre in self.ca3:
            for post in self.ca1:
                self.synapses.append(Synapse(pre, post, weight=random.uniform(0,1)))

    def step(self):
        for s in self.synapses:
            delta = s.propagate()
            s.post.integrate(delta)
