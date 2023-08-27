import time
import numpy as np

class Synth:
    def __init__(self, fs=44100, n_samples=256, buffer=100):
        self.fs = fs
        self.f = 440
        self.gate = 0
        self.n_samples = n_samples
        self.buffer = buffer
        self.chunk_number = 0
        self.velocity = 64

    # TODO: implement scala support
    def note_freq(self, n):
        return 440 * 2 ** ((n-69)/12)

    def parse_message(self, message):
        if message.type == "note_on":
            self.gate += 1
            self.f = self.note_freq(message.note)
            self.velocity = message.velocity
        if message.type == "note_off":
            self.gate -=1

    def generate(self):
        gate_mult = 1 if self.gate else 0
        volume = float(self.velocity)/127
        offset_phase = 2 * np.pi * self.n_samples * self.chunk_number / self.fs
        buffer_chunks = []
        for n in range(self.buffer):
            chunk = (gate_mult * volume * np.sin(2 * np.pi * np.arange(self.n_samples) * self.f / self.fs + offset_phase)).astype(np.float32).tobytes()
            buffer_chunks.append(chunk)
            self.chunk_number = (self.chunk_number + 1) % self.buffer
        return buffer_chunks
