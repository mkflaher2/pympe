import numpy as np

class BasicOsc:
    def __init__(self, fs=44100):
        self.fs = fs

    def generate(self, f=440):
        samples = (np.sin(2 * np.pi * np.arange(self.fs) * f / self.fs)).astype(np.float32)
        return samples

