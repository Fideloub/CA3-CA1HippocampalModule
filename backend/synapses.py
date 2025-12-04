class Synapse:
    def __init__(self, pre, post, weight):
        self.pre = pre
        self.post = post
        self.weight = weight

    def propagate(self):
        if self.pre.fired:
            return self.weight
        return 0.0
