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
package = 'com.gmail.altakey.effy'
activity ='com.gmail.altakey.effy.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
device.touch(790,485, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(689,1029, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(645,648, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(416,1792, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(950,1715, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(297,289, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(158,103, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(591,1756, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(112,1160, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(444,1426, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1070,918, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(806,1350, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(883,1536, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(569,1642, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(144,208, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1057,1331, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(772,314, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(500,70, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(77,674, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(992,1842, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(998,1868, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(816,1710, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)