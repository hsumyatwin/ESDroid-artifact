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
device.touch(1070,918, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(806,1343, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(883,1526, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(569,1631, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(144,220, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1057,1325, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(772,324, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(500,84, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(77,679, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(366,1561, 'DOWN_AND_UP')
