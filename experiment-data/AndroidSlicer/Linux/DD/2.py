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
package = 'ru.meefik.linuxdeploy'
activity ='ru.meefik.linuxdeploy.activity.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
MonkeyRunner.sleep(1)
device.touch(203,589, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(819,157, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(93,1613, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(577,224, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(574,203, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(191,1598, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(378,1774, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(622,1117, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(295,960, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1021,451, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(983,110, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(296,1228, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(311,187, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(244,318, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(652,1330, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(328,1153, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(38,899, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(100,1300, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1035,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(348,660, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(82,121, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(399,417, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1017,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(634,910, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(531,1722, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(115,1406, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(892,684, 'DOWN_AND_UP')
