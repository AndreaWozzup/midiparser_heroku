from mido import MidiFile
from GMMapping import GMMapping
from MidiInfo import MidiInfo


def parse(filename):
    mid = MidiFile(filename)
    table = []
    for i, track in enumerate(mid.tracks):
        instrument = "No instrument"
        table.append([i, track.name, instrument, len(track)])
        for msg in track:
            if hasattr(msg, "type") and hasattr(msg, "program") and (msg.type == "program_change"):
                instrument = GMMapping[msg.program]
                table[i] = [i, track.name, instrument, len(track)]
    midi_info = MidiInfo(filename, mid.length, mid.ticks_per_beat, table)
    print("Filename: " + midi_info.get_filename())
    print("Length: " + midi_info.get_minute() + ":" + midi_info.get_seconds())
    print("BPM: " + midi_info.get_bpm())
    print(midi_info.get_table())

    return midi_info


# if __name__== "__main__":
#     midi_parser()
