import mido

from app.synth.synth import Synth
from app.utils.mapper import NoteMapper

class MidiHandler:
    def __init__(self, device):
        self.port = mido.open_input(device, callback=self.process_message)
        self.output = mido.open_output('pympe', virtual=True)
        self.notes = [] # list of messages with all midi info
        self.channels = [] # list of channels in use
        self.mapper = NoteMapper(self.output)

    def process_message(self, message):

        if message.type == "note_on":
            # self.notes.append(message)

            for i in range(1,16):
                if i not in self.channels:
                    self.channels.append(i)
                    message_out = message.copy(channel=i)
                    self.output.send(message_out)
                    self.notes.append(message_out)
                    break

        elif message.type == "note_off":

            # TODO: make this less ugly

            for note in self.notes:
                if message.note == note.note:
                    message_out = message.copy(channel=note.channel)
                    self.output.send(message_out)
                    self.channels.remove(note.channel)
                    self.notes.remove(note)
                    break

        elif message.type == "control_change" and message.control==1:
            self.mapper.bend(message, self.notes)

        else:
            self.output.send(message)


        print(message)
        print(self.notes)
