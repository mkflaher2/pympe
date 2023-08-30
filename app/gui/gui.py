import tkinter as tk

import copy

from tkinter import ttk

from app.utils.mapper import NoteMapper

class PympeFrontend(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        self.clicked_note = 0

        self.octave_frame = tk.Frame(self)
        self.octave_frame.pack()

        octave_options = [0, 1, 2, 3, 4, 5, 6, 7]
        notes = range(12)
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
        self.keyboard_frame = tk.Frame(self)
        self.keyboard_frame.pack(side="bottom")

        self.drop = tk.OptionMenu(self.octave_frame, self.octave_clicked, *octave_options)
        self.drop.pack()

        self.buttons = {}

        for note in notes:
            self.buttons[note] = tk.Button(
                self.keyboard_frame,
                bg=key_colors[note],
                command=lambda note=note: self.keypress(note, self.octave_clicked.get())
            )
            self.buttons[note].pack(side="left")

    def keypress(self, note: int, octave: int):
        print(note, octave)
