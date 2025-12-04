class InputAgent:
    def process(self, input_data, network):
        for neuron, value in zip(network.ca3, input_data):
            neuron.integrate(value)
