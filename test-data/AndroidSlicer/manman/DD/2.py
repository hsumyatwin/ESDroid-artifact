#start monkey test seedNo 0
import os;
from subprocess import Popen
from subprocess import PIPE
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.MonkeyDevice import takeSnapshot
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
from com.android.monkeyrunner import MonkeyView
import random
import sys
import subprocess
from sys import exit
from random import randint
device = MonkeyRunner.waitForConnection()
package = 'com.adonai.manma'
activity ='com.adonai.manman.MainPagerActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(945,1127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(982,153, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(699,932, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(547,973, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(396,899, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(760,632, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(12,1284, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(805,1122, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(254,746, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(985,365, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(4,533, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(965,589, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(463,1260, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1026,117, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(707,285, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(253,972, 'DOWN_AND_UP')
