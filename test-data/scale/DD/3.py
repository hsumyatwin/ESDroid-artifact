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
package = 'com.davemorrissey.labs.subscaleview.sample'
activity ='com.davemorrissey.labs.subscaleview.sample.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(253,1357, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(744,252, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(817,858, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1051,603, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(238,1514, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(730,1130, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(18,1119, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(901,551, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(307,1028, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(409,406, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1055,760, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(85,165, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(216,754, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(98,883, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(780,355, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1048,983, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(564,1036, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(267,826, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(29,1364, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(172,1276, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(203,151, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1043,902, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(928,841, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(338,1266, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(67,614, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(553,1079, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(629,183, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(225,1090, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(71,142, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(655,1557, 'DOWN_AND_UP')
