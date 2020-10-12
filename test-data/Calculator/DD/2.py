#start monkey test
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
easy_device=EasyMonkeyDevice(device)
package = 'com.muledog.calculator'
activity ='com.muledog.calculator.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(702,990, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(608,1449, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(862,183, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(991,235, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1006,1496, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(638,904, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(77,1217, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(59,1698, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(78,1649, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(66,633, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(168,1213, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(250,1322, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(57,1180, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(140,721, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(609,600, 'DOWN_AND_UP')
