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
package = 'org.y20k.transistor'
activity ='org.y20k.transistor.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.1)
MonkeyRunner.sleep(0.1)
device.touch(958,708, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(960,376, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1008,1308, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1023,1678, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(989,1184, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(881,1410, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(925,1594, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(998,1677, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(901,1376, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(892,143, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(941,1431, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1016,260, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1027,122, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(927,1224, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(952,763, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1023,702, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1028,628, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(971,898, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(886,125, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(956,1267, 'DOWN_AND_UP')
