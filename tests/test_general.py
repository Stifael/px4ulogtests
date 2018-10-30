"""
Tests that can be applied to real test-flights as well
as simulated test-flights
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


class TestAttitude:
    """
    Test Attitude related constraints
    """

    def setup_class(self):
        filepath = getfilepath()
        topics = [
            "vehicle_attitude",
            "vehicle_attitude_setpoint",
            "vehicle_status",
        ]
        self.ulog = pyulog.ULog(filepath, topics)
        self.df = ulogconv.merge(ulogconv.createPandaDict(self.ulog))

    def test_tilt_desired(self):

        # During Manual / Stabilized and Altitude, the tilt threshdol should not exceed
        # MPC_MAN_TILT_MAX

        attanl.add_desired_tilt(self.df)
        man_tilt = (
            loginfo.get_param(self.ulog, "MPC_MAN_TILT_MAX", 0) * np.pi / 180
        )
        assert self.df[
            (
                (self.df.T_vehicle_status_0__F_nav_state == 0)
                | (self.df.T_vehicle_status_0__F_nav_state == 1)
            )
            & (
                self.df.T_vehicle_attitude_setpoint_0__NF_tilt_desired
                > man_tilt
            )
        ].empty


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
