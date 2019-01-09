from mido import MidiFile
from GMMapping import GMMapping
from MidiInfo import MidiInfo
import logging

logging.basicConfig(filename='MidiParser.log', level=logging.INFO)


def parse(filename):
    mid = MidiFile(filename)
    table = []
    bpm = []
    for i, track in enumerate(mid.tracks):
        instrument = "No instrument"
        table.append([i, track.name, instrument, len(track)])
        for msg in track:
            if hasattr(msg, "type") and hasattr(msg, "tempo") and (msg.type == "set_tempo"):
                bpm.append(int(round(60000000 / msg.tempo)))
            if hasattr(msg, "type") and hasattr(msg, "program") and (msg.type == "program_change"):
                instrument = GMMapping[msg.program]
                table[i] = [i, track.name, instrument, len(track)]
    midi_info = MidiInfo(filename, mid.length, bpm, table)
    logging.info("Filename: " + midi_info.get_filename())
    logging.info("Length: " + midi_info.get_minute() + ":" + midi_info.get_seconds())
    logging.info("BPM: " + midi_info.get_bpm())
    logging.info(midi_info.get_table())

    return midi_info


# if __name__== "__main__":
#     midi_parser()
