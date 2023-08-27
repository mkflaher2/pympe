import time
import numpy as np
import pyaudio as pa

class AudioOut:
    def __init__(self, ch=1, fs=44100):
        p = pa.PyAudio()
        self.channel = ch
        self.fs = fs
        self.stream = p.open(format=pa.paFloat32, channels=self.channel, rate=self.fs, output=True)

    def enable(self, synth):
        while True:
            # TODO: create a buffer
            output_buffer = synth.generate()
            while output_buffer:
                self.stream.write(output_buffer.pop())
