import mido

from app.midi.midi_handler import MidiHandler
from app.utils.mapper import NoteMapper
from app.gui.gui import PympeFrontend
import tkinter as tk

def main():

    output = mido.open_output('pympe', virtual=True)
    mapper = NoteMapper(output)
    midi = MidiHandler('Arturia KeyStep 37 MIDI 1', output, mapper)

    root = tk.Tk()

    PympeFrontend(root).pack(side="top", fill="both", expand=True)

    root.mainloop()

    midi.port.close()
    midi.output.close()

if __name__ == "__main__":
    main()
