class Neuron:
    def __init__(self, id, threshold=1.0):
        self.id = id
        self.potential = 0.0
        self.threshold = threshold
        self.fired = False

    def integrate(self, input_value):
        self.potential += input_value
        if self.potential >= self.threshold:
            self.fired = True
            self.potential = 0.0
        else:
            self.fired = False

    def reset(self):
        self.potential = 0.0
        self.fired = False
