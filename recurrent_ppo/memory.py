import random
from collections import namedtuple

# Taken from
# https://github.com/pytorch/tutorials/blob/master/Reinforcement%20(Q-)Learning%20with%20PyTorch.ipynb

Transition = namedtuple('Transition', ('history', 'policy', 'value', 'action', 'reward', 'mask', 'hx', 'cx'))


class Memory(object):
    def __init__(self):
        self.memory = []

    def push(self, history, policy, value, action, reward, mask, hx, cx):
        self.memory.append(Transition(history, policy, value, action, reward, mask, hx, cx))

    def sample(self):
        transitions = self.memory
        batch = Transition(*zip(*transitions))
        return batch


    def __len__(self):
        return len(self.memory)