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
package = 'com.malliaridis.android.obs.app'
activity ='com.malliaridis.android.obs.app.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(71,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(68,142, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(226,891, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(56,1713, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(68,1249, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(354,1710, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(490,1261, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(854,1707, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(892,1258, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(857,1736, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(775,1563, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(872,1725, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(546,1420, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(294,1707, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(517,1572, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1060,1261, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(889,783, 'DOWN_AND_UP')
