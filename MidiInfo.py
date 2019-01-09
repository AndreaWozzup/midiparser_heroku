import ntpath
from tabulate import tabulate

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class MidiInfo:
    def __init__(self, filename, length, ticks_per_beat, table):
        self.filename = filename
        self.length = length
        self.tick_per_beat = ticks_per_beat
        self.table = table

    def get_minute(self):
        return str(int(self.length//60))

    def get_seconds(self):
        sec = int(self.length % 60)
        return str(format(sec, '02d'))

    def get_bpm(self):
        bpm = str(self.tick_per_beat)
        return bpm

    def get_filename(self):
        filename = path_leaf(self.filename)
        return filename

    def get_table(self):
        headers = ['Track', 'Name', 'Instrument', 'Msg#']
        return tabulate(self.table, headers)

    def get_html_table(self):
        headers = ['TRACK', 'NAME', 'INSTRUMENT', 'MSG#']
        return tabulate(self.table, headers, tablefmt="html")


