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
device.touch(1048,1420, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(868,1588, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(707,126, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1077,527, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(32,1277, 'DOWN_AND_UP')
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
