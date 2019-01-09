import ntpath
from tabulate import tabulate

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


class MidiInfo:
    def __init__(self, filename, length, bpm, table):
        self.filename = filename
        self.length = length
        if bpm == []:
            self.bpm = [120]
        else:
            self.bpm = bpm
        self.table = table

    def get_minute(self):
        return str(int(self.length//60))

    def get_seconds(self):
        sec = int(self.length % 60)
        return str(format(sec, '02d'))

    def get_bpm(self):
        result = str(self.bpm[0])

        for i in range(1, len(self.bpm)):
            if self.bpm[i] != self.bpm[i - 1]:
                result = result + " => " + str(self.bpm[i])
        return result

    def get_filename(self):
        filename = path_leaf(self.filename)
        return filename

    def get_table(self):
        headers = ['Track', 'Name', 'Instrument', 'Msg#']
        return tabulate(self.table, headers)

    def get_html_table(self):
        headers = ['TRACK', 'NAME', 'INSTRUMENT', 'MSG#']
        return tabulate(self.table, headers, tablefmt="html")


