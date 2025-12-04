class Orchestrator:
    def __init__(self, network, agents):
        self.network = network
        self.agents = agents

    def run_cycle(self, input_data):
        for agent in self.agents:
            agent.process(input_data, self.network)
