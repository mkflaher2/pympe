from app.midi.midi_handler import MidiHandler
from app.synth.synth import Synth
from app.audio.audio import AudioOut

def main():
     # synth = Synth()
     midi = MidiHandler('Arturia KeyStep 37 MIDI 1')
     # audio = AudioOut()
     # audio.enable(synth)

     while True:
         pass
     midi.port.close()
     midi.output.close()

if __name__ == "__main__":
    main()
