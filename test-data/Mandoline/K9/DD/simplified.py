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
package = 'com.fsck.k9'
activity ='com.fsck.k9.activity.Accounts'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(842,1754, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(540,1417, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(68,1718, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(68,1406, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(67,1705, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(112,1410, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(857,1716, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(437,1408, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(998,1719, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(200,1698, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(241,1877, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(763,1730, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(241,1871, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(311,1757, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(71,1710, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(253,1859, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(273,1377, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(740,1716, 'DOWN_AND_UP')
