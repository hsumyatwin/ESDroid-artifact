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
package = 'com.nloko.android.syncmypix'
activity ='com.nloko.android.syncmypix.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.1)
device.touch(1036,1740, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(718,1092, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(523,824, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(256,728, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(766,1280, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(790,486, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(689,1022, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(645,646, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(416,1774, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(950,1699, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(297,293, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(158,110, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(591,1739, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(112,1152, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)