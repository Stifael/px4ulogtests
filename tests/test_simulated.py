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


# class TestSomething:
# 
    # def setup_dataframe(self, filepath):
    #     topics = [
    #         "topic1",
    #         "topic2",
    #     ]
    #     self.ulog = pyulog.ULog(filepath, topics)
    #     self.df = ulogconv.merge(ulogconv.createPandaDict(self.ulog))
#
    # def test_1(self, filepath):
        # TestSomething.setup_dataframe(self, filepath)
#        assert True
#    def test_2(self, filepath):
        # TestSomething.setup_dataframe(self, filepath)
#        assert True
