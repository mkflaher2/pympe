import time
import numpy as np
import pyaudio

p = pyaudio.PyAudio()

volume = 0.5
fs = 44100
duration = 5.0
f = 440.0

samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

output_bytes = (volume * samples).tobytes()

stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)

start_time = time.time()
stream.write(output_bytes)

stream.stop_stream()
stream.close()

p.terminate()
