"""
Tests that only make sense for simulated flights.
"""
from uloganalysis import attitudeanalysis as attanl
from uloganalysis import ulogconv
from uloganalysis import loginfo
import pyulog
import os
import numpy as np
import pytest


def getfilepath():
    currentpath = os.path.dirname(os.path.realpath(__file__))
    for f in os.listdir(currentpath + "/../log"):
        if f:
            filepath = f
            break
    return currentpath + "/../log/" + filepath


def setup_module(module):
    """
    Check if file exists. Otherwise don't bother to run all the tests
    """
    filepath = getfilepath()
    # ensure it is a ulg file
    base, ext = os.path.splitext(filepath)
    if ext.lower() not in (".ulg") or not filepath:
        pytest.exit("Either no file present or not an .ulg file.")


# class TestSomething:
#
#    def setup_class(self):
#        # get the required data
#        filepath = getfilepath()
#        topics = [
#            ""
#        ]
#        self.ulog = pyulog.ULog(filepath, topics)
#        self.df = ulogconv.merge(ulogconv.createPandaDict(self.ulog))
#
#    def test_1(self):
#        assert True
#    def test_2(self):
#        assert True
