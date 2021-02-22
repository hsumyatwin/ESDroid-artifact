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
package = 'com.mitzuli'
activity ='com.mitzuli.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(1001,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(863,125, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(355,1601, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(247,1839, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(80,154, 'DOWN_AND_UP')
