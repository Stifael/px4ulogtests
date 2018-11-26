"""
Tests that only make sense for simulated flights.
"""
from uloganalysis import attitudeanalysis as attanl
from uloganalysis import positionanalysis as posanl
from uloganalysis import ulogconv
from uloganalysis import loginfo
import pyulog
import os
import numpy as np
import pytest

def file_path(self, topics, filepath):
    self.ulog = pyulog.ULog(filepath, topics)
    self.df = ulogconv.merge(ulogconv.createPandaDict(self.ulog))

    # ensure it is a ulg file
    base, ext = os.path.splitext(filepath)
    if ext.lower() not in (".ulg") or not filepath:
        pytest.exit("Either no file present or not an .ulg file.")


# class TestSomething:
#
#    def test_1(self, filepath):
        # topics = [
            # "topic1",
            # "topic2",
        # ]
        # file_path(self, topics, filepath)
#        assert True
#    def test_2(self, filepath):
        # topics = [
            # "topic1",
            # "topic2",
        # ]
        # file_path(self, topics, filepath)
#        assert True
