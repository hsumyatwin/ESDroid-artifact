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
package = 'com.mikepenz.fastadapter.app'
activity ='com.mikepenz.fastadapter.app.SampleActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
MonkeyRunner.sleep(1)
device.touch(48,131, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(356,640, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(74,160, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(80,133, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(415,1003, 'DOWN_AND_UP')
