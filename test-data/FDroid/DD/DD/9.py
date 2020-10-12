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
package = 'org.fdroid.fdroid'
activity ='org.fdroid.fdroid.FDroid'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(498,219, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(358,1032, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1037,1601, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(745,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(599,1799, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(700,1750, 'DOWN_AND_UP')
