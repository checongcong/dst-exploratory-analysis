# IAGAParser parses the IAGA2002 format into DST data.
# IAGA2002 format: http://wdc.kugi.kyoto-u.ac.jp/mdplt/format/iaga2002.html

import sys
import time

from datetime import datetime
from dst import Dst

class IAGAParser:
    def __init__(self):
        pass

    def parse_file(self, filename):
        dst = Dst()

        # Open data file
        try:
            f = open(filename, 'r')
        except IOError:
            print("Failed to read file: ", filename)
            sys.exit()

        # Parse each line
        with f:
            for line in f:
                items = self._parse_line(line)
                if not items:
                    continue
                assert 2 == len(items)  # should be (timestamp, val)
                dst.add_item(items[0], items[1])

        return dst

    def _parse_line(self, line):
        line = line.strip()
        if not line or line.endswith('|'):
            return None
        items = line.split()
        assert 4 == len(items) # should be (date, time, day-of-year, value)

        # ("2000-01-08", "20:00:00.000") -> "2000-01-08 20:00:00"
        dt_str = items[0] + ' ' + items[1][:8]
        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        return (time.mktime(dt.timetuple()), float(items[3]))