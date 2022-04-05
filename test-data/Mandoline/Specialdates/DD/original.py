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
package = 'com.alexstyl.specialdates'
activity ='com.alexstyl.specialdates.ui.activity.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(951, 1675, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(417, 842, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(473, 1271, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(385, 675, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(646, 889, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(420, 1417, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(875, 915, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(913, 200, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(945, 1670, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(400, 838, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(464, 1280, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(391, 681, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(633, 887, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(415, 1415, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(870, 910, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(910, 195, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)