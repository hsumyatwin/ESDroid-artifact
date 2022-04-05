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
package = 'com.mkulesh.micromath.plus'
activity ='com.mkulesh.micromath.plus.MainActivityPlus'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(1029, 139, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(886, 250, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(872, 1003, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(951, 1578, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(320, 1021, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)