# pympe
A python prototype for applying MIDI Polyphonic Expressions (MPE) pitch bending to any MIDI input, inspired by the Pitch Innovations Fluid Chords plugin.

### TODO
- allow user to select from available MIDI devices (is currently hardcoded)
- add feature for multiple stages of chord bend/progression, either by midi CC/channel or in a single slide of the modwheel
- make the GUI suck less (add visual indicator for mappings, maybe use buttons instead of dropdown for octave selection)
- better DAW integration - either usable as an lv2 plugin or an insert
- ability to save and import/export chord mapping
- sometimes pitches for channels don't get unbent - find a better way to treat notes as objects and reset modwheel/pitchwheel values
