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
package = 'caldwell.ben.bites'
activity ='caldwell.ben.bites.Bites'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.2)
MonkeyRunner.sleep(0.2)
device.touch(4,1371, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(582,784, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(431,846, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(881,1691, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1052,1239, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(946,447, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1000,1859, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(792,1652, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(998,1849, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(247,1894, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(279,1642, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1032,1841, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1015,1873, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1008,1850, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(969,1919, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1059,1914, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(949,1829, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(926,1818, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(998,1917, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(918,1881, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(974,1897, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1079,1867, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(584,1014, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(870,270, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1070,1850, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1000,1862, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(678,1645, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(437,988, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(338,1337, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(443,798, 'DOWN_AND_UP')
