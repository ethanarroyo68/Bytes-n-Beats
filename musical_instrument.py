class MusicalInstrument:
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self, instrument):
        self.instrument = instrument

    @staticmethod
    def midi_to_note(midi_note):
        """Return the western notation note."""
        return MusicalInstrument.note_names[midi_note % 12]

    @staticmethod
    def midi_to_octave(midi_note):
        """Return the western notation octave."""
        return (midi_note // 12) - 1
    
    def print_note_count(self):
        note_count = self.count_notes()
        for i in range(12):
            print(f'{self.note_names[i]} : {note_count[i]}')

    def print_notation(self):
        """Print every note in the melody."""
        for note in self.instrument.notes:
            print(self.midi_to_note(note.pitch), end=" ")

    def midi_to_melody(self):
        """Convert monophonic MIDI melody to an array of notes."""
        return [f"{self.midi_to_note(note.pitch)}{self.midi_to_octave(note.pitch)}" for note in self.instrument.notes]

    def count_notes(self):
        """Count each instance of a given note in the melody."""
        note_frequencies = [0] * 12
        for note in self.instrument.notes:
            note_frequencies[note.pitch % 12] += 1
        return note_frequencies
