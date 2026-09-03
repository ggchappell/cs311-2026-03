# timeofday.py
# Glenn G. Chappell
# Started: 2026-08-31
# Updated: 2026-09-02
"""Class TimeOfDay: store & manipulate a time of day.
For CS 311 Fall 2026
"""

import copy  # For .deepcopy


# **********************************************************************
# Class TimeOfDay - Internal-use constants
# **********************************************************************


_SECS_IN_MIN = 60
_SECS_IN_HR = 60*_SECS_IN_MIN
_SECS_IN_DAY = 24*_SECS_IN_HR


# **********************************************************************
# Class TimeOfDay - Class definition
# **********************************************************************


class TimeOfDay:
    # ***** TimeOfDay: List of attributes *****

    # - _secs: seconds past midnight - must be int in [0, _SECS_IN_DAY).

    # ***** TimeOfDay: Initializer *****

    def __init__(self, hh=None, mm=None, ss=None):
        """Set time given hrs, mins, secs, or midnight if not given."""

        if hh is not None:
            assert isinstance(hh, int)
            assert isinstance(mm, int)
            assert isinstance(ss, int)
        else:
            hh = 0
            mm = 0
            ss = 0

        self.set_time(hh, mm, ss)

    # ***** TimeOfDay: Normal methods *****

    def get_time(self):
        """Return tuple holding hrs, mins, secs past midnight."""

        assert isinstance(self._secs, int)
        assert 0 <= self._secs < _SECS_IN_DAY

        hh = self._secs // _SECS_IN_HR
        mm = (self._secs - hh*_SECS_IN_HR) // _SECS_IN_MIN
        ss = self._secs - hh*_SECS_IN_HR - mm*_SECS_IN_MIN
        return (hh, mm, ss)

    def set_time(self, hh, mm, ss):
        """Given hrs, mins, secs, set time."""

        assert isinstance(hh, int)
        assert isinstance(mm, int)
        assert isinstance(ss, int)

        self._secs = hh*_SECS_IN_HR + mm*_SECS_IN_MIN + ss
        self._fix_secs()

    # ***** TimeOfDay: Operators & string conversion *****

    # __add__: binary + operator
    def __add__(self, chg):
        """Return new object advanced by chg seconds."""

        assert isinstance(chg, int)

        cpy = copy.deepcopy(self)
        cpy += chg
        return cpy

    # __sub__: binary - operator
    def __sub__(self, chg):
        """Return new object reduced by chg seconds."""

        assert isinstance(chg, int)

        cpy = copy.deepcopy(self)
        cpy -= chg
        return cpy

    # __iadd__: += operator
    def __iadd__(self, chg):
        """Advance current object by chg seconds."""

        assert isinstance(chg, int)

        self._secs += chg
        self._fix_secs()
        return self

    # __isub__: -= operator
    def __isub__(self, chg):
        """Reduce current object by chg seconds."""

        assert isinstance(chg, int)

        self._secs -= chg
        self._fix_secs()
        return self

    def __str__(self):
        """Informal string conversion: ' 8:30:05'."""

        assert isinstance(self._secs, int)
        assert 0 <= self._secs < _SECS_IN_DAY

        hh, mm, ss = self.get_time()
        result = ""
        if hh < 10:
            result = " "
        result += str(hh) + ":"
        if mm < 10:
            result += "0"
        result += str(mm) + ":"
        if ss < 10:
            result += "0"
        result += str(ss)
        return result

    def __repr__(self):
        """Formal string conversion: ' 8:30:05'."""

        assert isinstance(self._secs, int)
        assert 0 <= self._secs < _SECS_IN_DAY

        return str(self)

    # ***** TimeOfDay: Private methods *****

    def _fix_secs(self):
        """Private. Ensure attribute _secs lies in range."""

        assert isinstance(self._secs, int)

        if self._secs >= _SECS_IN_DAY or self._secs < 0:
            self._secs %= _SECS_IN_DAY
            # Above line does the right thing when _secs < 0

# End class TimeOfDay

