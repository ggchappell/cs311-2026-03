# timeofday.py  UNFINISHED
# Glenn G. Chappell
# 2026-08-31
"""Class TimeOfDay: store & manipulate a time of day.
For CS 311 Fall 2026
"""


class TimeOfDay:
    # Attributes:
    # - _secs: seconds past midnight - must be int from 0 to 24*60*60-1

    # Initializer

    def __init__(self, hh=None, mm=None, ss=None):
        """Set time given hrs, mins, secs, or midnight if not given."""
        if hh is None:
            hh = 0
        if mm is None:
            mm = 0
        if ss is None:
            ss = 0
        assert isinstance(hh, int)
        assert isinstance(mm, int)
        assert isinstance(ss, int)

        self.set_time(hh, mm, ss)

    # Normal methods

    def get_time(self):
        """Return tuple holding hrs, mins, secs past midnight."""

        hh = self._secs // 60*60
        mm = (self._secs - hh*60*60) // 60
        ss = self._secs - hh*60*60 - mm*60
        return (hh, mm, ss)

    def set_time(self, hh, mm, ss):
        """Given hrs, mins, secs, set time."""

        assert isinstance(hh, int)
        assert isinstance(mm, int)
        assert isinstance(ss, int)

        self._secs = hh*60*60 + mm*60 + ss
        self._fix_secs()

    # Operators & string conversion

    def __add__(self, chg):
        return self  # Dummy

    def __sub__(self, chg):
        return self  # Dummy

    def __iadd__(self, chg):
        return self  # Dummy

    def __isub__(self, chg):
        return self  # Dummy

    def __str__(self):
        """Informal string conversion: ' 8:30:05'."""
        hms = self.get_time()
        result = ""
        if hms[0] < 10:
            result = " "
        result += str(hms[0]) + ":"
        if hms[1] < 10:
            result += "0"
        result += str(hms[1]) + ":"
        if hms[2] < 10:
            result += "0"
        result += str(hms[2])
        return result

    def __repr__(self):
        """Formal string conversion: ' 8:30:05'."""

        return str(self)

    # Private methods

    def _fix_secs(self):
        """Private. Ensure attribute _secs lies in range."""

        if self._secs >= 24*60*60 or self._secs < 0:
            self._secs %= 24*60*60  # Does right thing when _secs < 0

