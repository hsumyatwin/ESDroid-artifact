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
package = 'wangdaye.com.geometricweather'
activity ='wangdaye.com.geometricweather.ui.activity.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(772,323, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(500,84, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(77,676, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(366,1556, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1050,1567, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(662,385, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(235,1548, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(10,1269, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(833,1304, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(228,1425, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1021,101, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(426,1547, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(849,1787, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(954,370, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1039,1324, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(732,1462, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(477,872, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(921,941, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1072,1746, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(381,158, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(77,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(247,1891, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1033,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(696,267, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(351,1045, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(331,1035, 'DOWN_AND_UP')
