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
package = 'com.liato.bankdroid'
activity ='com.liato.bankdroid.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.6)
MonkeyRunner.sleep(0.6)
device.touch(314,309, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(472,1105, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(98,1608, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(537,999, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(759,1107, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1012,723, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(62,380, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(445,1207, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(769,1718, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1026,1153, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(779,119, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(165,232, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1020,132, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(819,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(790,491, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(689,1033, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(645,653, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(416,1792, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(950,1716, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(297,296, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(158,111, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(591,1756, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(112,1163, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(444,1427, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1070,922, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(806,1352, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(883,1537, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(569,1643, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(144,216, 'DOWN_AND_UP')
