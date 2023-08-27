import mido

from typing import List

class NoteMapper:
    def __init__(self, output):
        self.mappings = {60: 67, 64: 62, 67: 71}
        self.output = output

    def bend(self, message, notes):
        for note in notes:
            if note.note in self.mappings.keys():
                message_out = mido.Message(
                    'pitchwheel',
                    channel=note.channel,
                    pitch=int((self.mappings[note.note] - note.note) * (8192 * message.value/127) / 48),
                    time=0
                )
                self.output.send(message_out)

