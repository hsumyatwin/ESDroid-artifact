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
