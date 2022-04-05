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
package = 'org.gnucash.android'
activity ='org.gnucash.android.ui.account.AccountsActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(581,1736, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(952,1519, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(929,989, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(671,1383, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(921,1707, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1054,1727, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1020,1712, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(819,658, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1039,1786, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(852,1751, 'DOWN_AND_UP')
