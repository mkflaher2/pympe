import tkinter as tk

import copy

from tkinter import ttk

from app.utils.mapper import NoteMapper

class PympeFrontend(tk.Frame):
    def __init__(self, parent, mapper, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        self.mapper = mapper

        self.octave_frame = tk.Frame(self)
        self.octave_frame.pack()

        self.note_pair = [-1, -1]

        octave_options = [0, 1, 2, 3, 4, 5, 6, 7]
        notes = range(25)
        key_colors = [
            'white',
            'black',
            'white',
            'black',
            'white',
            'white',
            'black',
            'white',
            'black',
            'white',
            'black',
            'white']

        self.octave_clicked = tk.IntVar()
        self.bottom_keyboard_frame = tk.Frame(self)
        self.bottom_keyboard_frame.pack(side="bottom")

        self.top_keyboard_frame = tk.Frame(self)
        self.top_keyboard_frame.pack(side="bottom")

        self.drop = tk.OptionMenu(self.octave_frame, self.octave_clicked, *octave_options)
        self.drop.pack()

        self.top_buttons = {}
        self.bottom_buttons = {}

        for note in notes:
            self.top_buttons[note] = tk.Button(
                self.top_keyboard_frame,
                bg=key_colors[note % 12],
                command=lambda note=note: self.keypress(note, self.octave_clicked.get(), 0),
            )
            self.top_buttons[note].pack(side="left")

            self.bottom_buttons[note] = tk.Button(
                self.bottom_keyboard_frame,
                bg=key_colors[note % 12],
                command=lambda note=note: self.keypress(note, self.octave_clicked.get(), 1),
            )
            self.bottom_buttons[note].pack(side="left")


    def keypress(self, note: int, octave: int, kb: int):
        midi_note = 12 * (octave + 1) + note
        if self.note_pair[kb] == -1:
            self.note_pair[kb] = midi_note

        if all(x != -1 for x in self.note_pair):
            self.mapper.add_mapping(self.note_pair)
            self.note_pair = [-1, -1]

