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
device.touch(790,491, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(689,1024, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(645,650, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(416,1772, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(950,1697, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(297,298, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(158,117, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(591,1737, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(112,1153, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(444,1413, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1070,916, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(806,1339, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(883,1521, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(569,1625, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(144,220, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1057,1320, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(112,1153, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(444,1413, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1070,916, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(806,1339, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(883,1521, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(569,1625, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(144,220, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1057,1320, 'DOWN_AND_UP')
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
