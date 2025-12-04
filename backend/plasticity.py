class STDP:
    def apply(self, synapse, pre_fired, post_fired, lr=0.01):
        if pre_fired and post_fired:
            synapse.weight += lr
        elif pre_fired and not post_fired:
            synapse.weight -= lr*0.5
        synapse.weight = max(0, synapse.weight)
