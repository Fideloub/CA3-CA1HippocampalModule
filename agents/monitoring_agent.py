class MonitoringAgent:
    def process(self, input_data, network):
        fired = [n.id for n in network.ca1 if n.fired]
        print('CA1 fired:', fired)
