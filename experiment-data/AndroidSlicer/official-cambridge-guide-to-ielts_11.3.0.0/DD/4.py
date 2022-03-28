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
package = 'air.com.yudu.ReaderAIR4697674'
activity ='com.yudu.androidreader.BaseActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
device.touch(790,492, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(689,1028, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(645,652, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(416,1778, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(950,1703, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(297,299, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(158,117, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(591,1743, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(112,1157, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(444,1418, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1050,1573, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(662,386, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(235,1553, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(10,1273, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(833,1308, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(228,1430, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1021,101, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(426,1552, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(849,1793, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(954,371, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1039,1328, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(732,1466, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(477,875, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(921,944, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1072,1751, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(381,158, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(77,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(522,1756, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1069,1403, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(542,518, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(877,1736, 'DOWN_AND_UP')
