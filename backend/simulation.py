class Simulation:
    def __init__(self, network):
        self.network = network

    def run(self, steps):
        for _ in range(steps):
            self.network.step()
