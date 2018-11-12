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


def getfilepath():
    currentpath = os.path.dirname(os.path.realpath(__file__))
    for f in os.listdir(currentpath + "/../inputlog"):
        if f:
            filepath = f
            break
    return currentpath + "/../inputlog/" + filepath


def setup_module(module):
    """
    Check if file exists. Otherwise don't bother to run all the tests
    """
    filepath = getfilepath()
    # ensure it is a ulg file
    base, ext = os.path.splitext(filepath)
    if ext.lower() not in (".ulg") or not filepath:
        pytest.exit("Either no file present or not an .ulg file.")


class TestRTLHeight:
    # The return to home height changes with the distance from home
    # mode was triggered
    # check the height above ground while the drone returns to home. compare it with 
    # the allowed maximum or minimum heights, until the drone has reached home and motors have been turned off

   def setup_class(self):
        # get the required data
        filepath = getfilepath()
        topics = [
            "vehicle_local_position",
            "vehicle_status",
        ]
        self.ulog = pyulog.ULog(filepath, topics)
        self.df = ulogconv.merge(ulogconv.createPandaDict(self.ulog))


   def test_rtl(self):
       # TODO adjust this test to also work with cone (only for yuneec)
        NAVIGATION_STATE_AUTO_RTL = 5           # see https://github.com/PX4/Firmware/blob/master/msg/vehicle_status.msg
        max_height_within_RTL_MIN_DIST = 10     # within this radius, the drone should not go higher than this value after RTL has been triggered
        thresh = 1                              # Threshold for position inaccuracies

        # drone parameters: below rtl_min_dist, the drone follows different rules than outside of it.
        rtl_min_dist = (
            loginfo.get_param(self.ulog, "RTL_MIN_DIST", 0)
        )
        rtl_return_alt = (
            loginfo.get_param(self.ulog, "RTL_RETURN_ALT", 0)
        )

        posanl.add_horizontal_distance(self.df)

        # Check vehicle status for RTL trigger
        # store all distance and height values that are reached ONLY DURING RTL in a new array
        distance_after_RTL = []
        height_after_RTL = []
        for i in range(self.df.T_vehicle_status_0__F_nav_state.count() - 1):
            # at least two consecutive T_vehicle_status_0__F_nav_state values have to be equal to 
            # NAVIGATION_STATE_AUTO_RTL in order to confirm that RTL has been triggered
            if self.df.T_vehicle_status_0__F_nav_state.iloc[i] == NAVIGATION_STATE_AUTO_RTL and \
            self.df.T_vehicle_status_0__F_nav_state.iloc[i+1] == NAVIGATION_STATE_AUTO_RTL:
                distance_after_RTL.append(self.df.T_vehicle_local_position_0__NF_abs_horizontal_dist.iloc[i])
                height_after_RTL.append(abs(self.df.T_vehicle_local_position_0__F_z.iloc[i]))
        
        # check if a value of the z position after triggering RTL is larger than allowed value
        if (distance_after_RTL[0] < rtl_min_dist) & (height_after_RTL[0] < max_height_within_RTL_MIN_DIST):  # TODO: is this second statement correct? what about 'cone'shape in a certain radius around home?
            assert max(height_after_RTL) < max_height_within_RTL_MIN_DIST

        elif (distance_after_RTL[0] < rtl_min_dist) & (height_after_RTL[0] > max_height_within_RTL_MIN_DIST):  # TODO: is this second statement correct? what about 'cone'shape in a certain radius around home?
            assert max(height_after_RTL) < height_after_RTL[0] + thresh

        elif (distance_after_RTL[0] > rtl_min_dist) & (height_after_RTL[0] < rtl_return_alt): 
            assert max(height_after_RTL) < rtl_return_alt + thresh

        elif (distance_after_RTL[0] > rtl_min_dist) & (height_after_RTL[0] > rtl_return_alt): 
            assert max(height_after_RTL) < height_after_RTL[0] + thresh




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
