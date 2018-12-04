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
            # Check if any of the topics exist in the topics exists in the log file
        # try:
        #     self.ulog = pyulog.ULog(filepath, topics)
        # except:
        #     print("Not a single topic that is needed for this test exists in the provided ulog file. Abort test")
        #     assert False

        # # Check for every topic separately if it exists in the log file
        # for i in range(len(self.ulog.data_list)):
        #     if self.ulog.data_list[i].name in topics:
        #         idx = topics.index(self.ulog.data_list[i].name)
        #         topics.pop(idx)

        # if len(topics) > 0:
        #     print("\033[93m" + "The following topics do not exist in the provided ulog file: " + "\033[0m")
        #     print(topics)
        #     pytest.skip("Skip this test because topics are missing")
        # else:
        #     self.df = ulogconv.merge(ulogconv.createPandaDict(self.ulog))

#
    # def test_1(self, filepath):
        # TestSomething.setup_dataframe(self, filepath)
#        assert True
#    def test_2(self, filepath):
        # TestSomething.setup_dataframe(self, filepath)
#        assert True
