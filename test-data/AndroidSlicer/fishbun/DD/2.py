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
package = 'com.sangcomz.fishbundemo'
activity ='com.sangcomz.fishbundemo.ChoiceActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
MonkeyRunner.sleep(1)
device.touch(231,651, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(270,1343, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(98,532, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(203,589, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(819,157, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(93,1613, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(577,224, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(574,203, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(191,1598, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(378,1774, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(622,1117, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(295,960, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(983,110, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(296,1228, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(311,187, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(244,318, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(652,1330, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(328,1153, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(38,899, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(100,1300, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(469,1487, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(250,1851, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(253,1862, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(992,441, 'DOWN_AND_UP')
