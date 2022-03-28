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
device.touch(625,516, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(588,1586, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1025,1651, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(535,62, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(10,495, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(496,38, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(186,173, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(262,996, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(581,1736, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(952,1519, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(754,1577, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(979,1110, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(886,1824, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1054,1405, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(929,989, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(671,1383, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(719,1800, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(921,1707, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1054,1727, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1020,1712, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(767,553, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1043,614, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(622,655, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(627,529, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(745,459, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(485,605, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1078,657, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(819,658, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(970,1088, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(923,1591, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(626,1686, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(899,1527, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(972,1827, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1039,1786, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(852,1751, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)