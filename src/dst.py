# Data structure wrapping Dst.

class Dst:
    def __init__(self):
        self._data = dict()  # maps timestamp to value
    
    def add_item(self, timestamp, val):
        self._data[timestamp] = val

    def head(self, n):
        cnt = 0
        for ts, val in self._data.items():
            print('Timestamp = {}, Value = {}'.format(ts, val))
            cnt += 1
            if cnt >= n:
                break