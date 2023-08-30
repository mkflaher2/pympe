import mido

from typing import List

class NoteMapper:
    def __init__(self, output):
        self.mappings = {}
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

    def add_mapping(self, notes: List[int]) -> bool:
        if notes[0] in self.mappings.keys():
            if self.mappings[notes[0]] == notes[1]:
                del self.mappings[notes[0]]
                print("deleted mapping {} -> {}".format(notes[0], notes[1]))
                return False
        self.mappings[notes[0]] = notes[1]
        print("added mapping {} -> {}".format(notes[0], notes[1]))
        return True

