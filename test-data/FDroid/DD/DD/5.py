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
device.touch(279,805, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(63,998, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(976,65, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(96,1309, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(561,472, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(921,406, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(441,1549, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(922,898, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(811,528, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(639,563, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(807,964, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(577,1141, 'DOWN_AND_UP')
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
