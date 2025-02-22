import pretty_midi
from musical_instrument import MusicalInstrument

# Load the MIDI file
midi_data = pretty_midi.PrettyMIDI("/s/bach/l/under/c835266433/Bytes-n-Beats/midi_solo.mid")

guitar_solo = MusicalInstrument(midi_data.instruments[0])
guitar_solo.print_notation()
print()
print("Note frequencies:")
guitar_solo.print_frequencies()
